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