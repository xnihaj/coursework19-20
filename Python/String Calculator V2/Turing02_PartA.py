equation = str(input("Please enter an arithmetic expression: ")) 

numberList = ["1","2","3","4","5","6","7","8","9","0"]
operators = ["+", "-"]
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

result = 0 # Solving the equation using the two lists
for j in range(len(equationList)):
    if operatorList[j] == "+":
        result = result + int(equationList[j])
    elif operatorList[j] == "-":
        result = result - int(equationList[j])

finalResult = result + 0 # Getting rid of 0's if user enters 001...

print ("The result is " + str(finalResult) + ".")
print ("Goodbye.")
