from flights.txt import Source
from flights.txt import Destination

//initializes a dictionary for word count
class Incoming:
def mapper_init(Destination):
Destination.cache = {}

//Update count
def mapper(Destination, Source, line):
for Source in line:
    Destination.cache[Source] += 1
    if (cache size > limit):
        for s in cache:
            yield s, cache[s]
        cache.clear()

//Output key value pairs from dictionary
def mapper_final(Destination):
if cache is not empty:
    for s in cache:
        yield s, cache[s]

 //output number on incoming flights for each destination
def reducer (Destination, Source, values):
    yield(Destination, sum(values))
