# Create a sportMart class, where you will have :- 
# inventory/shelf of items
# orders of customers

# create csv file which will store your inventory details and order details

# with the help of file handling techniques in python, read the file and create an object for trinity 
# store and populate the inventory items and orders into the trinity store

# to make sure that you have added all the items in your file, use a display method to show your inventory
# and order history

# write a menu-driven to create new order and update inventory
# export to file then

class SportMart:

    def __init__(self):
        self.inventory = {}
        self.orders = {}

    def create_inventory(self,ProductID,ProductName,Quantity,Price):
        temp = {
            'PID' : ProductID.strip().upper(),
            'PName' : ProductName.strip().upper(),
            'Qty' : int(Quantity),
            'PP' : int(Price)
        }
        self.inventory[ProductID] = temp

    def create_order(self,OrderID,ProductID,Quantity,UnitPrice,TotalPrice):
        temp = {
            'OID' : OrderID.strip().upper(),
            'PID' : ProductID.strip().upper(),
            'Qty' :int(Quantity),
            'PP' : int(UnitPrice),
            'TP' : int(TotalPrice)
        }
        self.orders[OrderID] = temp

    def disp_orders(self):
        print('The order details are:')
        print()
        for x in self.orders.values():
            print(x)
        print()

    def disp_inventory(self):
        print('The inventory details are:')
        print()
        for x in self.inventory.values():
            print(x)
        print()

    def create_new_order(self,OrderID,ProductID,Quantity,UnitPrice,TotalPrice):
        new = {
            'OID' : OrderID.strip().upper(),
            'PID' : ProductID.strip().upper(),
            'Qty' : int(Quantity),
            'PP' : int(UnitPrice),
            'TP' : int(TotalPrice)
        }
        self.orders[OrderID] = new


        if ProductID in self.inventory:
            self.inventory[ProductID]['Qty'] -= int(Quantity)
            print('\n Updated Inventory')
            for x in self.inventory.values():
                print(x)
        else:
            print('Product ID not found!!')
        
    def export_to_file(self):
        try:
            with open('Inventory.csv', 'r') as inv_file:
                self.existing_inventory_data = inv_file.readline()

            with open('Inventory.csv', 'w') as inv_file:
                inv_file.write(self.existing_inventory_data)
                for item in self.inventory.values():
                    inv_file.write(str(item['PID']) + ',' + str(item['PName']) + ',' + str(item['Qty']) + ',' + str(item['PP']) + '\n')
        
            with open('Order.csv', 'r') as ord_file:
                self.existing_order_data = ord_file.readline()

            with open('Order.csv','w') as ord_file:
                ord_file.write(self.existing_order_data)
                for order in self.orders.values():
                    ord_file.write(str(order['OID']) + ',' + str(order['PID']) + ',' + str(order['Qty']) + ',' + str(order['PP']) + ',' + str(order['TP']) + '\n')
            print('Files updated!')
        except:
            print('Files not found!')

trinity = SportMart()

orders = open('Order.csv','r')
o_header = orders.readline()
o_data = orders.readlines()

tot_qty = 0
for data in o_data:
    tmp = data.strip().split(',')
    trinity.create_order(tmp[0],tmp[1],tmp[2],tmp[3],tmp[4])

for i in o_data:
    tp = i.strip().split(',')
    qty = int(tp[2])
    tot_qty += qty
print('The total qty is:',tot_qty)

trinity.disp_orders()

inv = open('Inventory.csv','r')
i_header = inv.readline()
i_data = inv.readlines()

for i in i_data:
    tmp = i.strip().split(',')
    trinity.create_inventory(tmp[0],tmp[1],tmp[2],tmp[3])

trinity.disp_inventory()

while True:
    print('MENU:')
    print('1. Create new order')
    print('2. Export to file') 
    print('3. Quit')

    choice = int(input('Enter your choice:'))
    print('Your entered choice is',choice)

    if choice == 1:
        OrderID = input('Enter the order id:')
        ProductID = input('Enter the Product ID')
        Quantity = input('Enter the order qty')
        UnitPrice = input('Enter the unit price')
        TotalPrice = int(Quantity) * int(UnitPrice)
        trinity.create_new_order(OrderID,ProductID,Quantity,UnitPrice,TotalPrice)
    elif choice == 2:
        trinity.export_to_file()
    elif choice == 3:
        break
    else:
        print('Invalid choice, try again!')