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
                



f = open('data.txt','r').readlines()

for i in range(len(f)):
    d = [int(j) for j in f[i].split()]
    n = d[0]
    data = d[1:len(d)]
    sort = mergeSort(data)
    print(sort)



