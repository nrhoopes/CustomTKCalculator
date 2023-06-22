
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
        self.ui.clearScreen()
        self.ui.insertToOpBox(float(number)/100)

    def evaluate(self, expression):
        evaluation = str(eval(expression))
        self.ui.displayToOpBox(evaluation)

