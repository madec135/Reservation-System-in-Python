class Table:
    list_of_tables=[]
    id=1

    def __init__(self, table_name, table_price, table_color):
        self.__table_name=table_name
        self.__table_price=table_price
        self.__table_color=table_color
        self.__table_id=Table.id
        Table.id+=1

    def get_table_name(self):
        return self.__table_name
    
    def get_table_price(self):
        return self.__table_price
    
    def get_table_color(self):
        return self.__table_color
    
    def get_table_id(self):
        return self.__table_id

    def __str__(self):
        return f"Table name: {self.__table_name} Table price: {self.__table_price} Table color: {self.__table_color} Table id: {self.__table_id}"



def create_table():
    try:
        table_name=input("Enter table name here: \n")
        table_price=float(input("Enter table price here: \n"))
        table_color=input("Enter table color here: \n")
        table=Table(table_name, table_price, table_color)
        Table.list_of_tables.append(table)
        print("Table created successfully")
    except ValueError:
        print("Wrong table data. Please try again. Make sure that table price consists only of digits")



def view_tables():
    if len(Table.list_of_tables)==0:
        print("No available tables at moment")
    else:
        for table in Table.list_of_tables:
            print(table)


