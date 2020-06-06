def sor(v,n,s):
    #print("In Sorted")
    k=1;c=1;i=0
    while(i<n-1 and k<n and k!=i):
        if((v[k]-v[i]) >= s):
            c+=1
            i=k
            k+=1
        else:  k+=1    
    print(c)

def unsor(v,n,s):
    #print("In Unsorted")
    c=1;
    t=list()
    t.append(v[0])
    #print("Before For Loop:"); print(*t)
    for i in range(1,n):
        y=min(t) 
        #print("the min ele currently:" + str(y))
        if(v[i]- y < s ):
            t.append(v[i])                             #t[j]=v[i]
            #print("if condition is satisfied:"); print(*t)
        else:
            #print("if condition is not satisfied:"); print(*t)
            c+=1
            t=list()
            t.append(v[i])
    print(c)

def main():
    tc=int(input())
    while(tc>0):
        tc-=1
        n,s=[int(x) for x in input().split()]           #cin>>n>>s   n, s = map(int, input().split())            
        v=list()
        for i in range(0, n): 
            x=int(input()) 
            v.append(x)                                 #adding the element 
        #is_sorted = lambda a: np.all(v[:-1] <= v[1:])
        if(v==sorted(v)):   
            sor(v,n,s)                                  #if the given data is sorted
        else:
            unsor(v,n,s)                                #if the given data is sorted
        #print("The List is:"); print(*v)

if __name__=='__main__':
    main()