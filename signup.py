# the sign up class which has firstname ,lastname,phone.no,password and password
# confirmation as well as delivery location enables first first users to set up their 
# kijani groceries account.
# It also confirms  whether the password input is correct through the password 
# confirmation method.
# upon successfully setting up an account the user proceeds to log in into the kijani groceries

class signup:
    def __init__(self,First_Name,Last_Name,Email_Address,Phone_No,Account_password,Password_Conf,Delivery_Location) :
        self.First_Name=First_Name
        self.Last_Name=Last_Name
        self.Email_Address=Email_Address
        self.Phone_No=Phone_No
        self.Account_password=Account_password   
        self.Password_Conf=Password_Conf
        self.Delivery_Location=Delivery_Location
        
# password confirmation checks if the account password is correct

    def password_conf(self):
        if(self.Account_password==self.Password_Conf):
            print( f"Valid password")
        else:
            print(f"Please enter the correct password")

    def log_in (self,email,password):
        if email== self.Email_Address:
            return (f"Email successful")   
        elif password== self.Account_password:
            return(f"Password successful")
        else :
            return(f"Your email does not match your password")
