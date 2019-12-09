
userInput = str(input("Please enter an arithmetic expression: "))
numberList = (userInput.replace('+',' ').replace('-',' ').split())
equationCheck = list(userInput)

#Checks for empty string

if len(userInput) == 0:
    print("Empty string")
    exit()

#Checking if values can be accepted

equationLength = len(equationCheck)
acceptables=["1","2","3","4","5","6","7","8","9","0","+","-"]
i = 0

for i in range(equationLength):
    if (equationCheck[i]) not in acceptables:
        print ("Invalid expression")
        exit()
    else:
        i = i + 1

#Checking for erroneous inputs

operationSymbols = ["+","-"]

j = 0
for j in range(equationLength):
    if equationCheck[-1] in operationSymbols:
        print ("Invalid expression")
        exit()
    else:
        j = j + 1

#Checks for first symbols

swapNeg = 1

if equationCheck[0] == "+" or equationCheck[0] == "-":
    startSymbol = True
else:
    startSymbol = False

while startSymbol == True:
    if "+" in equationCheck[0]:
        equationCheck.remove(equationCheck[0])
    elif "-" in equationCheck[0]:
        equationCheck.remove(equationCheck[0])
        swapNeg = swapNeg * -1
    else:
        startSymbol = False

firstNumber = int(numberList[0]) * int(swapNeg)

numberList.insert(0, firstNumber)
numberList.remove(numberList[1])

#Setting up variables

symbol = 0
symbolPosition = 0

#Checks operator symbols throughout list

while len(numberList) > 1:

    while symbol == 0:

        if "+" in equationCheck and "-" in equationCheck:
            if (equationCheck.index("+")) < (equationCheck.index("-")):
                symbol = 1
            else:
                symbol = 2
        elif "+" in equationCheck:
            symbol = 1
        elif "-" in equationCheck:
            symbol = 2

    while symbol == 1:
        symbolPosition = (equationCheck.index("+"))
        addPos = int(symbolPosition) + 1

        if "+" in equationCheck[addPos]:
            equationCheck.remove(equationCheck[addPos])
                
        elif "-" in equationCheck[addPos]:
            equationCheck.remove(equationCheck[symbolPosition])
            symbol = 2

        else:
            numberList[0] = int(numberList[0]) + int(numberList[1])
            numberList.remove(numberList[1])
            equationCheck.remove(equationCheck[symbolPosition])
            symbol = 0

    while symbol == 2:
        symbolPosition = (equationCheck.index("-"))
        minusPos = int(symbolPosition) + 1

        if "-" in equationCheck[minusPos]:
            equationCheck.remove(equationCheck[minusPos])
            equationCheck.insert(symbolPosition, "+")
            equationCheck.remove(equationCheck[minusPos])
            symbol = 1
                
        elif "+" in equationCheck[minusPos]:
            equationCheck.remove(equationCheck[minusPos])

        else:
            numberList[0] = int(numberList[0]) - int(numberList[1])
            numberList.remove(numberList[1])
            equationCheck.remove(equationCheck[symbolPosition])
            symbol = 0

result = int(numberList[0])
output = result + 0

#Prints result

print ("The result is " + str(output) + ".")
print ("Goodbye.")
