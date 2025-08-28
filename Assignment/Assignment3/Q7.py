correct_userid="sakshi"
correct_password="sakshi2719"

userid=input("Enter a userid:")
password=input("Enter a password:")

if(correct_userid == userid and correct_password == password):
    print("Login Successfully")
else:
    print("Invalid user id and password")