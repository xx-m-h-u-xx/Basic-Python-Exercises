def chooseoption():
    print("Choose your option please")
    option=input()
    while option !="1" and option !="2":
        print("Choose your option please")
        option=input()

print("Welcome to my Questionnaire")
print("Would you like to 1: Go to School or 2: Stay in Bed")
chooseoption()
print ("Question 2. Which Team Would You Rather Play For...1: Play for Man United 2: Play for Man City?")
chooseoption()
print("Question 3. Who is better 1: Rademel Falcao or 2: Sergio Aguero?")
chooseoption()
print("Question 4. Who is better 1: Louis Van Gaal or 2: Jose Mourinho")
chooseoption()
print("Question 5. Who will win the title 1: Chelsea, 2: Man City or 3: Man United")
chooseoption()
if chooseoption=="3":
    print("Why Not The Red Devils!!!")
if chooseoption=="2":
    print("Man Shity!")
if chooseoption=="1":
    print("Just Because Eden Hazard!!!!")
print("Thank You For Your Time and For Doing The Quiz...")
