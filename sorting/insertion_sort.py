#insertion sort
def insertion_sort(array,size):
    for i in range(1,size):
        key=array[i]
        j=i-1
        while(j>-1 and key<array[j]):
            array[j+1]=array[j]
            j-=1
        array[j+1]=key
array=[10,3,2,5,4,7,6,8,9,1]
insertion_sort(array,10)
print(array)
