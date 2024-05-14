from Table import Table


class Reservation:
    list_of_revervations=[]

    def __init__(self, client_name, client_surname, table):
        self.__client_name=client_name
        self.__client_surname=client_surname 
        self.__table_name=table.get_table_name()
        self.__table_color=table.get_table_color()
        self.__table_id=table.get_table_id()

    def __str__(self):
        return f"Ordering client name: {self.__client_name} Ordering client surname: {self.__client_surname} Ordered table name: {self.__table_name} Ordered table color: {self.__table_color} Ordered table id: {self.__table_id}"


def reserve_table():
    try:
        table_id=int(input("Enter table id here that you want to order: \n"))
        budget=float(input("Enter your budget here: \n"))
        name=input("Enter your name here: \n")
        surname=input("Enter your surname here: \n")
        table=Table.list_of_tables[table_id-1]
        if budget>table.get_table_price():
            del Table.list_of_tables[table_id-1]
            reservation=Reservation(name, surname, table)
            Reservation.list_of_revervations.append(reservation)
            print("Reservation successfull")
        else:
            print("Cannot order table. Table price is higher than your budget")
    except ValueError:
            print("Please make sure that your budget consists only of digits")
    except IndexError:
        print("Table id not recognized. Please try again")


def view_reservations():
    if len(Reservation.list_of_revervations)==0:
        print("No reservations at current time")
    else:
        for reservation in Reservation.list_of_revervations:
            print(reservation)