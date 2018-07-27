prime = 101
# HashFunction 
# string = 'abc'
# ord('a')*pow(prime,0) + ord('b')*pow(prime,1) + ord('c')*pow(prime,2)
def myHash(string):
    ans = 0
    for i in xrange(len(string)):
        ans+= ord(string[i])*(pow(prime,i))
    return ans
# Rabin-Karp string matching algorithm
# param(String,Substring)
# return list of index
def rabinKarp(string,subString):
    sizeString,sizeSubstring = len(string),len(subString)
    index = []
    if sizeSubstring > sizeString:
        return index
    hashSubstring = myHash(subString)
    tempHash = myHash(string[0:sizeSubstring])
    for i in xrange(sizeString-sizeSubstring + 1):
        if tempHash==hashSubstring and subString == string[i:sizeSubstring+i]:
            index.append(i)
        # calculating new hash
        tempHash-=ord(string[i])
        tempHash/=prime
        tempHash+= ord(string[(i+sizeSubstring)%sizeString])*pow(prime,sizeSubstring-1)
    return index
# driver code
string = 'abcabcabc'
subString = 'abc'
print rabinKarp(string,subString)

