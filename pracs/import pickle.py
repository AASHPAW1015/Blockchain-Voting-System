import pickle 
#write function writesStudent() to write the records of students (admno, name, fee) in a binary file name "stud.dat", and write function display() those records froma binary which fee is less than 1500.



def writesStudent(fo):
    admno=input("Enter the admission number of student:")
    name=input("Enter the name of the student:")
    fee=int(input("Enter the fees:"))
    d=[admno,name,fee]
    pickle.dump(d,fo)
def display(fo):
    fo.seek(0)
    while True:
        try:
            d = pickle.load(fo)  
            if d[2] < 1500:
                print(d)  
        except EOFError:
            break

fo=open("stud.dat","wb+")
ch="y"
while ch=="Y" or ch=='y':
    print("""Choose any one option from below:
          1)Write Student Data
          2)Display record of the student with fees less than 1500 """)
    c=int(input(">"))
    if (c==1):
        writesStudent(fo)
    elif (c==2):
        display(fo)
    else:
        print("Invalid Choice")
    print("Do you want to continue? (y or n)")
    ch=input(">")
fo.close()