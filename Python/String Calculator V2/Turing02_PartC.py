equation = str(input("Please enter an arithmetic expression: ")) 

numberList = ["1","2","3","4","5","6","7","8","9","0"]
operators = ["+", "-","*"]

validInput = numberList + operators

equationList = []
operatorList = ["+"]
tempNum = ""
num = ""
lastOp = -1

equationLen = len(equation) # The length of the string
lastIndex = equationLen - 1 # The last number in the string

if equationLen == 0: # Checking if its an empty string
    print("Empty string")
    exit()

for check in range(equationLen): # Checks for erroneous inputs and invalid input
    if (equation[check]) not in validInput:
        print ("Invalid expression")
        exit()
    elif equation[-1] in operators:
        print ("Invalid expression")
        exit()
    elif equation[0] in operators:
        print ("Invalid expression")
        exit()
    elif (equation[check]) in operators and (equation[check+1]) in operators:
        print ("Invalid expression")
        exit()
    else:
        check += 1

for i in range(equationLen): # Splitting the equation into a number and operator list

    if equation[i] in numberList:
        tempNum = str(tempNum) + str(equation[i])
        
    elif equation[i] in operators:
        num = tempNum
        tempNum = ""
        equationList.append(num)
        operatorList.append(equation[i])
        lastOp = i

num = equation[lastOp+1:equationLen] # Adding numbers after last operator onto the list
equationList.append(num)

j = 0 # Checks for the times symbol and then times the two list items together and then replaces the list with the new value, then removes times operator
while j != (len(equationList)):
    tempList = []
    timesAns = 0
    timesList = []
    
    if operatorList[j] == "*":
        timesAns = int(equationList[j]) * int(equationList[j-1])
        timesList.append(timesAns)
        tempList = operatorList[0:j]
        operatorList = tempList + operatorList[j+1::]
        tempList = equationList[0:(j-1)]
        equationList = tempList + timesList + equationList[j+1::]
        j = 0
    else:
        j += 1
        
result = 0

i = 0
for i in range(len(equationList)): # Solving the equation using the two lists
    if operatorList[i] == "+":
        result = result + int(equationList[i])
    else:
        result = result - int(equationList[i])

finalResult = result + 0 # Getting rid of 0's if user enters 001...

print ("The result is " + str(finalResult) + ".")
print ("Goodbye.")
