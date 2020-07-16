def bubble_sort(array):
    isSorted=False
    counter=0
    while not isSorted:
        isSorted=True
        i=0
        while(i<len(array)-1-counter):
            if(array[i]>array[i+1]):
                array[i],array[i+1]=array[i+1],array[i]
                isSorted=False
            i+=1
        counter+=1
    return array
array=[8,9,2,3,5,1,1,3]
print(bubble_sort(array))
