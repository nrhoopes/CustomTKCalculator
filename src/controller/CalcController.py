
class calcController:
    def __init__(self, ui):
        self.ui = ui

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

    
    def isFullExpression(self, expression):
        operatorCount = 0
        operandCount = 0
        currentOperand = False
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
        if currentOperand:
            operandCount += 1

        if (operatorCount + 1) == operandCount:
            return True
        else:
            return False

