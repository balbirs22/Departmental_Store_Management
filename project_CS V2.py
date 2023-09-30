import mysql.connector as m
from prettytable import PrettyTable
con=m.connect(host="localhost",user="root",password="12345")
cur=con.cursor()
cur.execute("create database if not exists Departmental_Store")
cur.execute("use Departmental_Store")
a='''create table if not exists customer(
     cust_name varchar(50) not null,
     cust_phone varchar(10) not null,
     cust_email varchar(100) not null,
     gender varchar(10))'''
cur.execute(a)
a='''create table if not exists members(
     cust_name varchar(50) not null,
     cust_phone varchar(10) not null,
     cust_email varchar(100) not null,
     gender varchar(10))'''
cur.execute(a)
a='''create table if not exists grocery(
     P_ID integer primary key,
     P_Name varchar(100) not null,
     Qty integer check(Qty>=0),
     Price integer check(price>0),
     Brand varchar(50))'''
cur.execute(a)
a='''create table if not exists toys(
     P_ID integer primary key,
     P_Name varchar(100) not null,
     Qty integer check(Qty>=0),
     Price integer check(price>0),
     Brand varchar(50))'''
cur.execute(a)
a='''create table if not exists Personal_Care(
     P_ID integer primary key,
     P_Name varchar(100) not null,
     Qty integer check(Qty>=0),
     Price integer check(price>0),
     Brand varchar(50))'''
cur.execute(a)
a='''create table if not exists Bill(
     P_ID integer,
     P_Name varchar(50),
     Qty integer,
     Price integer,
     Cost integer)'''
cur.execute(a)
def all_cust():
    print("Welcome to Balbir's Departmental store")
    cust_name=input("Please Enter your Name:")
    while True:
        cust_phone=input("Please Enter your Mobile Number:")
        if len(cust_phone)!=10:
            print("Incorrect Mobile number")
            print("Please Enter again")
        else:
            break
    while True:
        cust_email=input("Please Enter your google email adress:")
        if cust_email.endswith('@gmail.com'):
            break
        else:
            print("Incorrect Email id")
            print("Enter Again")
    gender=input("Enter your gender:")
    data=(cust_name,cust_phone,cust_email,gender)
    a='insert into customer values(%s,%s,%s,%s)'
    cur.execute(a,data)
    con.commit()
    print("customer account created successfully")
    ch=input("Enter space to return to main menu")
    if ch==" ":
        return
def member_cust():
     print("Welcome to Balbir's Departmental store")
     cust_name=input("Please Enter your Name:")
     while True:
         cust_phone=input("Please Enter your Mobile Number:")
         if len(cust_phone)!=10:
             print("Incorrect Mobile number")
             print("Please Enter again")
         else:
             break
     while True:
         cust_email=input("Please Enter your google email adress:")
         if cust_email.endswith('@gmail.com'):
             break
         else:
             print("Incorrect Email id")
             print("Enter Again")
     gender=input("Enter your gender:")
     data=(cust_name,cust_phone,cust_email,gender)
     a='insert into customer values(%s,%s,%s,%s)'
     cur.execute(a,data)
     con.commit()
     print("Member account created successfully")
     ch=input("Enter space to return to main menu")
     if ch==" ":
         return  
def items():
    a2='''
    Categories are:
    1.grocery
    2.personal_care
    3.toys
    4.exit'''
    while True:
        print(a2)
        ch=int(input("Enter choice number"))
        if ch==1:
            t=PrettyTable(['P_ID','P_Name','Brand','Price'])
            a='select P_ID,P_Name,Brand,Price from grocery;'
            cur.execute(a)
            data=cur.fetchall()
            for e,f,g,h in data:
                t.add_row([e,f,g,h])
            print(t)
        elif ch==2:
            t=PrettyTable(['P_ID','P_Name','Brand','Price'])
            a='select P_ID,P_Name,Brand,Price from personal_care;'
            cur.execute(a)
            data=cur.fetchall()
            for e,f,g,h in data:
                t.add_row([e,f,g,h])
            print(t)
        elif ch==3:
            t=PrettyTable(['P_ID','P_Name','Brand','Price'])
            a='select P_ID,P_Name,Brand,Price from personal_care;'
            cur.execute(a)
            data=cur.fetchall()
            for e,f,g,h in data:
                t.add_row([e,f,g,h])
            print(t)      
        elif ch==4:
            print("Thank you")
            break
        else:
            print("Incorrect choice")
            print("Enter choice again")
