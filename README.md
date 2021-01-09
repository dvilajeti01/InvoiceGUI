# InvoiceGUI

### Project Summary
    InvoiceGUI was my attempt at building my first python GUI. 
InvoiceGUI is a visual invoice generator. The idea was inspired by the invoices I had to submit at work which 
were tedious to put together. The project was fruitful in the sense that it allowed me to gain experience building a GUI, practice my
python skills and build something of use. A key aspect of the project or rather lacking aspect is the absense of a database. This was intentional since it allowed me to proceed faster with the project and didn't seem fitting for a tool so small and basic. I did not believe there would be a real advantage to implementing a database for the project in its standing condition. Although with the understanding that I(or someone else) would wish to extend the project, the application was built with the MVC architecture in mind. This would allow for the addition of a database, additional features, and general up keep for the source code. 

    In the end, the GUI itself lacks features common to most user friendly applications in the market 
    and it is not the most aesthetically pleasing application ever (lol).
Nonetheless, it does accomplish the task promised which is is producing invoices
from user input. And like mentioned above it was a a fun learning experinece setting me up for another more advanced and applicable project.

### Installation

First you will need to install wkhtmltopdf.

#### Windows/Mac:

Download installer from the page below.

https://wkhtmltopdf.org/downloads.html

#### Linux: 

```bash
sudo apt update
sudo apt install openssl build-essential xorg libssl-dev
sudo apt install -y wkhtmltopdf
```

Additionally you may have to run the command below in the case of an error concerning libQt5Core

```bash
strip --remove-section=.note.ABI-tag /usr/lib/x86_64-linux-gnu/libQt5Core.so.5
```

After having installed wkhtmltopdf you will want to clone this project.

```git
git clone https://github.com/dvilajeti01/InvoiceGUI.git
```

And run the following command to install the required python modules.

```bash
pip install -r requirements.txt
```

Finally executing the invoice_gui.py file will open up the application and you're on your way!

```
python invoice_gui.py
```

#### Implicit requirements
* python >= 3.8.5
* git >= 2.25.1
