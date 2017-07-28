from random import randint
import time

#Generates a random list of numbers through a user defined range and amount
def number_generator(range, amount):
    counter = 0
    list = []
    while counter <= amount:
        number = randint(0, range)
        list.append(number)
        counter += 1
    return list

#Find the largest value in the generated list, checks for duplicate entries, removes them and calculates runtime 
def find_largest(numberlist):
    time_start = time.clock()
    duplicateCount = 0
    max_num = max(numberlist)
    numberlist.remove(max_num)
    while max_num in numberlist:
       duplicateCount += 1
       numberlist.remove(max_num)
    latency = (time.clock() - time_start)
    return {'Max':max_num, 'Duplicates':duplicateCount ,'Computation Time':format(latency, '.10f')}

#Run program
Number = number_generator(100, 200)
Result = find_largest(Number)
for key in reversed(sorted(Result)):
    print("%s: %s" % (key, Result[key]))
