#Times Table Teller
import time
e=1

t=int(input("Which Times Table would you like?"))
time.sleep(1)

while e<13:
    print(e*t)
    e=e+1
    time.sleep(1)
    
