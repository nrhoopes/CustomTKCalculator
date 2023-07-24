
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
        self.evaluate(mem + op)
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
        
        # List of possible operators the calculator supports
        operators = ["+", "-", "/", "*"]

        for i in expression:
            if i in operators:
                operatorCount += 1
                if currentOperand:
                    operandCount += 1
                    currentOperand = False
                pass
            elif i.isnumeric() or i == ".":
                currentOperand = True
                pass
        # Fence post - There won't be another operator to count the last operand, so
        # double check if we need to add another to the operandCount.
        if currentOperand:
            operandCount += 1

        if (operatorCount + 1) == operandCount:
            return True
        else:
            return False

