choice = ""

while choice != "add" and choice != "subtract":
    choice = input("Would you like to add or subtract? ")
    if choice != "add" and choice != "subtract":
        print("You must enter add or subtract")


sum1 = input("Please enter the first integer you would like to " + choice + " \n")

sum2 = input("Please enter the second integer you would like to " + choice + " \n")

if choice == "add" :
    mathCond = int(sum1) + int(sum2)

if choice == "subtract" :
    mathCond = int(sum1) - int(sum2)

def calc():
    print("Your answer is: ", mathCond)

calc()
