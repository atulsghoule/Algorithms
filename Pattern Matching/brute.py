# Pattern matching
# param(string,subString)
# return list of index
def brute(string,subString):
    index = list()
    sizeString,sizeSubstring =len(string),len(subString)
    for i in xrange(sizeString-sizeSubstring+1):
        if subString == string[i:i+sizeSubstring]:
            index.append(i)
    return index
# driver code
string = "abcabcabc"
subString = 'abc'
print brute(string,subString)
