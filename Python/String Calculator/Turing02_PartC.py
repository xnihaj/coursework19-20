#Takes user input and converts into lists

userInput = str(input("Please enter an arithmetic expression: "))
numberList = (userInput.replace('+',' ').replace('-',' ').replace('*',' ').split())
equationCheck = list(userInput)
equationLength = len(equationCheck)

#Checks for empty string

if len(userInput) == 0:
    print("Empty string")
    exit()

#Checking if values can be accepted
    
acceptables = ["1","2","3","4","5","6","7","8","9","0","+","-","*"]

i = 0
for i in range(equationLength):
    if (equationCheck[i]) not in acceptables:       
        print ("Invalid expression")
        exit()
    else:
        i = i + 1

#Checking for erroneous inputs 

operationSymbols = ["+","-","*"]

j = 0
for j in range(equationLength):

    if equationCheck[-1] in operationSymbols:
        print ("Invalid expression")
        exit()
    
    elif equationCheck[j] in operationSymbols and equationCheck[j+1] in operationSymbols:
        print ("Invalid expression")
        exit()
    else:
        j = j + 1

#Splitting input into only symbols list

symbolPosList = []
for x in userInput:
    if not x.isdigit():
        symbolPosList.append(x)

#Setting up variables

symbol = 0
symbolPosition = 0

#Checks operator symbols throughout list

while len(numberList) > 1:    

    while symbol == 0:
        if "*" in symbolPosList:
            symbolPosition = int(symbolPosList.index("*"))
            numberAfterSymbol = symbolPosition + 1
            numberList[symbolPosition] = int(numberList[symbolPosition]) * int(numberList[numberAfterSymbol])
            numberList.remove(numberList[numberAfterSymbol])
            symbolPosList.remove(symbolPosList[symbolPosition])
        elif "+" in equationCheck and "-" in equationCheck:
            if (equationCheck.index("+")) < (equationCheck.index("-")):
                symbol = 1
            else:
                symbol = 2
        elif "+" in equationCheck:
            symbol = 1
        elif "-" in equationCheck:
            symbol = 2
        else:
            break

#1 = addition symbol
        
    while symbol == 1: 
        numberList[0] = int(numberList[0]) + int(numberList[1])
        numberList.remove(numberList[1])
        symbolPosition = (equationCheck.index("+"))
        equationCheck.remove(equationCheck[symbolPosition])
        symbol = 0

#2 = subtraction symbol
        
    while symbol == 2:
        numberList[0] = int(numberList[0]) - int(numberList[1])
        numberList.remove(numberList[1])
        symbolPosition = (equationCheck.index("-"))
        equationCheck.remove(equationCheck[symbolPosition])
        symbol = 0
        
#Formatting final result

result = int(numberList[0])
output = result + 0

#Printing result

print ("The result is " + str(output) + ".")
print ("Goodbye.")
