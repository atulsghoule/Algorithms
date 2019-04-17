class MergeSort:
    def __init__(self,array):
        self.array = array
        self.size = len(array)
    def sort(self):
        brick = 0
        while 1<<brick < self.size:
            for start in xrange(0,self.size,(1<<brick)*2):
                self.merge(start,1<<brick)
            brick+=1
    def merge(self,start,block):
        s1,s2 = start,min(self.size,start+block)
        a1,a2 = list(),list()
        for i in xrange(s1,s2):a1.append(self.array[i])
        for i in xrange(s2,min(self.size,s2+block)):a2.append(self.array[i])
        a1.append(float('inf'));a2.append(float('inf'))
        index,index1,index2,sizeK = s1,0,0,s1+len(a1)+len(a2)-2
        while index < sizeK:
            if a1[index1] < a2[index2]:self.array[index] = a1[index1];index1+=1
            else:self.array[index] = a2[index2];index2+=1
            index+=1
    def printArray(self):
        for i in self.array:
            print i,
        print 
array = [1,2,3,6,1,2,4,7,9]
MyArray = MergeSort(array)
MyArray.sort()
MyArray.printArray()