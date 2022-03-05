import csv
with open('testfile.csv', 'r') as read_obj:
csv_reader = csv.reader(read_obj)
list_of_csv = list(csv_reader)
print(list_of_csv)
parts = list(csv.reader ([line]))[0]

from otestfile.csv import Quantity
from testfile.csv import UnitPrice
from testfile.csv import Country

class Country(MRJob):
    def mapper(self, Country, line):
        for Country in line:
           yield (Country)
    def reducer(self, key, amount):
        amount = (Quantity, Price)
        yield (Country, sum(amount))
