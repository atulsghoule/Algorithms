##selection sort
def selection_sort(array,size):
    for i in range(size):
        index=i
        for j in range(i+1,size):
            if array[j]<array[index]:
                index=j
        array[i],array[index]=array[index],array[i]
array=[2,10,4,3,5,6,8,7,9,1]
selection_sort(array,10)
print(array)
