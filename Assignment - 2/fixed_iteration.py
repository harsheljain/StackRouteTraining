
def fn1(val):
    x = 1 + (1/val)
    return x

def fn2(val=1):
    x=((val**3) + 2)/7
    return x  

def convg(val):
    
    v1=fn1(val) # Replace fn1 with fn2 for second function.
    v2 = abs(v1-val)
    
    if(v2<=0.0005):
        print("The converged value : ",v1)
        return
    
    else:
        return convg(v1)
         
a = input("enter initial guess : ")
a=float(a)
convg(a)
