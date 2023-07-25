import math

class calcController:
    def __init__(self, ui):
        self.ui = ui
        self.calcMode = None
        self.answerInBox = False

    # Public method convertPercent
    # Arguments:
    #   - number: the number to convert to a percentage
    #
    # Will accept a number, convert it to a percentage and then will return the percentage
    # and place it into the operation box.
    def convertPercent(self, number):
        percentDec = ""
        for i in range(len(number) - 1, -1, -1):
            if number[i].isnumeric():
                percentDec = number[i] + percentDec
                number = number[0:len(number)-1]
            else:
                break
        if percentDec != "":
            self.ui.clearScreen()
            self.ui.insertToOpBox(number + str(float(percentDec)/100))

    # Public method evaluate
    # Arguments:
    #   - expression: an expression that is input into the calculator in string form.
    #
    # Will evaluate the expression, cast it to a string, and then tell the opBox to display that string.
    def evaluate(self, expression):
        # print(self.isFullExpression(expression))
        if self.isFullExpression(expression):
            evaluation = str(eval(expression))
            self.ui.displayToOpBox(evaluation)

    # Public method sciEvaluate
    # Arguments:
    #   - mem: The current memory saved in the scientific calculator's memEntry
    #   - op: The current value in the opBox
    #
    # Allows for the program to build the full equation and then evalute it as all
    # the information will not be in the same box in the scientific calculator.
    # Still utilizes evaluate().  Will also keep the memEntry up to date
    def sciEvaluate(self, mem, op):
        # If we are doing a logarithm we need to parse out the format and find the
        # numbers that the user wants to use to calculate.
        if "log[" in mem:
            currentMem = self.ui.memEntry.get()
            numIndex = mem.index("[") + 1
            num = ""
            newOp = ""
            for i in range(numIndex, len(mem), 1):
                if mem[i] == "(":
                    continue
                elif mem[i].isnumeric():
                    num += mem[i]
                elif mem[i] == ")":
                    break
                else:
                    break
            for i in range(0, len(op), 1):
                if op[i].isnumeric() or op[i] == ".":
                    newOp += op[i]
            
            self.ui.memEntry.configure(state="normal")
            self.ui.memEntry.insert(len(currentMem), op + "]")
            self.ui.memEntry.configure(state="disabled")

            self.ui.clearScreen()
            self.ui.insertToOpBox(str(math.log(int(num), int(newOp))))

            self.answerInBox = True
        else:
            self.evaluate(mem + op)
            if self.isFullExpression(mem + op):
                currentMem = self.ui.memEntry.get()

                self.ui.memEntry.configure(state="normal")
                self.ui.memEntry.insert(len(currentMem), op)
                self.ui.memEntry.configure(state="disabled")

                self.answerInBox = True

    # Public method sciCalcInsert
    # Arguments:
    #   - op: The operation to insert into the memEntry
    #
    # Used instead of insertIntoOpBox as you need to also insert the equation into
    # the memEntry and clear the opBox.  This is used primarily for operations (+, *, etc..)
    # It will take whatever is currently in the memEntry and add on the operator and the operand
    # in the memEntry and clear the opBox.
    def sciCalcInsert(self, op):
        currentOperand = self.ui.opBox.get()
        currentMem = self.ui.memEntry.get()

        if self.answerInBox:
            self.ui.memEntry.configure(state="normal")
            self.ui.memEntry.delete(0, len(self.ui.memEntry.get()))
            self.ui.memEntry.configure(state="disabled")
            currentMem = ""

        self.answerInBox = False # If answerInBox was True, it is now False because the answer has been edited.

        self.ui.memEntry.configure(state="normal")
        self.ui.memEntry.insert(len(currentMem), currentOperand + op)
        self.ui.memEntry.configure(state="disabled")

        self.ui.opBox.configure(state="normal")
        self.ui.opBox.delete(0, len(self.ui.opBox.get()))
        self.ui.opBox.configure(state="disabled")

        self.ui.clearButton.configure(text="C")

    # Public method factorial
    # Arguments:
    #   - num: The number to perform a factorial operation on
    #
    # Will take whatever num is passed in, perform a factorial operation on it, and
    # then will erase anything in the opBox and place the answer in.
    def factorial(self, num):
        ans = num * (num - 1)
        for i in range(num - 2, 1, -1):
            ans = ans * i
        self.ui.clearScreen()
        self.ui.insertToOpBox(ans)
    
    # Public method flipSign
    # Arguments:
    #   - num: the number of the sign to flip (string)
    #
    # Will flip the sign of the given num, clear the screen, and place the new value into opBox
    def flipSign(self, num):
        if num != "":
            self.ui.clearScreen()
            self.ui.insertToOpBox(str(int(num) * -1))
            self.answerInBox = False

    # Public method absolute
    # Arguments:
    #   - num: the number to find the absolute value for
    #
    # Will change the opBox's number to be the absolute value of that number
    def absolute(self, num):
        if num != "":
            self.ui.clearScreen()
            self.ui.insertToOpBox(str(abs(int(num))))
            self.answerInBox = False

    # Public method squirt
    # Arguments:
    #   - num: the number to find the sqrt for.
    #
    # "sqrt sounds like squirt".  Finds the sqrt of the given number and 
    # puts it into the opBox.
    def squirt(self, num):
        if num != "":
            self.ui.clearScreen()
            self.ui.insertToOpBox(str(math.sqrt(int(num))))
            self.answerInBox = False

    # Public method squir
    # Arguments:
    #   - num: The number to square
    #
    # Finds the square of the number given and puts it into the opBox.
    def squir(self, num):
        if num != "":
            self.ui.clearScreen()
            self.ui.insertToOpBox(str(int(num) ** 2))
            self.answerInBox = False

    # Public method tenx
    # Arguments:
    #   - num: The number to put 10 to the power of.
    #
    # will find 10^num and return it to the opBox.
    def tenx(self, num):
        if num != "":
            self.ui.clearScreen()
            self.ui.insertToOpBox(str(10 ** int(num)))
            self.ui.memEntry.configure(state="normal")
            if self.answerInBox:
                self.ui.memEntry.delete(0, len(self.ui.memEntry.get()))
            self.ui.memEntry.insert(0, f"10^{num}")
            self.ui.memEntry.configure(state="disabled")

            self.answerInBox = False

    # Public method log
    # Arguments:
    #   - num: The number to format for evaluation later.
    # 
    # Will place "log[num base " into the memEntry, formatted and waiting for a base.
    # Logarithm is calculated in the sciEvaluate function.
    def log(self, num):
        if num != "":
            self.ui.clearScreen()
            self.ui.memEntry.configure(state="normal")
            self.ui.memEntry.delete(0, len(self.ui.memEntry.get()))
            self.ui.memEntry.insert(0, f"log[{num} base ")
            self.ui.memEntry.configure(state="disabled")

    # Public method isFullExpression
    # Arguments:
    #   - expression: An expression string to see if a full expression is present.
    #
    # isFullExpression will return True or False depending on if the passed in expression is an
    # actual and valid expression.  A valid expression is one that is defined as having two
    # operands per operator.
    def isFullExpression(self, expression):
        operatorCount = 0
        operandCount = 0
        currentOperand = False
        lastChar = ""
        
        # List of possible operators the calculator supports
        operators = ["+", "-", "/", "*"]

        for i in expression:
            if i in operators:
                if (lastChar in operators or lastChar == "") and i == "-":
                    lastChar = "pass"
                    continue
                elif lastChar == "*" and i == "*":
                    lastChar = "pass"
                    continue
                operatorCount += 1
                if currentOperand:
                    operandCount += 1
                    currentOperand = False
                lastChar = i
                pass
            elif i.isnumeric() or i == ".":
                currentOperand = True
                pass
        # Fence post - There won't be another operator to count the last operand, so
        # double check if we need to add another to the operandCount.
        if currentOperand:
            operandCount += 1

        if (operatorCount + 1) == operandCount:
            if operandCount == 1 and operatorCount == 0:
                return False
            else:
                return True
        else:
            return False

