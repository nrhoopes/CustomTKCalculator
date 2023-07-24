
class calcController:
    def __init__(self, ui):
        self.ui = ui
        self.calcMode = None

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

    def sciEvaluate(self, mem, op):
        self.evaluate(mem + op)
        currentMem = self.ui.memEntry.get()

        self.ui.memEntry.configure(state="normal")
        self.ui.memEntry.insert(len(currentMem), op)
        self.ui.memEntry.configure(state="disabled")


    def sciCalcInsert(self, op):
        currentOperand = self.ui.opBox.get()
        currentMem = self.ui.memEntry.get()

        self.ui.memEntry.configure(state="normal")
        self.ui.memEntry.insert(len(currentMem), currentOperand + op)
        self.ui.memEntry.configure(state="disabled")

        self.ui.opBox.configure(state="normal")
        self.ui.opBox.delete(0, len(self.ui.opBox.get()))
        self.ui.opBox.configure(state="disabled")

        self.ui.clearButton.configure(text="C")

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

