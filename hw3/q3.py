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
   def mapper(self, key, line):
      Country = line.split()
      for Country:
         yield ("_" + Country, 1)
         yield "Total_", 1
         country_name = key[0].upper()
         yield country_name +"_", 1
   def reducer(self, key, amount):
      amount = (Quantity * Price)
      yield (key, sum(amount))
if __name__ == '__main__':
    Global.run()
    
  int getPartition(Key key, Value value, int numPart) {
    if key.startsWith("_") { //normal word
       partition = 1 + (key.hash() % (numPart - 1))
    }
    else { //Summary
       partition = 0
    }
    return partition
}
