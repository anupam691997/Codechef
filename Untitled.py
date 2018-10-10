
# coding: utf-8

# In[13]:


T=int(input())


while T>0:
    N=int(input())
    N=N-1
    
    bits=0
    nibble=0
    byte=0
    
    x=int(N/26)
    
   # print(x," ")
    
    bits=bits+pow(2,x)
    
   # print(bits," ")
    
    N=N%26
    
    #print(N," ")
    
    if N<2:
        print(bits," ",nibble," ",byte,"\n")
        T=T-1
        continue
    else:
        N=N-2
        nibble=bits
        bits=0
    
    if N<8:
        print(bits," ",nibble," ",byte,"\n")
        T=T-1
        continue
    else:
        N=N-8
        byte=nibble
        nibble=0
        print(bits," ",nibble," ",byte,"\n")
    
    T=T-1
        
    
    
    
    
    
    
    

