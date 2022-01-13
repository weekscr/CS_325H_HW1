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
                



f = open('data.txt','r').readlines()

for i in range(len(f)):
    d = [int(j) for j in f[i].split()]
    n = d[0]
    data = d[1:len(d)]
    sort = insertSort(data)
    print(sort)



