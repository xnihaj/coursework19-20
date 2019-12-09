userInput = str(input("Please enter an arithmetic expression: "))
numberList = (userInput.replace('+',' ').replace('-',' ').split())
equationCheck = list(userInput)
symbol = 0
symbolPosition = 0

if len(userInput) == 0:
    print("Empty string")
    exit()

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
        numberList[0] = int(numberList[0]) + int(numberList[1])
        numberList.remove(numberList[1])
        symbolPosition = (equationCheck.index("+"))
        equationCheck.remove(equationCheck[symbolPosition])
        symbol = 0

    while symbol == 2:
        numberList[0] = int(numberList[0]) - int(numberList[1])
        numberList.remove(numberList[1])
        symbolPosition = (equationCheck.index("-"))
        equationCheck.remove(equationCheck[symbolPosition])
        symbol = 0

result = int(numberList[0])
output = result + 0
print ("The result is " + str(output) + ".")
print ("Goodbye.")




