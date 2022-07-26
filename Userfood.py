import Adminfood as ad

class User :
      login_info = {}
      def __init__(self,email,name,phone_no,address,password):
          self.email = email
          self.name = name
          self.phone_no = phone_no
          self.address = address
          self.password = password
          User.login_info[self.email] ={'Email':self.email,'Full_Name':self.name,'Phone_no':self.phone_no,'Address':self.address,'Password':self.password,}
                                               
          self.order_history = {}


      def place_order(self):
          print("What you want to order : ")
          ad.show_menu()
          choice_user = int(input("If you want to order then select 1.YES  2.NO"))
          if choice_user == 1:
              n=int(input("How many Item do You Want to Order "))
              total_value=0
              discount=0
              for i in range(n):
                  uitemid = int(input("Enter the Item id here: "))
                  quan = int(input("Enter the quantity of the item: "))
                  total_value = total_value + ad.food_menu[uitemid]['Price'] * quan
                  discount += ad.food_menu[uitemid]['%Discount']
                  ad.food_menu[uitemid]['Av_Stock'] = ad.food_menu[uitemid]['Av_Stock']-quan
                  self.order_history[uitemid] = {
                      "Itemname": ad.food_menu[uitemid]["Itemname"],
                      "Price": ad.food_menu[uitemid]["Price"],
                      "Quantity": quan
                                                }
              order_confirm = input("want to proceed  Yes or NO ")
              if order_confirm == 'Yes':
                  print(f"Total Discount Allowed is {discount} ")
                  print(f"After  Discount total costs is {total_value-discount} INR in total")
                  print("You're order is successfully placed...")

              elif order_confirm=="No":
                  print("Order has been Cancelled ")
                  self.order_history.clear()

              else :
                  print("Invalid choice")

          elif choice_user == 2:
              print("Thank you for visiting")

          else:
              print(" Invalid selection ")


      def food_order_history(self):
        print(self.order_history)


      def profile_updation(self):
          print("Update Profile Here")
          email=input("Enter Your Mail-id ")
          if email in User.login_info.keys():
              print("Email Matched ")
              del User.login_info[email]

              new_email=input("Enter new  Email ")
              new_name = input("Enter new  Name ")
              new_phone_no = int(input("Enter new  Phone No "))
              new_Address = input("Enter new  Address ")
              new_password = input("Enter new  Password ")

              User.login_info[new_email] = {'Email': new_email,
                                                    'Full_Name': new_name,
                                                    'Phone_no': new_phone_no,
                                                    'Address': new_Address,
                                                    'Password': new_password,
                                                    }
              print("Profile Updated Successfully")

          else :
              print("Email not Registered")

      @classmethod
      def login(cls, email, password):
          if  email in cls.login_info.keys():
              if cls.login_info.get(email)['Password'] == password:
                 print(f"logged in Successfully {cls.login_info.get(email)['Full_Name']}")
                 return True
              else:
                 print("SORRY! These are the Wrong Credentials")
                 return False
          else:
              print(f"{email} Not registered please register first ")
              return False


# Test Purpose Ignore This
"""obj=Application('piyush@gmail.com', 'Piyush' ,8852978223, 's-198', 'Piyush@123')
obj.print_profile()"""


"""def check_user(self, email, password):
    if email in Application.login_info.keys():
        if Application.login_info[email]['Password'] == password:
            print("Now...  You are Loggedin  ")
        else:
            print("Password does not Matched")
    else:
        print(f"{email} Not Registered Yet.. First Register then Come Again !!!!! ")
"""
