# Seek and Destroy (Largest Values)

This program will generate a list of random numbers stored in a list, then compute the largest value in the list. 

After this, it will search for duplicates in the list, remove them, and count how many were present. 

In addition, computation time will be generated. 

Output will consist of:

A) Original list, the number of elements contained, and the average value

B) Processed list, the number of elements contained, and the average value

C) The Max value of the original list

D) Number of duplicates of the max value contained in the original list

E) Computation time of list processing

## Imports
```Python3
from random import randint
import time
from statistics import mean
```

## Number Generator
```Python3
def number_generator(range, amount):
    counter = 0
    list = []
    while counter <= amount:
        number = randint(0, range)
        list.append(number)
        counter += 1
    print("Original List: \nElements contained = " + str(len(list)) + "\n" + str(sorted(list)))
    avgOriginalList = mean(list)
    print("Average of values : " + format(avgOriginalList, ".2f")+"\n")
    return list
```

## Find Largest, Eliminate Duplicates, Calculate Run Time
```Python3
def find_largest(numberlist):
    time_start = time.clock()
    duplicateCount = 0
    max_num = max(numberlist)
    numberlist.remove(max_num)
    duplicateCount += 1
    while max_num in numberlist:
        duplicateCount += 1
        numberlist.remove(max_num)
    latency = (time.clock() - time_start)
    listAvg = mean(numberlist)
    print("Processed List: \nElements contained = " + str(len(numberlist)) + "\n" + str(sorted(numberlist)))
    print("Average of values : " + format(listAvg, ".2f")+"\n")
    return {'Max':max_num, 'Duplicates':duplicateCount ,'Computation Time':format(latency, '.10f')}
```

## Run It
```Python3
if __name__ == "__main__":
    print("Please enter the largest range you would like to consider. Ex. Enter '100' to generate a random list including values from+
                                                                                                                               1-100")
    Range = int(input())
    print("\nPlease enter that number of entries you would like to generate. Ex. Enter '50' to generate 50 entries in your list.")
    Amount = int(input())
    Number = number_generator(Range, Amount)
    Result = find_largest(Number)
    print("Results:")
    for key in reversed(sorted(Result)):
        print("%s: %s" % (key, Result[key]))
```
