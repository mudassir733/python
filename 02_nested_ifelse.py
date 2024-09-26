
score = input("What is your score?") 

score = int(score)

if score >= 90:
    age = int(input("What is your age?"))
    if age >= 18:
        print("Congratulations! You passed with distinction. Grade A+")
    else:
        print("Sorry, you did not pass with distinction.")
elif score >= 50:
    age = int(input("What is your age?"))
    if age >= 18:
        print("Congratulations! You passed. Grade B+")
    else:
        print("Sorry, you did not pass.")
elif score >= 40:
    print("Your grade is C")
else:
    print("Your grade is F")


