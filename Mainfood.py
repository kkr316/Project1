import Adminfood as admin
from Userfood import User
user=User(str,str,str,str,str)
# start code
temp_variable=1
temp_var=True
while temp_var :

    inp=int(input("Where You Want to Login?? 1. Admin  2. User  3. User Registration 4. Exit "))
    #if temp_variable == 0:
      #  temp=True
# check inp
    if inp == 1:
       print("Login AS  Admin Panel..")
       username=input("Enter a Username ")
       password = input("Enter a Password ")
       if admin.admin_info[username] == password:
         print("you Logged in ********** Successfully  ********************")
         while temp_var:
            admin_input = int(input(
                "Choose the options of admin panel 1.ADD NEW ITEM 2.EDIT ITEM 3.VIEW Menu List 4.REMOVE ITEM 5.EXIT"))
            if admin_input == 1:
                admin.add_fooditem()
            elif admin_input == 2:
                admin.edit_fooditem()
            elif admin_input == 3:
                admin.show_menu()
            elif admin_input == 4:
                admin.remove_item()
            elif admin_input == 5:
                print(f"You're Exit to the admin panel   {username}")
                temp_var = False
            else:
                print("Wrong input Please Read Carefully Instruction  !!!")

       else :
           print("Invalid Credentials !!!!! ")


    elif inp == 2 :
      print("Login As User Panel..")
      enter_email = input("Enter a Email ")
      password = input("Enter a Password")

      if User.login(enter_email,password):
        temp=True
        while temp:
            choice_user = int(input(f"{enter_email},Enter the option 1. Place new order 2. Order history 3. Update Profile 4. Exit"))
            if choice_user == 1:
                user. place_order()

            elif choice_user == 2:
                user.food_order_history()

            elif choice_user ==3:
                user.profile_updation()
                temp=False

            elif choice_user == 4:
                print("You're Successfully logged out")
                temp= False
            
            else:
                print("Wrong selection ")

    elif inp == 3:

      new_email = input("Enter new  Email ")
      if new_email in user.login_info.keys():
        print("Email Already Registered.......")
      else :
        #print("Enter Your Detail Here <<<<<-")
        new_name = input("Enter new  Name ")
        new_phone_no = int(input("Enter new  Phone No "))
        new_Address = input("Enter new  Address ")
        new_password = input("Enter new  Password ")
        user=User(new_email,new_name,new_phone_no,new_Address,new_password)

        print("Your have Registered Successfully.......")
        print("Now you can Login... ")


    elif inp == 4:
        temp_var=False
        exit()

    else :
      print("Wrong selection made ")


