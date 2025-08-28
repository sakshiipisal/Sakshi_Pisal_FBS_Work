u= input("Enter User Id:")
p= input("Enter Password:")

if(u == 'sakshi' and p == 'sakshi2719'):
    c=input("Enter Captcha")

    if(c == "2719"):
        print("Successfully Login")
    else:
        print("Failed Captcha")
else:
    print("Invalid")