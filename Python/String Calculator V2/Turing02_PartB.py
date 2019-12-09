equationInput = str(input("Please enter an arithmetic expression: ")) 

equation = ""

numberList = ["1","2","3","4","5","6","7","8","9","0"]
operators = ["+", "-"]

validInput = numberList + operators

equationList = []
operatorList = ["+"]
tempNum = ""
num = ""
lastOp = -1

inputLen = len(equationInput)

if inputLen == 0: # Checks for empty string
    print("Empty string")
    exit()
        
for check in range(inputLen): # Checks for erroneous and invalid inputs
    if (equationInput[check]) not in validInput:
        print ("Invalid expression")
        exit()
    elif equationInput[-1] in operators:
        print ("Invalid expression")
        exit()
    else:
        check += 1

i = 0
while i != inputLen: # Solving the multiple operator symbols
    if equationInput[i] in numberList:
        equation = str(equation) + str(equationInput[i])
        i += 1
        
    elif equationInput[i] == "+":
        if equationInput[i+1] in operators:
            i += 1
        else:
            equation = str(equation) + str(equationInput[i])
            i += 1

    elif equationInput[i] == "-":
        pos = i + 1
        flip = 1

        for i in range(i, int(inputLen)):
            
            if equationInput[i] == "-":
                flip = flip *-1
            elif equationInput[i] == "+":
                flip = flip
            else:
                flip = flip
                break
      
        if flip == -1:
            equation = str(equation) + ("-")
        else:
            equation = str(equation) + ("+")

firstNumNeg = False # Checking to see if the first operator is positive or negative
if equation[0] == "+":
    firstNumNeg = False
    equation = equation[1:len(equation)]
elif equation[0] == "-":
    firstNumNeg = True
    equation = equation[1:len(equation)]
else:
    pass

equationLen = len(equation) # The length of the string
lastIndex = equationLen - 1 # The last number in the string
    
x = 0
while x != equationLen: # Splitting the equation into a number and operator list
    if equation[x] in numberList:
        tempNum = str(tempNum) + str(equation[x])
        x+=1
    elif equation[x] in operators:
        num = tempNum
        tempNum = ""
        equationList.append(num)
        operatorList.append(equation[x])
        lastOp = x
        x+=1
    else:
        finalResult = equation[x]
        break

num = equation[lastOp+1:equationLen] # Adding numbers after last operator onto the list
equationList.append(num)

if firstNumNeg == True: # Making it negative if the first operator was negative
    tempOpList = []
    tempOpList.append("-")
    tempOpList = tempOpList + operatorList[1::]
    operatorList = tempOpList
else:
    pass

result = 0 # Solving the equation using the two lists
for j in range(len(equationList)):
    if operatorList[j] == "+":
        result = result + int(equationList[j])
    elif operatorList[j] == "-":
        result = result - int(equationList[j])

finalResult = result + 0 # Getting rid of 0's if user enters 001

print ("The result is " + str(finalResult) + ".")
print ("Goodbye.")
