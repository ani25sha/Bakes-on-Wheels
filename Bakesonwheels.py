import mysql.connector as my
import matplotlib.pyplot as plt


con=my.connect(host="localhost", user="root", passwd="2020#Books", database="Bakes_On_Wheels")

cursor=con.cursor(buffered=True)


#1. To display specified records from table department
def display():
    cursor.execute("select * from Billing_Counter")
    data=cursor.fetchall()
    count=cursor.rowcount
    print("No. of rows extracted", count)
    for i in data:
        print()
        for j in i:
            print(j, end="  ")
    print()
    
#2. Display n number of entries

def displayn():
    cursor.execute("select * from Billing_Counter")
    n=int(input("Enter number of starting records that you want to read"))
    info=cursor.fetchmany(n)
    cnt=cursor.rowcount
    if n>cnt:
        print("Too many rows")
    else:
        print("No. of rows extracted", cnt)
        for i in info:
            print()
            for j in i:
                print(j, end="  ")
    print()
         
#3. Insert new values into table DONE
def add():
    t=int(input("How many records do you want to add?"))
    for i in range (0,t):
        b=int(input("Enter invoice number:"))
        d=input("Enter date")
        name=input("Enter customer name:")
        ph=int(input("Enter customer's phone number:"))
        cake=int(input("Enter number of cakes purchased:"))
        biscuit=int(input("Enter number of biscuits purchased:"))
        pastry=int(input("Enter number of pastries purchased:"))
        puff=int(input("Enter number of puffs purchased:"))
        roll=int(input("Enter number of rolls purchased:"))
        c=cake*795+biscuit*85+pastry*110+puff*25+roll*40
        gst=c*0.06
        am=c+gst
        cursor.execute("insert into Billing_Counter values ({}, '{}', '{}', {}, {}, {}, {}, {}, {}, {}, {}, {})".format(b, d, name, ph, cake, biscuit, pastry, puff, roll, c, gst, am))
    con.commit()
    print("Done")

#4. To check the list items being sold in the shop
def items():
    cursor.execute("select Item_Name from Item_Details")
    print("The items available in our shop our:")
    data=cursor.fetchall()
    for i in data:
        for j in i:
            print(j)

#5. Updating phone number of a customer who has visited earlier
def update_phone():
    n=input("Dear Customer, please provide us with your Name: ")
    cursor.execute("select Cust_Name from Billing_Counter")
    v=cursor.fetchall()
    if n in v:        
        p=int(input("Please provide us with your phone number: "))
        cursor.execute("update Billing_Counter set Cust_Phone={} where Cust_Name='{}'".format(p, n))
        con.commit()
        print("Thank You")
    else:
        print("Sorry, we do not have your entry! Don't miss on our cakes, affordable yet delicious!")

#6. Searching for a customer's record on basis of their name
def searching():
    n=input("Dear Customer, please tell us your name: ")
    cursor.execute("select * from Billing_Counter where Cust_Name='{}'".format(n))
    v=cursor.fetchall()
    c=cursor.rowcount
    if c>1:
        print("\nYou have visited us", c, "times!")
    else:
        print("\nYou have visited us", c, "time!")
    if n in v:    
        for i in v:
            print()
            for j in i:
                print(j, end=", ")
    else:
        print()
        print("Don't miss on our cakes, affordable yet tasty!")

#7. To display number of a particular quantity bought
def sum_item():
    c=input("Options:\n1. Cakes\n2. Biscuits\n3. Pastries\n4. Puffs\n5. Rolls\nEnter your choice")

    str="No_Of_"+c
    s="Number of "+c+" bought"
    
    cursor.execute("select sum({}) as '{}' from Billing_Counter".format(str, s))
    i=cursor.fetchall()
    for j in i:
        print("Till date, the number of cakes we've sold are:")
        for k in j:
            print(k, end="")

#8. Graph for items sold
def graph():
    cursor.execute("select sum(No_Of_Cakes), sum(No_Of_Biscuits), sum(No_Of_Pastries), sum(No_Of_Puffs), sum(No_Of_Rolls)  from Billing_Counter")
    data=cursor.fetchall()
    l=[]
    for i in data:
        for j in i:
            l.append(j)
    figure = plt.figure()
    axes = figure.add_subplot(1,1,1)
    axes.bar(['Cakes', 'Biscuits', 'Pastries', 'Puffs', 'Rolls'], l)
    plt.title("Sales")
    plt.show()

#Menu-driven section
l=[1,2,3,4,5,6,7,8,9]
while True:
    print("\nWelcome to Bakes on Wheels!")
    print("\n1. Display complete data\n2. Diplay starting n number of entries\n3. Add new data\n4. View items\n5. Change/Add phone number\n6. How many times have you visited us?\n7. Sales (Stats)\n8. Sales (Graph)\n9. Exit")
    ch=int(input("Enter your choice number"))
    if ch==1:
        display()
    elif ch==2:
        displayn()
    elif ch==3:
        add()
    elif ch==4:
        items()
    elif ch==5:
        update_phone() 
    elif ch==6:
        searching()
    elif ch==7:
        sum_item()
    elif ch==8:
        graph()
    elif ch not in l:
        print(" Oops! Invalid input")
    elif ch==9:
        print("Bye :)")
        break
