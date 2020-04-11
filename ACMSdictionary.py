#!/usr/bin/env python
# coding: utf-8

# In[8]:


## find unique triplets which sum to 0

def pairSum(List, elem, ansList, s, e):
    
    Dictionary = {}
    
    while s < e:
        
        if List[s] + List[e] + elem == 0:
            
            l = []
            l.append(elem)
            l.append(List[s])
            l.append(List[e])
            
            if not(List[s] in Dictionary and Dictionary[List[s]] == List[e]):
                ansList.append(l)
                Dictionary[List[s]] = List[e]
                
            e = e - 1
            s = s + 1
            
        elif List[s] + List[e] > elem:
            s = s + 1
            
        else:
            e = e - 1

def findTriplets(List):
    
    List.sort()
    ansList = []
    i = 0
    j = len(List)
    
    while i < j - 2:
        pairSum(List, List[i], ansList, i + 1, j - 1)
        i = i + 1
        
    for i in ansList:
        print(i)

if __name__ == "__main__":
    
    List = [-1, 0, 1, 2, -1, -4]
    findTriplets(List)


# In[ ]:




