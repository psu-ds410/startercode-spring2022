from flights.txt import Source
from flights.txt import Destination

//initializes a dictionary for word count
class Incoming:
def mapper_init(Source):
Source.cache = {}

//Update count
def mapper(Source, Destination, line):
for Destination in line:
    Source.cache[Destination] += 1
    if (cache size > limit):
        for d in cache:
            yield d, cache[d]
        cache.clear()

//Output key value pairs from dictionary
def mapper_final(Source):
if cache is not empty:
    for d in cache:
        yield d, cache[d]

 //output number on incoming flights for each destination
def reducer (Destination, Source, values):
    yield(Destination, sum(values))
