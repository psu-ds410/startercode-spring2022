from fractions import Fraction
import csv
with open('testfile.csv', 'r') as read_obj:
csv_reader = csv.reader(read_obj)
list_of_csv = list(csv_reader)
print(list_of_csv)
parts = list(csv.reader ([line]))[0]

from testfile.csv import Quantity
from testfile.csv import UnitPrice
from testfile.csv import Country

from mrjob.job import MRJob
class Global(MRJob):
   def mapper(self, Country, line):
      Country = line.split()
      for Country:
         yield ("_" + Country, 1)
         yield "Total_", 1
         country_name = key[0].upper()
         yield country_name +"_", 1
   def reducer(self, Country, amount):
      amount = (Quantity * Price)
      yield (Country, sum(amount))
if __name__ == '__main__':
    Global.run()

  int getPartition(Key Country, Value amount, int total) {
    if key.startsWith("_") { //normal word
       partition = Country + Fraction(amount / total)
    }
    else { //Summary
       partition = 0
    }
    return partition
}
