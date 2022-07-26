
admin_info={"kkr":"K@123"}

food_menu={1:{'Itemid':1,'Itemname':'Rasgulla','Quantity':100,'Price':10,'%Discount':0,'Av_Stock':100},
           2:{'Itemnid':2,'Itemname':'Rabdi','Quantity':20,'Price':30,'%Discount':5,'Av_Stock':20},
           }

item_id=2
def add_fooditem():
    global item_id
    item_id=item_id+1
    item_name=input("Enter food item Name ")
    item_quantity = int(input("Enter food item Quantity "))
    item_price = int(input("Enter food item Price "))
    item_discount = int(input("Enter food item Discount "))
    item_stock = int(input("Enter food item Stock "))


    if item_id in food_menu.keys():
        print("You Can't Add New Food Item!!!   Id is already Present ")
    else :
        food_menu[item_id]={'Itemid':item_id,
                            'Itemname':item_name,
                            'Quantity':item_quantity,
                            'Price':item_price,
                            '%Discount':item_discount,
                            'Av_Stock':item_stock
                            }
        print("Food Item Successfully Added.......")

def edit_fooditem():
    itemid = int(input("Enter food item id "))
    if itemid in food_menu.keys():
        print("You can edit items:")
        item_name = input("Enter food item Name ")
        item_quantity = int(input("Enter food item Quantity "))
        item_price = int(input("Enter food item Price "))
        item_discount = int(input("Enter food item Discount "))
        item_stock = int(input("Enter food item Stock "))
        
        food_menu[itemid]['Itemname']=item_name
        food_menu[itemid]['Quantity']=item_quantity
        food_menu[itemid]['Price'] = item_price
        food_menu[itemid]['%Discount'] = item_discount
        food_menu[itemid]['Av_Stock'] = item_stock
        print(f"{itemid}  is Updated Successfully.......!")

    else :
        print(f"{itemid}  is Not Present Inside the Menu List.......")


def show_menu():
    i=0
    for values in food_menu.values():
        i=i+1
        print(i, values)

def remove_item():
    
    itemid = int(input("Enter food item id "))
    if itemid in food_menu.keys():
        del  food_menu[itemid]
        print(f"{itemid} is Deleted Successfully..!!!")
    else :
        print(f"{itemid} is not in menu.......")
