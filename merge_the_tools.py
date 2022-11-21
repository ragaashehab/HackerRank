def merge_the_tools(string, k):
    # your code goes here

    lstkele= []
    lstuniquele= []
    
    for i in range(0,len(string),k):
        lstkele.append(string[i : i+k])
            
    for se in lstkele:
        uniquele= ""
        for e in se:
            if e not in uniquele:
                uniquele= uniquele + e
        print(uniquele)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)