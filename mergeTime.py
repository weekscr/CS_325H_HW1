import numpy
import time

#Merge sort list of integers from a file "data.txt"
def mergeSort(data):
    #check trivial case
    if len(data)>1:
        m = len(data)//2 #split list in 'half'
        lh = data[:m]
        rh = data[m:]
        mergeSort(lh) #recursively sort the two halves
        mergeSort(rh)

        #merge the two halves
        a=0
        b=0
        i=0
        
        while a<len(lh) and b<len(rh):
            #compare lists and increment values
            if lh[a] < rh[b]: 
                data[i]=lh[a]
                a+=1
            else:
                data[i]=rh[b]
                
                b+=1
            i+=1
        #account for any remaining data
        if len(lh)>a:
            while a<len(lh):
                data[i]=lh[a]
                a+=1
                i+=1

        if len(rh)>b:
            while b<len(rh):
                data[i]=rh[b]
                b+=1
                i+=1


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
        sort = mergeSort(data)
        end=time.time()
        print("Time to sort ", n ," integers: ", "{:.9f}".format(end-start), " s")
        avgTime+=(end-start)
    avgTimes.append(avgTime/trials)

print(avgTimes)
