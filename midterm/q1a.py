from flights.txt import Source
from flights.txt import Destination

//initializes a dictionary for word count
class Outgoing:
def mapper_init(Source)
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
def mapper_final(Source)
if cache is not empty:
    for d in cache:
        yeild d, cache[d]
 
//output number of outgoing flights for each source airport
def reducer (Source, Destination, values)
    yield(Source, sum(values))
