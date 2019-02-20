from faker import Faker
import random
from random import randint
import click
from dclogger.dclogger import error, info, dcprint
import string


@click.command()
@click.argument('field')
def dataset_test(field):
    dg = DataGenerator()
    out = dg.generate(field)
    #dcprint(out)


class DataGenerator:
    def __init__(self):
        self.aFake = Faker()
        return

    def generate(self, field, row_no=None, part_no=None):
        ret_value = None
        if field == "Address_1":
            ret_value = self.aFake.address().split('\n', 1)[0]
        elif field == "Address_2":
            ret_value = self.aFake.address().split('\n', 1)[1]
        elif field=="Taxn":
            tax_names = ["GST","CST", "TAX", self.aFake.currency()[0]]
            ret_value = tax_names[randint(0,3)]
        elif field == "Amount":
            if randint(1, 100) < 10:
                currency = "$"
            else:
                currency = self.aFake.currency()[0]
            ret_value = currency + ' ' + str(randint(1, 1000000))
        elif field == "Text":
            ret_value = self.aFake.text()
        elif field == "Address":
            if part_no is None or part_no == 0:
                ret_value = self.aFake.address()
            elif part_no > 2:
                ret_value = ''
            else:
                ret_value = self.aFake.address().split('\n', 1)[part_no - 1]
        elif field == "NumberPercent":
            ret_value = str(randint(0, 99)) + ' %'
        elif field == "Number":
            ret_value = str(randint(1, 100000000))
        elif field == 'Date':
            formats = [
                "%Y-%m-%d",
                "%m/%d/%Y",
                "%d-%b-%y",
                "%d-%B-%y",
                "%x",
                "%B-%d-%y",
                "%m-%d-%Y",
                "%Y %m %d",
                "%d %m %Y",
                "%d %B %y",     # ["%Y-%m-%d", "%m/%d/%Y", "%d-%b-%y", "%d-%B-%y", "%x", "%B-%d-%y", "%m-%d-%Y", ]
                "%m/%d/%y",     # mm/dd/yy 02/21/18
                "%d/%m/%Y",     # dd/mm/yyyy 21/02/2018
                "%d/%m/%y",     # dd/mm/yy 21/02/18
                "%d-%m-%Y",     # dd-mm-yyyy 21-02-2018
                "%d-%m-%y",     # dd-mm-yy  21-02-18
                "%m-%d-%y",     # mm-dd-yy 02-21-18
                "%b %d, %Y",    # Mth d, yyyy Feb 21, 2018
                "%B %d, %Y",    # Month d, yyyy February 21, 2018
                ]
            rand = random.randint(0, len(formats) - 1)
            ret_value = self.aFake.date_between(
                start_date="-30y",
                end_date="today").strftime(
                formats[rand])
        elif field == 'Date2':
            formats = [
                "%Y-%m-%d",
                "%b %d to %b %d, %Y"
                "%b %d to %b %d,%Y"
                "%m/%d/%Y",
                "%d-%b-%y",
                "%d-%B-%y",
                "%x",
                "%B-%d-%y",
                "%m-%d-%Y",
                "%Y %m %d",
                "%d %m %Y",
                "%d %B %y",     # ["%Y-%m-%d", "%m/%d/%Y", "%d-%b-%y", "%d-%B-%y", "%x", "%B-%d-%y", "%m-%d-%Y", ]
                "%m/%d/%y",     # mm/dd/yy 02/21/18
                "%d/%m/%Y",     # dd/mm/yyyy 21/02/2018
                "%d/%m/%y",     # dd/mm/yy 21/02/18
                "%d-%m-%Y",     # dd-mm-yyyy 21-02-2018
                "%d-%m-%y",     # dd-mm-yy  21-02-18
                "%m-%d-%y",     # mm-dd-yy 02-21-18
                "%b %d, %Y",    # Mth d, yyyy Feb 21, 2018
                "%B %d, %Y",    # Month d, yyyy February 21, 2018
                ]
            rand = random.randint(0, len(formats) - 1)
            ret_value = self.aFake.date_between(
                start_date="-30y",
                end_date="today").strftime(
                formats[rand])
        
        elif field == 'AlphaNumeric':
            ret_value = ''.join(random.choices(
                string.ascii_uppercase +string.ascii_lowercase,
                k=random.randint(0, 4)
                    )) +  str(randint(1, 100000)).zfill(randint(1, 6))

        elif field == 'CompanyName':
            ret_value = self.aFake.company()
        elif field == 'Name':
            ret_value = self.aFake.name()
        elif field == 'Phone':
            ret_value = self.aFake.phone_number()
        elif field == 'Sentence':
            ret_value = self.aFake.sentence()
        else:
            error("Unknown field ", field)
            ret_value = None
        return ret_value

    def post_process(self, text):
        text = text.replace('?', ' ')
        return text


if __name__ == '__main__':
    dataset_test()
