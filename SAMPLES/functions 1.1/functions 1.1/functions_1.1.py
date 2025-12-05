#to check if no. is a prime no.
def prime():
    c=0
    n1=int(input("Enter an integer:"))
    for i in range (1,n1+1):
        if n1%i==0:
            c+=1
    return c
r=prime()
if r==2:
    print("The number given is a prime number!")
else:
    print("nope.")
    
    

        
    
  
