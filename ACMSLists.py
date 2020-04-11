#!/usr/bin/env python
# coding: utf-8

# In[3]:


## Find maximum average subarray of k length

def solve(List, k) -> float:
    
    if len(List) == 0 or len(List) < k:
        return 0
    
    i = 0
    j = k - 1
    ans = 0
    sum = 0
    
    while i <= j:
        sum += List[i]
        i = i + 1
    ans = sum / k
    
    i = 1
    j = k
    
    while j < len(List):
        sum -= List[i]
        sum += List[j]
        ans = max(ans, sum / 4)
        i = i + 1
        j = j + 1
        
    return ans

if __name__ == "__main__":
    
    List = []
    n = int(input("Enter size "))
    k = int(input("Enter k"))
    i = 0;
    
    while i < n:
        x = int(input("Enter element "))
        List.append(x)
        i = i + 1
        
    ans = solve(List, k)
    print(ans)


# In[ ]:




