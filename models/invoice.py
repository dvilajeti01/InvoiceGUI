import pdfkit
import jinja2
import pandas as pd
from datetime import datetime as dt

from models.entry import Entry
from models.mail_info import MailInfo

COLUMNS = ['Date', 'Description', 'Quantity', 'Rate', 'Amount']


class Invoice:
    def __init__(self):

        self.date = None
        self.due_date = None
        self.sender = None
        self.recipient = None
        self.entries = pd.DataFrame(columns=COLUMNS)

    def append_entry(self, entry):
        # Seems redundant but this decouples the entry from the invoice
        # in case column labels change you dont have to make changes to
        # the entry class
        entry_values = {
            'Date': entry.date,
            'Description': entry.description,
            'Quantity': entry.quantity,
            'Rate': entry.rate,
            'Amount': entry.amount
        }

        # Append entry to dataframe
        self.entries = self.entries.append(entry_values, ignore_index=True)

    def remove_entry(self, entry):
        # Removes an entry from the dataframe
        # If duplicate only first instance is removed
        for index, row in self.entries.iterrows():
            if row.tolist() == entry.to_list():
                self.entries = self.entries.drop(index)
                break

    def get_entries(self, date):

        # Get all entries for a given date
        entries = self.entries[self.entries['Date'] == date]

        # Look into if this works
        res = entries.values.tolist()

        return res

    def has_date(self, date):
        # Checks to see if there is an entry for a given date
        if self.entries[self.entries['Date'] == date].size > 0:
            return True
        else:
            return False

    def to_html(self, data, file_name):

        # Load template
        template_loader = jinja2.FileSystemLoader(searchpath="./")
        template_env = jinja2.Environment(loader=template_loader)

        TEMPLATE_FILE = "invoice_template.html"

        template = template_env.get_template(TEMPLATE_FILE)

        # Render invoice using invoice data
        output_text = template.render(
            invoice_date=self.date,
            invoice_due_date=self.due_date,
            recipient=self.recipient,
            sender=self.sender,
            df=data.to_html())

        # Write to and save HTML file
        html_file = open(file_name + '.html', 'w')
        html_file.write(output_text)
        html_file.close()

    def to_pdf(self, file_name):

        # Convert HTML file to a PDF file
        pdfkit.from_file(input=file_name + '.html', output_path=file_name +
                         '.pdf')

    def generate_invoice(self, file_name='invoice'):

        self.date = dt.today().strftime('%m/%d/%Y')

        final_invoice = self.entries

        for index, row in final_invoice.iterrows():
            row['Date'] = dt.strptime(row['Date'], '%m/%d/%Y')

        final_invoice = final_invoice.sort_values(by='Date', ascending=True)
        final_invoice = final_invoice.sort_index()

        COLUMNS_TO_TOTAL = ['Quantity', 'Amount']
        final_invoice.loc['Total', :] = final_invoice[COLUMNS_TO_TOTAL].sum(
            axis=0, numeric_only=True)

        final_invoice = final_invoice.fillna(' ')

        self.to_html(final_invoice, file_name)
        self.to_pdf(file_name)
