from random import randint
import time
from statistics import mean

#Generates a random list of numbers through a user defined range and amount
#Prints the original list set and sorts values
#Computes the mean of the list elements, format prints to second decimal point
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

#Find the largest value in the generated list, checks for duplicate entries, removes them and calculates runtime
#Prints the processed lsit set and sorts values
#Computes the mean of the list elements, format prints to second decimal point
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

#Run program
if __name__ == "__main__":
Number = number_generator(100, 1000)
Result = find_largest(Number)
print("Results:")
for key in reversed(sorted(Result)):
    print("%s: %s" % (key, Result[key]))