def Order():
    CH=input("Enter membership status(y/n):")
    if CH=='y'or CH=='Y':
        m=True
    else:
        m=False
    a='''
    1.grocery
    2.personal_care
    3.toys
    4.show bill
    5.Exit'''
    while True:
        print(a)
        ch=int(input("Enter choice number:"))
        if ch==1:
            P_ID=int(input("Enter product ID:"))
            p=(P_ID,)
            P_Name=input("Enter product name:")
            st="select price from grocery where P_ID=%s"
            cur.execute(st,p)
            d=cur.fetchone()
            Price=d[0]
            if cur.rowcount==0:
                print("Incorrect Product selected")
                break 
            Qty=int(input("Enter quantity:"))
            dd=(Qty,P_ID)
            st2='''update grocery
                 set qty=qty-%s where P_ID=%s'''
            cur.execute(st2,dd)
            data=(P_ID,P_Name,Qty,Price,Price*Qty)
            st4="insert into bill values(%s,%s,%s,%s,%s)"
            cur.execute(st4,data)
            con.commit()
            ch=input("Press spacebar to continue")
            if ch==' ':
                continue
            else:
                print("Incorrect choice")
                break
        elif ch==2:
            P_ID=int(input("Enter product ID:"))
            p=(P_ID,)
            P_Name=input("Enter product name:")
            st="select price from personal_care where P_ID=%s"
            cur.execute(st,p)
            d=cur.fetchone()
            Price=d[0]
            if cur.rowcount==0:
                print("Incorrect Product selected")
                break 
            Qty=int(input("Enter quantity:"))
            dd=(Qty,P_ID)
            st2='''update personal_care
                 set qty=qty-%s where P_ID=%s'''
            cur.execute(st2,dd)
            data=(P_ID,P_Name,QTY,Price,Price*QTY)
            cur.execute("insert into bill values(%s,%s,%s,%s,%s)",data)
            con.commit()
            ch=input("Press spacebar to continue")
            if ch==' ':
                continue
            else:
                print("Incorrect choice")
                break
        elif ch==3:
            P_ID=int(input("Enter product ID:"))
            p=(P_ID,)
            P_Name=input("Enter product name:")
            st="select * from toys where P_ID=%s"
            cur.execute(st,p)
            d=cur.fetchone()
            Price=d[0]
            if cur.rowcount==0:
                print("Incorrect Product selected")
                break
            Qty=int(input("Enter quantity:"))
            dd=(Qty,P_ID)
            st2='''update toys
                 set qty=qty-%s where P_ID=%s'''
            cur.execute(st2,dd)
            data=(P_ID,P_Name,QTY,Price,Price*QTY)
            cur.execute("insert into bill values(%s,%s,%s,%s,%s)",data)
            con.commit()
            ch=input("Press spacebar to continue")
            if ch==' ':
                continue
            else:
                print("Incorrect choice")
                break
        elif ch==4:
            if m==True:
                t=PrettyTable(['P_ID','P_Name','Qty','Price','Cost'])
                cur.execute("Select * from bill")
                data=cur.fetchall()
                for e,f,g,h,i in data:
                    t.add_row([e,f,g,h,i])
                print(t)
                cur.execute("select sum(cost) from bill")
                data=cur.fetchone()
                TotalCost=data[0]
                a=int(TotalCost)
                print("Original Cost:",a)
                print("Membership Price",a-0.1*a)
                stt="delete from bill"
                cur.execute(stt)
                con.commit()
                break
            else:
                cur.execute("Select * from bill")
                data=cur.fetchall()
                for i in data:
                    print(*i,sep="\t")
                cur.execute("select sum(cost) from bill")
                data=cur.fetchone()
                TotalCost=data[0]
                a=int(TotalCost)
                print("Original Cost:",a)
                stt="delete from bill"
                cur.execute(stt)
                con.commit()
                break
        elif ch==5:
            print("Thank You")
            break
