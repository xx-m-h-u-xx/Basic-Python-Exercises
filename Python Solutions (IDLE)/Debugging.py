# Practise Activity Debugging --- #

file=open("Python test.", "a+")
again = "Y"
while again == "Y":
    name=input("Please type in a name: ")
    file.write(name+"\n")
    again=input("Do you want to enter another name (Y/N)? ")
    again=again.upper()
file.close()
