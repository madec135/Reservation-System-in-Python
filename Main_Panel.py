from Table import create_table
from Table import view_tables
from Reservation import reserve_table
from Reservation import view_reservations


def main():
    while True:
        try:
            choice=int(input("Enter 1 to create table. Enter 2 to see available tables. Enter 3 to order table. Enter 4 to see all ordered tables. Enter 0 to exit from program \n"))
            if choice==1:
                create_table()
            elif choice==2:
                view_tables()
            elif choice==3:
                reserve_table()
            elif choice==4:
                view_reservations()
            elif choice==0:
                break
            else:
                print("Choice not recognized. Please try again")
        except ValueError:
            print("Choice not recognized. Please select what you want to do by entering digit")


if __name__=="__main__":
    main()