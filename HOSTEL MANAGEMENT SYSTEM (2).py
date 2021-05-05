print("**********************************************")
print("**********************************************")
print("**          __         __   __         __   **")
print("**    |  | |__  |     |    |  |  |\/| |__   **")
print("**    |/\| |__  |___  |__  |__|  |  | |__   **")
print("**                _____   __                **")
print("**                  |    |  |               **")
print("**                  |    |__|               **")
print("**   __   _ _       __        __            **")
print("**  |  _   |  \  / |__  |\ | |    |__|  \_/ **")
print("**  |__/  _|_  \/  |__  | \| |__  |  |   |  **")
print("**                                          **")
print("**********************************************")
print("**********************************************")
from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
if current_time>='00:00:00' and current_time<'12:00:00':
    print("Good Morning !")
elif current_time>='12:00:00' and current_time<'16:00:00':
    print("Good Afternoon !")
else:
    print("Good Evening !")
print("You are welcome to our Hostel Givenchy")
print("Our Hostel Have 100 Rooms")
print("From 100 rooms, 50 rooms hare AC Room and 50 are Non-AC rooms")
print("")
import random
def search(x):
    import os
    import sys
    import fileinput
    
    tempFile = open( 'Records.txt', 'a+' )
    for line in fileinput.input( 'Records.txt' ):
        if x in line:
            return 'Stop'
        else:
            return 'Please Continue'
    
def HMS():
    
    print("Choices")
    print("1.Make an Admission")
    print("2.Edit students detail")
    print("3.Want to see students list")
    print("0.To exit")
    x=int(input("Enter Your Choice : "))
    if x==1:
        p=random.randint(10000,100000)
        q=str(p)
        print(search(q))
        print("Admmision Number : ",q)
        def adm(p):
            a=str(input("Enter Name : "))
            print("Choose your Gender : ")
            print("1.Male")
            print("2.Female")
            print("3.Others")
            gen=int(input("Choose 1, 2 or 3 : "))
            if gen==1:
                gen=str("Male")
            elif gen==2:
                gen=str("Female")
            elif gen==3:
                gen=str("Others")
            else:
                print("Invalid Input")
                x=str(input("Enter Your Gender (In words): "))
            b=input("Enter Phone Number : ")
            if len(b)==10:
                print("")
            else :
                print(b,"is not a valid ")
                b=input("Enter Phone Number : ")
                if len(b)==10:
                    print()
                else:
                    print("Invalid input")
                    exit()
            c=input("Enter D.O.B (dd/mm/yyyy) : ")
            h=str(input("Enter you Email ID : "))
            
            y=random.randint(111111,999999)
            z=str(y)
            import smtplib 
            li = [h] 
     
            for dest in li:
                s=smtplib.SMTP('smtp.gmail.com', 587) 
                s.starttls() 
                s.login("sasoni2712@gmail.com", "ShivamAtulsoni03") 
                message = ('YOU OTP is '+z)
                subject = "OTP Verification"
                s.sendmail("MyHostel365@gmail.com", dest, message) 
                s.quit()
            print("An OTP is Sent to Your Mail ID")
            w=str(input("Enter OTP : "))
            if w==z:
                print("Email Verified")
            else :
                print("Invalid OTP")
                y=random.randint(111111,999999)
                z=str(y)
                import smtplib 
                li = [h] 
     
                for dest in li:
                    s=smtplib.SMTP('smtp.gmail.com', 587) 
                    s.starttls() 
                    s.login("MyHostel365@gmail.com", "MyHostel365365") 
                    message =z
                    subject = "OTP Verification"
                    s.sendmail("MyHostel365@gmail.com", dest, message) 
                    s.quit()
                print("An OTP is once again Sent to Your Mail ID")
                w=str(input("Enter OTP : "))
                if w==z:
                    print("Email Verifiesd")
                else:
                    print("INCORRECT OTP")
                    print("Sorry But no room will be alloted to you")
                    print("")
                    exit()
                
            print("Type of Room Wanted ")
            print("1.AC")
            print("2.Non AC")
            d=int(input("Enter Your Choice (Choose 1 or 2) : "))
            if d==1:
                print("Price is Rs.15,000/Month (Includes Lunch and Dinner)")
            elif d==2:
                print("Price is 10,000/Month (Includes Lunch and Dinner)")
            else:
                print("Invalid input")
                quit()
            e=int(input("For How much time do you need room (Enter in number of months) : "))
            if d==1:
                print("Total Cost will be : ",15000*e)
            elif d==2:
                print("Total Cost will be : ",10000*e)
            else :
                print("Invalid Input")
                exit()
            n=random.randint(101,200)
            print("Room Alloted to You will be",n)
            
            print("*******************************")
            print("*******************************")
            print("Your Details are : ")
            print("Name : ",a)
            print("Phone Number : ",b)
            print("D.O.B : ",c)
            print("You want to live here for ",e," Months")
            v=str(e)
            print("Room Alloted to you is : ",n)
            print("*******************************")
            print("*******************************")
            g=str(n)
            f=open('Records.txt','a+')
            oo=f.writelines("*************************")
            ad=f.writelines('Admission Number : ')
            no=f.writelines(q)
            u=f.writelines('Name : ')
            l=f.writelines(a)
            gend=f.writelines('Gender: ')
            ans=f.writelines(gen)
            h=f.writelines('Phone Number : ')
            m=f.writelines(b)
            i=f.writelines('D.O.B : ')
            o=f.writelines(c)
            j=f.writelines('No Of Months To Live : ')
            p=f.writelines(v)
            k=f.writelines('Room No : ')
            r=f.writelines(g)
            f.close()
            print(HMS())
            return a,b,c,v,g
        print(adm(p))
    elif x==2:
        a=input("Enter text to replace : ")
        b=input("Enter text to replace it with : ")
        with open('Records.txt', 'r+') as f:
            file_source = f.read()
            replace_string = file_source.replace(a,b)
            write_file = f.write(replace_string)
        f.close()
        print("You Data has been Updated")
        print("Thank You")
        print("***************************")
        print(HMS())
    elif x==3:
        i=open('Records.txt','r')
        f=i.read()
        print(f)
        i.close()
        print("***************************")
        print(HMS())
    elif x==0:
        exit()
    else:
        print("Invalid Choice")
        print("***************************")
        print(HMS())
print("***************************")
print(HMS())
