#!/usr/bin/env python
# coding: utf-8

# In[24]:


## Find the longest common prefix among a list of strings

def longestCommonPrefix(List) -> str:
    
        if len(List) == 0:
            return ""
        if len(List) == 1:
            return List[0]
        i = 0
        minlen = len(List[0])
        j = 0
        prefix = ""
        while i < len(List):
            minlen = min(minlen, len(List[i]))
            i = i + 1
        k = 1
        while j < minlen:
            c = List[0][j]
            k = 1
            while k < len(List):
                if List[k][j] != c:
                    return prefix
                k = k + 1
            prefix = prefix + c
            j = j + 1
        return prefix    

if __name__ == "__main__":
    
    List = []
    n = int(input("Enter size of the list"))
    i = 0
    while i < n:
        s = str(input("Enter a string"))
        List.append(s)
        i = i + 1
    pr = longestCommonPrefix(List)
    print(pr)
        
    


# In[ ]:





# In[ ]:




