#DBConnection
import mysql.connector

class DBConnect:
    def getConnection():
        conn = mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='root',
            database='hotel'
        )
        return conn
#Entity    
class Booking:
    def __init__(self, cname, phone, room_type, days, checkin_date, checkout_date, total_amount):
        self.cname = cname
        self.phone = phone
        self.room_type = room_type
        self.days = days
        self.checkin_date = checkin_date
        self.checkout_date = checkout_date
        self.total_amount = total_amount

#App.py
#DashBoard
from dao import Dao
from entity import Booking

while True:
    print("\n\t--- HOTEL BOOKING SYSTEM ---")
    print("\n\t1. Add Booking")
    print("\t2. View Booking")
    print("\t3. Delete Booking")
    print("\t4. Update Booking")
    print("\t0. Exit")

    ch = int(input("\nEnter choice: "))

    if ch == 0:
        print("Thank You!")
        break

    elif ch == 1:
        cname = input("\n\tName: ")
        phone = input("\tPhone: ")
        room_type = input("\tRoom Type (AC/Non-AC): ")
        days = int(input("\tDays: "))
        checkin = input("\tCheck-in Date: ")
        checkout = input("\tCheck-out Date: ")

        bk = Booking(cname, phone, room_type, days, checkin, checkout, 0)
        Dao.addBooking(bk)
        input("\n\tPress Enter To Continue")

    elif ch == 2:
        Dao.viewAllBooking()
        input("\n\tPress Enter To Continue")

    elif ch == 3:
        bid = input("\n\tEnter Booking ID: ")
        Dao.deleteBooking(bid)
        input("\n\tPress Enter To Continue")

    elif ch == 4:
        bid = input("\n\tEnter Booking ID: ")
        cname = input("\tName: ")
        phone = input("\tPhone: ")
        room_type = input("\tRoom Type: ")
        days = int(input("\tDays: "))
        checkin = input("\tCheck-in: ")
        checkout = input("\tCheck-out: ")

        Dao.updateBooking(bid, cname, phone, room_type, days, checkin, checkout)

    else:
        print("Wrong Choice!")

#Dao.py

from dbConnect import DBConnect

class Dao:

    #  ADD BOOKING
    def addBooking(bk):
        sql = """INSERT INTO booking
        (cname, phone, room_type, days, checkin_date, checkout_date, total_amount)
        VALUES (%s,%s,%s,%s,%s,%s,%s)"""
       

        if bk.room_type.lower() == "ac":
            price = 1000
        else:
            price = 500

        total = price * bk.days

        data= (bk.cname, bk.phone, bk.room_type, bk.days, bk.checkin_date, bk.checkout_date, total)
        conn = DBConnect.getConnection()
        cur = conn.cursor()

        cur.execute(sql,data)
        if cur.rowcount>0:
              print("\n\tBooking Added Successfully!")
        else:
            print("\n\tFailed To Add!")


        conn.commit()
        cur.close()
        conn.close()


    #  VIEW All Booking
    def viewAllBooking():
        sql = "SELECT * FROM booking"

        conn = DBConnect.getConnection()
        cur = conn.cursor()

        cur.execute(sql)
        data = cur.fetchall()

        for bk in data:
            print("\n\tID:", bk[0])
            print("\tName:", bk[1])
            print("\tPhone:", bk[2])
            print("\tRoom:", bk[3])
            print("\tDays:", bk[4])
            print("\tCheck-in:", bk[5])
            print("\tCheck-out:", bk[6])
            print("\tTotal:", bk[7])

        cur.close()
        conn.close()


    #  DELETE Any Booking
    def deleteBooking(bid):
        sql = "DELETE FROM booking WHERE bid=%s"

        conn = DBConnect.getConnection()
        cur = conn.cursor()

        cur.execute(sql, (bid,))

        if cur.rowcount > 0:
            print("\n\tBooking Deleted Successfully!")
        else:
            print("\n\tBooking Not Found!")

        conn.commit()
        cur.close()
        conn.close()


#  UPDATE Booking
def updateBooking(bid, cname, phone, room_type, days, checkin_date, checkout_date):
        sql = """UPDATE booking 
        SET cname=%s, phone=%s, room_type=%s, days=%s, checkin_date=%s, checkout_date=%s 
        WHERE bid=%s"""

        if room_type.lower() == "ac":
            price = 1000
        else:
            price = 500

        total = price * days

        conn = DBConnect.getConnection()
        cur = conn.cursor()

        cur.execute(sql, (
            cname, phone, room_type, days,
            checkin_date, checkout_date, bid
        ))

        if cur.rowcount > 0:
            print("\n\tBooking Updated Successfully!")
        else:
            print("\n\tBooking Not Found!")

        conn.commit()
        cur.close()
        conn.close()








        
        input("\n\tPress Enter To Continue")        
