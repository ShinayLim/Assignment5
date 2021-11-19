def insertNumber():
    global number1
    global number2
    global number3
    number1 = int(input('Enter First number : '))
    number2 = int(input('Enter Second number : '))
    number3 = int(input('Enter Third number : '))

def highest(number1, number2, number3):
    if (number1 > number2) and (number1 > number3):
        largestNum = number1
    elif (number2 > number1) and (number2 > number3):
        largestNum = number2
    else:
        largestNum = number3
    print("The largest of the 3 numbers is : ", largestNum)

def lowest(number1, number2, number3):
    if (number1 < number2) and (number1 < number3):
        smallestNum = number1
    elif (number2 < number1) and (number2 < number3):
        smallestNum = number2
    else:
        smallestNum = number3
    print("The smallest of the 3 numbers is : ", smallestNum)