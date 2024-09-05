
#PROJECT NAME: AIRLINE MANAGEMENT
#MADE BY: STEFI SHOBIKA SUKUMAR

import mysql.connector as ms
db=ms.connect(host="localhost",user="root",password="stefi",database="airline_management_system")
a=db.cursor()

def clear():
    for _ in range(2):
        print()
        
def flightnum():
    try:
        num=input("enter flight number:")
        query="select*from flight_details where flightnumber= %s"
        a.execute(query,(num,))
        record=a.fetchall()
        if record:
            for x in record:
                print(x)
        else:
            print("NO FLIGHT FOUND WITH THE GIVEN FLIGHT NUMBER")
            return None
    except:
        print("ERROR")
        return None

def add():
    b=input("enter flight number:")
    c=input("enter flight name:")
    d=input("enter model variant:")
    e=input("enter departure:")
    f=input("enter arrival:")
    g=input("enter departuretime:")
    h=input("enter arrivaltime:")
    i=input("enter flightstatus:")
    q1="insert into flight_details (flightnumber,flightname,modelvariant,departure,arrival,departuretime,arrivaltime,flightstatus)values (%s,%s,%s,%s,%s,%s,%s,%s)"
    val=(b,c,d,e,f,g,h,i)
    a.execute(q1,val)
    a.execute("select*from flight_details")
    record=a.fetchall()
    for x in record:
        print(x)
    db.commit()
    return

def remove():#removing details of a flight by using flightnumber
    try:
        b=input("enter flight number:")
        c=("delete from flight_details where Flightnumber=%S",(b,))
        print("The flight detail has been successfully removed")
        db.commit()
        return
    except:
        print("no flight found")
    
def flightstatus():#viewing details of a flight by its flight status
    try:
        b=input("enter flight status:")
        c=("select*from flight_details where flightstatus=%s")
        a.execute(c,(b,))
        record=a.fetchall()
        for x in record:
            print(x)
    except:
        print("NO FLIGHT FOUND")

def update():
    acd=input("enter the flight number to be modified:")
    bcd=input("enter the new departure time:")
    q1="update flight_details set departuretime=%s where flightnumber=%s"
    val=(bcd,acd)
    a.execute(q1,val)
    db.commit()
    print("DONE")
    print("DUE TO EARLY BOARDING THE DEPARTURE TIME HAS BEEN CHANGED")
    return

ch="y"
while ch=="y":
    clear()
    print("="*120)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ WELCOME TO TIRUCHIRAPALLI ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ AIRLINE MANAGEMENT SYSTEM ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("="*120)
    print("1.TO DISPLAY FLIGHT DETAILS")
    print("2.TO ADD NEW FLIGHT DETAILS")
    print("3.TO REMOVE FLIGHT DETAILS")
    print("4.TO VIEW DETAILS ACCORDING TO FLIGHTSTATUS")
    print("5.TO UPDATE FLIGHT DETAILS")
    choice=int(input("ENTER YOUR CHOICE (1..5):"))
    if choice==1:
        flightnum()
    if choice==2:
        add()
    if choice==3:
        remove()
    if choice==4:
        flightstatus()
    if choice==5:
        update()

    ch=input("do you wanna continue (y/n)?:")
db.close()
