# equilibrium index problem
  
def equilibrium(a): 

    sumt = sum(a) # total sum
    suml = 0   # sum left
    x=[]
    for i, num in enumerate(a): 
        sumt -= num 
        if suml is sumt: 
            x.append(i) 
        suml += num  

    #print(x)
    if len(x):
        return min(x)
    else:
        return -1
      
if __name__ == '__main__':
    a = [-7, 1, 5, 2, -4, 3, 0] 
    print ('Min equilibrium index is :', equilibrium(a)) 
#equilibrium(arr)