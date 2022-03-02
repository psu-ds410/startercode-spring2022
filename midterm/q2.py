from flights.txt import Source
from flights.txt import Destination
from flights.txt import Airport

//initializes a dictionary for word count
class Flights:
def mapper_init(Destination):
Destination.cache = {}
Source.cache = {}

//Update count
def mapper(Destination, Source, Airport):
for Source in airport:
    Destination.cache[Source] += 1
for Destination in airport:
    Source.cache[Destination] += 1
    if (cache size > limit):
        for s in cache:
            yield s, cache[s]
        cache.clear()
    else:
        for d in cache:
            yield d, cache[d]
            cache.clear

//Output key value pairs from dictionary
def mapper_final(Destination):
if cache is not empty:
    for s in cache:
        yield s, cache[s]
    for d in cache:
        yield d


 //output number on incoming flights for each destination
def reducer (Destination, Source, values):
    yield(Destination, sum(values))

//int getPartition(key Airport, value Source, int Destination){
//if
//}
