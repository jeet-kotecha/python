# use if else statment for check that user entered correct username and password 
un="bca"
pw="sem-5"

uname=input("Enter username:")
pword=input("Enter password:")

if uname==un and pword==pw:
    print("login successfully")
else:
    print("invalid username or password")    