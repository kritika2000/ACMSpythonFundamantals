#!/usr/bin/env python
# coding: utf-8

# In[8]:


## find the median of two sorted arrays

def findMedian(Tuple1, Tuple2) -> float:
    
    l1 = len(Tuple1)
    l2 = len(Tuple2)
    l = l1 + l2
    
    List = []
    
    if l == 0:
        return 0
    
    i = 0
    j = 0
    
    while i < l1 and j < l2:
        
        if Tuple1[i] < Tuple2[j]:
            List.append(Tuple1[i])
            i = i + 1
        else:
            List.append(Tuple2[j])
            j = j + 1
            
    while i < l1:
        List.append(Tuple1[i])
        i = i + 1
            
    while j < l2:
        List.append(Tuple2[j])
        j = j + 1
        
    x = int(l / 2)
    
    if(l % 2 == 0):
        return (List[x - 1] + List[x]) / 2
    else:
        return List[x]
    
if __name__ == "__main__":
    
    Tuple1 = (1, 6 ,9 ,12 ,18 ,19)
    Tuple2 = (3, 5, 7, 11, 17, 20, 25)
    
    ans = findMedian(Tuple1, Tuple2)
    print(ans)


# In[ ]:




