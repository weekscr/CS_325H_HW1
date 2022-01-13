import numpy
import time

#insert sort list of integers from a file "data.txt"
def insertSort(data):

    for i in range(1,len(data)):
    	#take the value at i and move it backwards in the list until it is greater than the previous value
        ph=data[i]
        j=i-1
        while j>=0 and data[j]>ph:
        	#compare data and swap elements if needed
            data[j+1]=data[j]
            j-=1
        data[j+1]=ph

    return data
                



N = [500,1000,1500,2000,2500,3000,3500,4000,4500,5000]
avgTimes = []
trials = 3

for i in range(len(N)):
    n = N[i]
    avgTime = 0
    
    for j in range(trials):
        data = numpy.random.randint(0,10000,N[i])
        start=time.time()
        sort = insertSort(data)
        end=time.time()
        print("Time to sort ", n ," integers: ", "{:.9f}".format(end-start), " s")
        avgTime+=(end-start)
    avgTimes.append(avgTime/trials)

print(avgTimes)

