def gcd(m,n):
    fm = []
    for i in range(1,m+1):
        if (m%i)==0:
            fm.append(i)
    fn = []
    for j in range(1,n+1):
        if (n%j)==0:
            fn.append(j) 
    cf = []
    for f in fm:
        if f in fn:
            cf.append(f)
    return(cf[-1])
print(gcd(12,20)) 

#more optimised ones 
def gcd(m,n):                         
    for i in range(1,min(m,n)+1):
        if (m%i)==0 and (n%i) ==0:
            mrcf = i
    return(mrcf) 
print(gcd(10,60))  

#euclid's algorithm
def gcde(m,n):
    #assume m>=n
    if m<n:
        (m,n)=(n,m)
    if (m%n)==0:
        return(n)
    else:
        diff = m-n
        # diff>n? possible!
        return(gcde(max(n,diff),min(n,diff)))
# the more optimised one :
def gcdw(m,n):
    if m<n:
        (m,n) =(n,m) #assume m>=n        
    while(m%n) != 0:
        diff = m-n
        (m,n) = (max(n,diff),min(n,diff))
    return(n)  
