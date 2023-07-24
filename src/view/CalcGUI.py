import tkinter as tk
import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class CalcGUI:
    def __init__(self):
        # Definition of the root window, size, and title
        self.root = ctk.CTk()
        self.root.title("Calculator")

        self.buttonWidth = 75
        self.fontSize = 35
        self.font = "TkDefaultFont"

        # # # Menu Creation # # #
        self.menubar = tk.Menu(self.root)
        self.calculatorsMenu = tk.Menu(self.menubar, tearoff=0)

        self.calculatorsMenu.add_command(label="Basic Calculator", command=lambda: self.basicCalc())
        self.calculatorsMenu.add_command(label="Scientific Calculator", command=lambda: self.sciCalc())

        self.menubar.add_cascade(label="Switch Calculator", menu=self.calculatorsMenu)
        self.root.configure(menu=self.menubar)

        # Creation of the mainFrame that all widgets will be placed in
        self.mainFrame = ctk.CTkFrame(self.root)
        self.mainFrame.pack()

    # Public method launch
    # 
    # Used to launch the actual GUI after setup is completed.
    def launch(self):
        # self.basicCalc() # Calculator will always start in basic mode
        self.sciCalc() # REMOVE
        self.root.mainloop() # launch program

    # Public method setController
    # Arguments:
    #   - controller: A calcController object
    #
    # Sets the global controller for this calculator GUI.
    def setController(self, controller):
        self.controller = controller

    # Public method insertToOpBox
    # Arguments:
    #   - string: a string to be inserted into the operation box
    #
    # Unlocks the operation box for editing, places string in, and closes the box again.
    def insertToOpBox(self, string):
        self.opBox.configure(state="normal")
        self.opBox.insert(len(self.opBox.get()), string)
        self.opBox.configure(state="disabled")

    # Public method displayToOpBox
    # Arguments:
    #   - string: a string to be displayed into the operation box
    #
    # As opposed to inserting to the end of the operation box, displayToOpBox will
    # instead clear the screen and then insert the given string onto the screen.
    def displayToOpBox(self, string):
        self.clearScreen()
        self.insertToOpBox(string)

    # Public method clearScreen
    #
    # Used to clear the screen of the calculator.
    def clearScreen(self):
        self.opBox.configure(state="normal")
        self.opBox.delete(0, len(self.opBox.get()))
        self.opBox.configure(state="disabled")
        if self.clearButton.cget('text') == "CE":
            self.opBox.configure(state="normal")
            self.opBox.delete(0, len(self.opBox.get()))
            self.opBox.configure(state="disabled")
            
            if self.controller.calcMode == "sci":
                self.memEntry.configure(state="normal")
                self.memEntry.delete(0, tk.END)
                self.memEntry.configure(state="disabled")
        self.clearButton.configure(text="CE")

    # Public method removeLast
    #
    # Used to remove the most recent digit or character typed into the operation box.
    # Essentially a backspace button.
    def removeLast(self):
        self.opBox.configure(state="normal")
        self.opBox.delete(len(self.opBox.get()) - 1, len(self.opBox.get()))
        self.opBox.configure(state="disabled")

    # Private method __clearFrame
    # Arguments:
    #   - frame: The given frame that needs to be cleared.
    # 
    # Clear every widget from the frame passed in.
    # Window will remain open, assure you fill with something afterwards.
    def __clearFrame(self, frame):
        for widgets in frame.winfo_children():
            widgets.destroy()

    # Private method __shortcut
    # Arguments:
    #   - event: A <KeyPress> event
    #
    # __shortcut will evaluate every keypress from the user and will decide if
    # the button the user presses is allowed.  If it is, it will either add the
    # key to the operation box or will perform the special function. Otherwise,
    # nothing will happen.
    def __shortcut(self, event):
        if event.char.isnumeric() or event.char in ["/", "*", "-", "+", "."]:
            self.insertToOpBox(event.char)
        elif event.keysym == "BackSpace":
            self.removeLast()
        elif event.keysym == "Return" or event.keysym == "KP_Enter":
            self.controller.evaluate(self.opBox.get())

    def __sciShortcut(self, event):
        if event.char.isnumeric():
            self.insertToOpBox(event.char)
        elif event.char in  ["/", "*", "-", "+", "."]:
            self.controller.sciCalcInsert(event.char)
        elif event.keysym == "BackSpace":
            self.removeLast()
        elif event.keysym == "Return" or event.keysym == "KP_Enter":
            self.controller.sciEvaluate(self.memEntry.get(), self.opBox.get())

    # Public method basicCalc
    #
    # Populates the main window with widget for a basic calculator
    # Currently the basic calculator grid looks like this:
    #
    #     0  1  2  3
    #   --------------
    # 0 | [ screen ] |
    # 1 | ce %  <  / |
    # 2 | 7  8  9  * |
    # 3 | 4  5  6  - |
    # 4 | 1  2  3  + |
    # 5 |    0  .  = |
    #   --------------
    def basicCalc(self):
        self.controller.calcMode = "basic"
        self.root.geometry("450x400")
        self.__clearFrame(self.mainFrame)

        # Creation of the operation box at the top of the window.
        self.opBox = ctk.CTkEntry(self.mainFrame, height=75, width=350, justify="right", font=(self.font, self.fontSize), state="disabled")
        self.opBox.grid(column=0, row=0, columnspan=4, pady=5)

        self.root.bind("<KeyPress>", self.__shortcut)

        # Creation of the operation buttons along the top and side of keypad
        self.clearButton = ctk.CTkButton(self.mainFrame, text="CE", width=self.buttonWidth, font=(self.font, self.fontSize), command=self.clearScreen)
        self.clearButton.grid(column=0, row=1, pady=5)

        self.percentButton = ctk.CTkButton(self.mainFrame, text="%", width=self.buttonWidth, font=(self.font, self.fontSize), command=lambda: self.controller.convertPercent(self.opBox.get()))
        self.percentButton.grid(column=1, row=1, pady=5)
        
        self.backButton = ctk.CTkButton(self.mainFrame, text="<-", width=self.buttonWidth, font=(self.font, self.fontSize), command=self.removeLast)
        self.backButton.grid(column=2, row=1, pady=5)

        self.divideButton = ctk.CTkButton(self.mainFrame, text="/", width=self.buttonWidth, font=(self.font, self.fontSize), command=lambda: self.insertToOpBox("/"))
        self.divideButton.grid(column=3, row=1, pady=5)

        self.multButton = ctk.CTkButton(self.mainFrame, text="*", width=self.buttonWidth, font=(self.font, self.fontSize), command=lambda: self.insertToOpBox("*"))
        self.multButton.grid(column=3, row=2, pady=5)

        self.subButton = ctk.CTkButton(self.mainFrame, text="-", width=self.buttonWidth, font=(self.font, self.fontSize), command=lambda: self.insertToOpBox("-"))
        self.subButton.grid(column=3, row=3, pady=5)

        self.addButton = ctk.CTkButton(self.mainFrame, text="+", width=self.buttonWidth, font=(self.font, self.fontSize), command=lambda: self.insertToOpBox("+"))
        self.addButton.grid(column=3, row=4, pady=5, sticky="ns")

        self.equalButton = ctk.CTkButton(self.mainFrame, text="=", width=self.buttonWidth, font=(self.font, self.fontSize), command=lambda: self.controller.evaluate(self.opBox.get()))
        self.equalButton.grid(column=3, row=5, pady=5, sticky="ns")

        # Creation of the number buttons on the keypad 0-9
        self.sevenButton = ctk.CTkButton(self.mainFrame, text="7", width=self.buttonWidth, font=(self.font, self.fontSize), command=lambda: self.insertToOpBox("7"))
        self.sevenButton.grid(column=0, row=2, pady=5)

        self.eightButton = ctk.CTkButton(self.mainFrame, text="8", width=self.buttonWidth, font=(self.font, self.fontSize), command=lambda: self.insertToOpBox("8"))
        self.eightButton.grid(column=1, row=2, pady=5)

        self.nineButton = ctk.CTkButton(self.mainFrame, text="9", width=self.buttonWidth, font=(self.font, self.fontSize), command=lambda: self.insertToOpBox("9"))
        self.nineButton.grid(column=2, row=2, pady=5)

        self.fourButton = ctk.CTkButton(self.mainFrame, text="4", width=self.buttonWidth, font=(self.font, self.fontSize), command=lambda: self.insertToOpBox("4"))
        self.fourButton.grid(column=0, row=3, pady=5)

        self.fiveButton = ctk.CTkButton(self.mainFrame, text="5", width=self.buttonWidth, font=(self.font, self.fontSize), command=lambda: self.insertToOpBox("5"))
        self.fiveButton.grid(column=1, row=3, pady=5)

        self.sixButton = ctk.CTkButton(self.mainFrame, text="6", width=self.buttonWidth, font=(self.font, self.fontSize), command=lambda: self.insertToOpBox("6"))
        self.sixButton.grid(column=2, row=3, pady=5)

        self.oneButton = ctk.CTkButton(self.mainFrame, text="1", width=self.buttonWidth, font=(self.font, self.fontSize), command=lambda: self.insertToOpBox("1"))
        self.oneButton.grid(column=0, row=4, pady=5)

        self.twoButton = ctk.CTkButton(self.mainFrame, text="2", width=self.buttonWidth, font=(self.font, self.fontSize), command=lambda: self.insertToOpBox("2"))
        self.twoButton.grid(column=1, row=4, pady=5)

        self.threeButton = ctk.CTkButton(self.mainFrame, text="3", width=self.buttonWidth, font=(self.font, self.fontSize), command=lambda: self.insertToOpBox("3"))
        self.threeButton.grid(column=2, row=4, pady=5)

        self.zeroButton = ctk.CTkButton(self.mainFrame, text="0", width=self.buttonWidth, font=(self.font, self.fontSize), command=lambda: self.insertToOpBox("0"))
        self.zeroButton.grid(column=1, row=5, pady=5)

        # Creation of the decimal button
        self.decimalButton = ctk.CTkButton(self.mainFrame, text=".", width=self.buttonWidth, font=(self.font, self.fontSize), command=lambda: self.insertToOpBox("."))
        self.decimalButton.grid(column=2, row=5, pady=5)

    # Public method sciCalc
    #
    # Populates the main window with widgets for the scientific calculator
    def sciCalc(self):
        self.__clearFrame(self.mainFrame)
        self.root.geometry("550x620")

        self.controller.calcMode = "sci"

        self.screenFrame = ctk.CTkFrame(self.mainFrame)

        self.memEntry = ctk.CTkEntry(self.screenFrame, state="disabled", justify='right')
        self.memEntry.grid(column=2, row=0, columnspan=3, sticky="esw")

        # Creation of the operation box at the top of the window.
        self.opBox = ctk.CTkEntry(self.screenFrame, height=75, width=500, justify="right", font=(self.font, self.fontSize), state="disabled")
        self.opBox.grid(column=0, row=1, columnspan=5)

        self.screenFrame.grid(column=0, row=0, columnspan=5)

        self.root.bind("<KeyPress>", self.__sciShortcut)

        # Creation of the operation buttons along the top and side of keypad
        self.clearButton = ctk.CTkButton(self.mainFrame, text="CE", width=self.buttonWidth, font=(self.font, self.fontSize), command=self.clearScreen)
        self.clearButton.grid(column=3, row=1, pady=5)

        self.percentButton = ctk.CTkButton(self.mainFrame, text="%", width=self.buttonWidth, font=(self.font, self.fontSize), command=lambda: self.controller.convertPercent(self.opBox.get()))
        self.percentButton.grid(column=3, row=2, pady=5)

        self.piButton = ctk.CTkButton(self.mainFrame, text="pi", width=self.buttonWidth, font=(self.font, self.fontSize), command=lambda: self.insertToOpBox("3.14"))
        self.piButton.grid(column=2, row=2, pady=5)

        self.absButton = ctk.CTkButton(self.mainFrame, text="|x|", width=self.buttonWidth, font=(self.font, self.fontSize), command=lambda: print("abs()"))
        self.absButton.grid(column=1, row=2, pady=5)
        
        self.modButton = ctk.CTkButton(self.mainFrame, text="mod", width=self.buttonWidth, font=(self.font, self.fontSize), command=lambda: self.insertToOpBox(" % "))
        self.modButton.grid(column=4, row=2, pady=5)

        self.factorialButton = ctk.CTkButton(self.mainFrame, text="n!", width=self.buttonWidth, font=(self.font, self.fontSize), command=lambda: self.insertToOpBox("!"))
        self.factorialButton.grid(column=3, row=3, pady=5)

        self.closeParenButton = ctk.CTkButton(self.mainFrame, text=")", width=self.buttonWidth, font=(self.font, self.fontSize), command=lambda: self.insertToOpBox(")"))
        self.closeParenButton.grid(column=2, row=3, pady=5)

        self.openParenButton = ctk.CTkButton(self.mainFrame, text="(", width=self.buttonWidth, font=(self.font, self.fontSize), command=lambda: self.insertToOpBox("("))
        self.openParenButton.grid(column=1, row=3, pady=5)

        self.backButton = ctk.CTkButton(self.mainFrame, text="<-", width=self.buttonWidth, font=(self.font, self.fontSize), command=self.removeLast)
        self.backButton.grid(column=4, row=1, pady=5)

        self.divideButton = ctk.CTkButton(self.mainFrame, text="/", width=self.buttonWidth, font=(self.font, self.fontSize), command=lambda: self.controller.sciCalcInsert("/"))
        self.divideButton.grid(column=4, row=3, pady=5)

        self.multButton = ctk.CTkButton(self.mainFrame, text="*", width=self.buttonWidth, font=(self.font, self.fontSize), command=lambda: self.controller.sciCalcInsert("*"))
        self.multButton.grid(column=4, row=4, pady=5)

        self.subButton = ctk.CTkButton(self.mainFrame, text="-", width=self.buttonWidth, font=(self.font, self.fontSize), command=lambda: self.controller.sciCalcInsert("-"))
        self.subButton.grid(column=4, row=5, pady=5)

        self.addButton = ctk.CTkButton(self.mainFrame, text="+", width=self.buttonWidth, font=(self.font, self.fontSize), command=lambda: self.controller.sciCalcInsert("+"))
        self.addButton.grid(column=4, row=6, pady=5, sticky="ns")

        self.equalButton = ctk.CTkButton(self.mainFrame, text="=", width=self.buttonWidth, font=(self.font, self.fontSize), command=lambda: self.controller.sciEvaluate(self.memEntry.get(), self.opBox.get()))
        self.equalButton.grid(column=4, row=7, pady=5, sticky="ns")

        # Creation of the number buttons on the keypad 0-9
        self.sevenButton = ctk.CTkButton(self.mainFrame, text="7", width=self.buttonWidth, font=(self.font, self.fontSize), command=lambda: self.insertToOpBox("7"))
        self.sevenButton.grid(column=1, row=4, pady=5)

        self.eightButton = ctk.CTkButton(self.mainFrame, text="8", width=self.buttonWidth, font=(self.font, self.fontSize), command=lambda: self.insertToOpBox("8"))
        self.eightButton.grid(column=2, row=4, pady=5)

        self.nineButton = ctk.CTkButton(self.mainFrame, text="9", width=self.buttonWidth, font=(self.font, self.fontSize), command=lambda: self.insertToOpBox("9"))
        self.nineButton.grid(column=3, row=4, pady=5)

        self.fourButton = ctk.CTkButton(self.mainFrame, text="4", width=self.buttonWidth, font=(self.font, self.fontSize), command=lambda: self.insertToOpBox("4"))
        self.fourButton.grid(column=1, row=5, pady=5)

        self.fiveButton = ctk.CTkButton(self.mainFrame, text="5", width=self.buttonWidth, font=(self.font, self.fontSize), command=lambda: self.insertToOpBox("5"))
        self.fiveButton.grid(column=2, row=5, pady=5)

        self.sixButton = ctk.CTkButton(self.mainFrame, text="6", width=self.buttonWidth, font=(self.font, self.fontSize), command=lambda: self.insertToOpBox("6"))
        self.sixButton.grid(column=3, row=5, pady=5)

        self.oneButton = ctk.CTkButton(self.mainFrame, text="1", width=self.buttonWidth, font=(self.font, self.fontSize), command=lambda: self.insertToOpBox("1"))
        self.oneButton.grid(column=1, row=6, pady=5)

        self.twoButton = ctk.CTkButton(self.mainFrame, text="2", width=self.buttonWidth, font=(self.font, self.fontSize), command=lambda: self.insertToOpBox("2"))
        self.twoButton.grid(column=2, row=6, pady=5)

        self.threeButton = ctk.CTkButton(self.mainFrame, text="3", width=self.buttonWidth, font=(self.font, self.fontSize), command=lambda: self.insertToOpBox("3"))
        self.threeButton.grid(column=3, row=6, pady=5)

        self.zeroButton = ctk.CTkButton(self.mainFrame, text="0", width=self.buttonWidth, font=(self.font, self.fontSize), command=lambda: self.insertToOpBox("0"))
        self.zeroButton.grid(column=2, row=7, pady=5)

        self.flipButton = ctk.CTkButton(self.mainFrame, text="+/-", width=self.buttonWidth, font=(self.font, self.fontSize), command=lambda: print("Flip sign"))
        self.flipButton.grid(column=1, row=7, pady=5)

        self.secondButton = ctk.CTkButton(self.mainFrame, fg_color="white", text_color="blue", text="2nd", width=self.buttonWidth, font=(self.font, self.fontSize), command=lambda: print("2nd!"))
        self.secondButton.grid(column=0, row=2, pady=5)

        self.sqrButton = ctk.CTkButton(self.mainFrame, text="x^2", width=self.buttonWidth, font=(self.font, self.fontSize), command=lambda: print("sqr"))
        self.sqrButton.grid(column=0, row=3, pady=5)

        self.sqrtButton = ctk.CTkButton(self.mainFrame, text="sqrt", width=self.buttonWidth, font=(self.font, self.fontSize), command=lambda: print("sqrt"))
        self.sqrtButton.grid(column=0, row=4, pady=5)

        self.xpowyButton = ctk.CTkButton(self.mainFrame, text="x^y", width=self.buttonWidth, font=(self.font, self.fontSize), command=lambda: print("x^y"))
        self.xpowyButton.grid(column=0, row=5, pady=5)

        self.tenxButton = ctk.CTkButton(self.mainFrame, text="10^x", width=self.buttonWidth, font=(self.font, self.fontSize), command=lambda: print("10x"))
        self.tenxButton.grid(column=0, row=6, pady=5)

        self.logButton = ctk.CTkButton(self.mainFrame, text="log", width=self.buttonWidth, font=(self.font, self.fontSize), command=lambda: print("log"))
        self.logButton.grid(column=0, row=7, pady=5)

        # Creation of the decimal button
        self.decimalButton = ctk.CTkButton(self.mainFrame, text=".", width=self.buttonWidth, font=(self.font, self.fontSize), command=lambda: self.insertToOpBox("."))
        self.decimalButton.grid(column=3, row=7, pady=5)
