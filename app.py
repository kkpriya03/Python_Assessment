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
        input("\n\tPress Enter To Continue")