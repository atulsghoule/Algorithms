# Longest prefix == Longest suffix
# param(string)
# returns a array will information on index of prefix
def prefixArray(string):
    size,index,i=len(string),0,1
    array = [0]*size
    while i < size:
        if string[i] == string[index]:
            array[i] = index+1
            index+=1;i+=1
        else:
            if index!=0:
                index = array[index-1]
            else:
                array[i] = 0
                i+=1
    return array
# Kmap algorithm of patter string
# param(string,subString)
# return array of index
def kmap(string,subString):
    sizeString,sizeSubstring = len(string),len(subString)
    array = prefixArray(subString)
    i,j = 0,0
    index = list()
    while i<sizeString: 
        if string[i]==subString[j]:
            i+=1;j+=1
        else:
            if j!=0:
                j = array[j-1]
            else:
                i+=1
        if j==sizeSubstring:
            index.append(i-sizeSubstring)
            j=0
    return index
# driver code
string = 'abcabcabc'
subString = 'abc'
print kmap(string,subString)
