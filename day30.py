import itertools
numbers = [10,20,30,40,50]
ite = iter(numbers)
try:
    print(next(ite))
    print(ite)
    print(next(ite))
    print(next(ite))
    print(next(ite))
    print(next(ite))
    print(next(ite))

  # This will raise StopIteration since there are no more items in the iterator.
except:
    print("StopIteration raised")