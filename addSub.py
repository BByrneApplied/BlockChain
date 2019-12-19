choice = ""

while choice != "add" and choice != "subtract" and choice !="multiply" and choice !="divide":

    choice = input("Would you like to add, subtract, divide or multiply? ")

    if choice != "add" and choice != "subtract" and choice !="multiply" and choice !="divide":

        print("You must enter add,subtract,divide or multiply")

sum1 = input("Please enter the first integer you would like to " + choice + " \n")

sum2 = input("Please enter the second integer you would like to " + choice + " \n")

def switch_func(value):
    return {
        'add': int(sum1) + int(sum2),
        'subtract': int(sum1) - int(sum2),
        'divide': int(sum1) / int(sum2),
        'multiply': int(sum1) * int(sum2),
    }.get(value)

print('The answer is : ', switch_func(choice))