def additems():
    print("Welcome Manager")
    a1='''
    1.grocery items
    2.toys
    3.personal_care items
    4.Exit'''
    while True:
        print(a1)
        ch=int(input("enter your choice"))
        if ch==1:
            P_ID=int(input("Enter Product ID:"))
            P_Name=input("Enter Product Name:")
            Qty=int(input("Enter Quantity:"))
            Price=eval(input("Enter Price:"))
            Brand=input("Enter Brand name:")
            data=(P_ID,P_Name,Qty,Price,Brand)
            a="insert into grocery values(%s,%s,%s,%s,%s)"
            cur.execute(a,data)
            con.commit()
            print("Data inserted successfully")
        elif ch==2:
            P_ID=int(input("Enter Product ID:"))
            P_Name=input("Enter Product Name:")
            Qty=int(input("Enter Quantity:"))
            Price=eval(input("Enter Price:"))
            Brand=input("Enter Brand name:")
            data=(P_ID,P_Name,Qty,Price,Brand)
            a='insert into toys values(%s,%s,%s,%s,%s)'
            cur.execute(a,data)
            con.commit()
            print("Data inserted successfully")
        elif ch==3:
            P_ID=int(input("Enter Product ID:"))
            P_Name=input("Enter Product Name:")
            Qty=int(input("Enter Quantity:"))
            Price=eval(input("Enter Price:"))
            Brand=input("Enter Brand name:")
            data=(P_ID,P_Name,Qty,Price,Brand)
            a='insert into personal_care values(%s,%s,%s,%s,%s)'
            cur.execute(a,data)
            con.commit()
            print("Data inserted successfully")
        elif ch==4:
            break
        else:
            print("Incorrect choice")
            print("Enter Again")
def search_item_manager():
    print("Welcome manager")
    a1='''
    1.grocery 
    2.toys
    3.personal_care 
    4.Exit'''
    while True:
        print(a1)
        ch=int(input("Enter category number to begin search"))
        if ch==1:
            t=PrettyTable(['P_ID','P_Name','Qty','Price','Brand'])
            P_ID=int(input('Enter product id to begin search'))
            p=(P_ID,)
            cur.execute("select * from grocery where P_ID=%s",p)
            r=cur.rowcount
            if r==0:
                data=cur.fetchall()
                for e,f,g,h,i in data:
                    t.add_row([e,f,g,h,i])
                print(t)
                print("search successful")
            else:
                print("No such product exists")
        elif ch==2:
            t=PrettyTable(['P_ID','P_Name','Qty','Price','Brand']) 
            P_ID=int(input('Enter product id to begin search'))
            p=(P_ID,)
            cur.execute("select * from toys where P_ID=%s",p)
            r=cur.rowcount
            if r==0:
                data=cur.fetchall()
                for e,f,g,h,i in data:
                    t.add_row([e,f,g,h,i])
                print(t) 
                print("search successful")
            else:
                print("No such product exists")
        elif ch==3:
            t=PrettyTable(['P_ID','P_Name','Qty','Price','Brand'])
            P_ID=int(input('Enter product id to begin search'))
            p=(P_ID,)
            cur.execute("select * from grocery where P_ID=%s",p)
            r=cur.rowcount
            if r==0:
                data=cur.fetchall()
                for e,f,g,h,i in data:
                    t.add_row([e,f,g,h,i])
                print(t) 
                print("search successful")  
            else:
                print("No such product exists")
        elif ch==4:
            print("Thank You")
            break
        else:
            print("Incorrect Choice")
            print("Enter Again")
def search_item_customer():
    print("Welcome")
    a1='''
    1.grocery 
    2.toys
    3.personal_care 
    4.Exit'''
    while True:
        print(a1)
        ch=int(input("Enter category number to begin search"))
        if ch==1:
            t=PrettyTable(['P_ID','P_Name','Price'])
            P_ID=int(input("Enter Product ID"))
            p=(P_ID,)
            cur.execute("select P_ID,P_Name,Price from grocery where P_ID=%s",p)
            if cur.rowcount==0:
                d=cur.fetchall()
                for e,f,g in d:
                    t.add_row([e,f,g])
                print(t)
                print("Search Successful")
            else:
                print("No such product exists")
        elif ch==2:
            t=PrettyTable(['P_ID','P_Name','Price'])
            P_ID=int(input("Enter Product ID"))
            p=(P_ID,)
            cur.execute("selectP_ID,P_Name,Price from toys where P_ID=%s",p)
            if cur.rowcount==0:
                d=cur.fetchall()
                for e,f,g in d:
                    t.add_row([e,f,g])
                print(t)
                print("Search Successful")
            else:
                print("No such product exists")
        elif ch==3:
            t=PrettyTable(['P_ID','P_Name','Price'])
            P_ID=int(input("Enter Product ID"))
            p=(P_ID,)
            cur.execute("select P_ID,P_Name,Price from grocery where P_ID=%s",p)
            if cur.rowcount==0:
                d=cur.fetchall()
                for e,f,g in d:
                    t.add_row([e,f,g])
                print(t)
                print("search successful")
            else:
                print("No such product exists")
        elif ch==4:
            print("Thank You")
            break
        else:
            print("Incorrect Choice")
            print("Enter Again")
