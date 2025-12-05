import csv
firstinput=str(input("Enter the first name you wish to find:"))
with open("names_csv.csv", "r") as data:
    read=csv.reader(data)
    for i in read:
        if i['first_name']==firstinput:
            print("The name",firstinput,"is there")
        else:
            print("Not there")
    
