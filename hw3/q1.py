import csv
with open('testfile.csv', 'r') as read_obj:
csv_reader = csv.reader(read_obj)
list_of_csv = list(csv_reader)
print(list_of_csv)
parts = list(csv.reader ([line]))[0]

from testfile.csv import Quantity
from testfile.csv import UnitPrice

class Country(MRJob):
    def mapper(self, Country, line):
        for Country in line:
           yield (Country)
    def reducer(self, key, amount):
        amount = (Quantity * Price)
        yield (Country, sum(amount))