def remove_item():
    print("Welcome Manager")
    a='''
    1.grocery 
    2.toys
    3.personal_care 
    4.Exit'''
    while True:
        print(a)
        ch=int(input("Enter category number to begin removing items"))
        if ch==1:
            P_ID=int(input("Enter Product ID"))
            p=(P_ID,)
            cur.execute("delete from grocery where P_ID=%s",p)
            con.commit()
            if cur.rowcount!=0:
                print("product deleted successfully")
            else:
                print("No such product exists")
        elif ch==2:
            P_ID=int(input("Enter Product ID"))
            p=(P_ID,)
            cur.execute("delete from toys where P_ID=%s",p)
            con.commit()
            if cur.rowcount!=0:
                print("product deleted successfully")
            else:
                print("No such product exists")
        elif ch==3:
            P_ID=int(input("Enter Product ID"))
            p=(P_ID,)
            cur.execute("delete from personal_care where P_ID=%s",p)
            con.commit()
            if cur.rowcount!=0:
                print("product deleted successfully")
            else:
                print("No such product exists")
        elif ch==4:
            print("Thank You")
            break
        else:
            print("Incorrect Choice")
            print("Enter Again")
def productQty_0():
    print("welcome manager")
    a='''
    1.grocery 
    2.toys
    3.personal_care 
    4.Exit'''
    while True:
        print(a)
        ch=int(input("Enter category number to begin search"))
        if ch==1:
            t=PrettyTable(['P_ID','P_Name','Qty','Price','Brand'])
            cur.execute("select * from grocery where qty=0")
            if cur.rowcount!=0:
                data=cur.fetchall()
                for e,f,g,h,i in data:
                    t.add_row([e,f,g,h,i])
                print(t)
            else:
                print("No such record exists")
        elif ch==2:
            t=PrettyTable(['P_ID','P_Name','Qty','Price','Brand'])
            cur.execute("select * from toys where qty=0")
            if cur.rowcount!=0:
                data=cur.fetchall()
                data=cur.fetchall()
                for e,f,g,h,i in data:
                    t.add_row([e,f,g,h,i])
                print(t)  
            else:
                print("No such record exists")
        elif ch==3:
            t=PrettyTable(['P_ID','P_Name','Qty','Price','Brand'])
            cur.execute("select * from personal_care where qty=0")
            if cur.rowcount!=0:
                data=cur.fetchall()
                for e,f,g,h,i in data:
                    t.add_row([e,f,g,h,i])
                print(t)
            else:
                print("No such record exists")
        elif ch==4:
            print("Thank you")
            break
        else:
            print("Incorrect choice")
            print("Enter Again")         
def Brand():
    print("welcome manager")
    a='''
    1.grocery 
    2.toys
    3.personal_care 
    4.Exit'''
    while True:
        print(a)
        ch=int(input("Enter category number to begin search"))
        if ch==1:
            t=PrettyTable(['P_ID','P_Name',"Qty",'Price','Brand'])
            brand=input("Enter Brand name:")
            b=(brand,)
            cur.execute("select * from grocery where brand=%s",b)
            if cur.rowcount==0:
                data=cur.fetchall()
                for e,f,g,h,i in data:
                    t.add_row([e,f,g,h,i])
                print(t)
            else:
                print("No Such product exists")
        elif ch==2:
            t=PrettyTable(['P_ID','P_Name',"Qty",'Price','Brand'])
            brand=input("Enter Brand name:")
            b=(brand,)
            cur.execute("select * from toys where brand=%s",b)
            if cur.rowcount==0:
                data=cur.fetchall()
                for e,f,g,h,i in data:
                    t.add_row([e,f,g,h,i])
                print(t)
            else:
                print("No Such product exists")
        elif ch==3:
            t=PrettyTable(['P_ID','P_Name',"Qty",'Price','Brand'])
            brand=input("Enter Brand name:")
            b=(brand,)
            cur.execute("select * from personal_care where brand=%s",b)
            if cur.rowcount==0:
                data=cur.fetchall()
                for e,f,g,h,i in data:
                    t.add_row([e,f,g,h,i])
                print(t)
            else:
                print("No Such product exists")
        elif ch==4:
            print("Thank you")
            break
        else:
            print("Incorrect choice")
            print("Enter Again")
