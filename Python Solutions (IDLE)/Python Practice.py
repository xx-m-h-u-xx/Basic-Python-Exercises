tries=1
print("What is your password?")
password = input()
while password != "123asda":
    print("What is your password?")
    password =input()
    tries=tries+1print("you have tried",tries+1,"times")
if password == "123asda":
    print("Accepted")
    


