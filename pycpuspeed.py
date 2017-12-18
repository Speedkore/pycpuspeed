import time
import random
import functools
import math
import sys
from datetime import datetime

usage = '''Usage:
Specify the number of minutes to run test as first parameter
Ex. python pycpuspeed 10 '''

def stress():
    N = 10000000

    #test 1
    randoms = [int(random.random()*10) for i in range(N)]
    randoms =  sorted(randoms)
    randoms = map(lambda x: math.sqrt(x), randoms)
    reduce = functools.reduce(lambda x,y: x+y, randoms)


    #test 2
    list_append = []
    for i in range(N):
        list_append.append(i)

    #test 3
    total = 0
    for i in range(N):
        total = i/2*i+total
    




if __name__ == "__main__":
    if len(sys.argv)!=2:
        print(usage)
        exit(1)
    try:
       arg_time = int(sys.argv[1])
    except ValueError:
        print(usage)
        exit(1)
    loop = 0
    times = []
    total_time = 0

    while total_time < arg_time * 60:
        time1 = time.time()
        stress()
        time2 = time.time()
        loop_time = time2 - time1
        total_time += loop_time
        times.append(loop_time)
        print("{0} Loop #{1} Time elapsed: {2:.3f}".format(datetime.now().strftime('%H:%M:%S'), loop, loop_time))
        loop+=1

print("Max: {0:.3f} in loop #{1}".format(max(times), [i for i,x in enumerate(times) if x == max(times)]))
print("Min: {0:.3f} in loop #{1}".format(min(times), [i for i,x in enumerate(times) if x == min(times)]))
print("Total: {0:.3f}".format(sum(times)))
print("Average: {0:.3f}".format((sum(times) / float(len(times)))))
    