def cust():
    print("Welcome Manager")
    while True:
        ch=input("Enter gender(M/F)")
        if len(ch)==1:
            break
        else:
            print("Enter only 1 character")
    c=(ch,)
    if ch in "Mm":
        t=PrettyTable(['Cust_Name','Cust_Phone','Cust_email','Gender'])
        st="select * from customer where gender='m'"
        cur.execute(st)
        data=cur.fetchall()
        for e,f,g,h in data:
            t.add_row([e,f,g,h])
        print(t)
    elif ch in "Ff":
        t=PrettyTable(['Cust_Name','Cust_Phone','Cust_email','Gender'])
        st="select * from customer where gender='f'"
        cur.execute(st)
        data=cur.fetchall()
        for e,f,g,h in data:
            t.add_row([e,f,g,h])
        print(t)
    else:
        print("Incorrect choice")
        print("Enter Again")
def mem():
    print("Welcome Manager")
    while True:
        ch=input("Enter gender(M/F)")
        if len(ch)==1:
            break
        else:
            print("Enter only 1 character")
    c=(ch,)
    if ch in "Mm":
        t=PrettyTable(['Cust_Name','Cust_Phone','Cust_email','Gender'])
        st="select * from customer where gender='m'"
        cur.execute(st)
        data=cur.fetchall()
        for e,f,g,h in data:
            t.add_row([e,f,g,h])
        print(t)
    elif ch in "Ff":
        t=PrettyTable(['Cust_Name','Cust_Phone','Cust_email','Gender'])
        st="select * from customer where gender='f'"
        cur.execute(st)
        data=cur.fetchall()
        for e,f,g,h in data:
            t.add_row([e,f,g,h])
        print(t)      
    else:
        print("Incorrect choice")
        print("Enter Again")
print("Welcome to Balbir's Departmental Store")
a='''
1.New customer
2.New member
3.Show product
4.Billing
5.Search Item
6.Exit'''
a2='''
1.Search item
2.Add item
3.Delete item
4.Product Having No Stock
5.search poduct having particular brand
6.Segregate non member customer  according to gender
7.Segregate non member customer  according to gender
8.Exit'''
a3=True
while True:
    a4='''
    1.customer
    2.Manager
    3.Continue'''
    print(a4)
    ch=int(input("Enter your choice:"))
    if ch==1:
        print("Welcome")
        break
    elif ch==2:
        ID=int(input("Enter Manager id:"))
        if ID==22:
            print("Welcome Manager")
            a3=False
            break
        else:
            print("Incorrect ID")
            print("Enter Again")
    elif ch==3:
        break
    else:
        print("Incorrect choice")
        print("Enter Again")
if a3==True:
    while True:
        print(a)
        ch=int(input("Enter your choice"))
        if ch==1:
            all_cust()
        elif ch==2:
            member_cust()
        elif ch==3:
            items()
        elif ch==4:
            Order()
        elif ch==5:
            search_item_customer()
        elif ch==6:
            print("Thank you")
            print("Please visit again")
            break
        else:
            print("Incorrect Choice")
            print("Enter Again")
else:
    while True:
        print(a2)
        ch=int(input("Enter your choice:"))
        if ch==1:
            search_item_manager()
        elif ch==2:
            additems()
        elif ch==3:
            remove_item()
        elif ch==4:
            productQty_0()
        elif ch==5:
            Brand()
        elif ch==6:
            cust()
        elif ch==7:
            mem()
        elif ch==8:
            print("Thank for using our software")
            print("Hope you loved our services")
            break
        else:
            print("Incorrect choice")
            print("Enter Again")
            
            
    
            
            
        
        
    
    

    
        
                
            
            
        
            
            
            
            
                     
                
                
                
                
                
            
                
            
                
                            
    
    
            
        
        
        
    
    
    
    
            
            
            
        

     
     
            

