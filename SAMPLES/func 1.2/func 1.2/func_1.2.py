#find lcm and hcf of 2 numbers' input
#loop, counter has the max, changes at each step

def HCF():
    n1=int(input("Enter the first no.:"))
    n2=int(input("Enter the second no.:"))
    c1=0
    p=n1*n2
    for i in range (1,p):
        if (n1%i==0) and (n2/%i==0):
            c1=i
    return (c1,p)
hcf,pr=HCF()
print("The product is", pr)
print("The hcf of the numbers is:",hcf)
lcm=pr//hcf
print("The lcm is:", lcm)

 
    

    

    
    


