import tkinter as tk
import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class CalcGUI:
    def __init__(self):
        # Definition of the root window, size, and title
        self.root = ctk.CTk()
        self.root.geometry("450x400")
        self.root.title("Calculator")

        # Creation of the mainFrame that all widgets will be placed in
        self.mainFrame = ctk.CTkFrame(self.root)
        self.basicCalc() # Calculator will always start in basic mode
        self.mainFrame.pack(padx=5, pady=5)

    # Public method launch
    # 
    # Used to launch the actual GUI after setup is completed.
    def launch(self):
        self.root.mainloop() # launch program

    # Public method setController
    # Arguments:
    #   - controller: A calcController object
    #
    # Sets the global controller for this calculator GUI.
    def setController(self, controller):
        self.controller = controller

    # Public method basicCalc
    #
    # Populates the main window with widget for a basic calculator
    def basicCalc(self):
        self.buttonWidth = 75
        self.fontSize = 35

        # Creation of the operation box at the top of the window.
        self.opBox = ctk.CTkEntry(self.mainFrame, height=75, width=350, justify="right", font=("TkDefaultFont", self.fontSize))
        self.opBox.grid(column=0, row=0, columnspan=4, pady=5)

        # Creation of the operation buttons along the top and side of keypad
        self.subButton = ctk.CTkButton(self.mainFrame, text="-", width=self.buttonWidth, font=("TkDefaultFont", self.fontSize))
        self.subButton.grid(column=3, row=1, pady=5)

        self.multButton = ctk.CTkButton(self.mainFrame, text="*", width=self.buttonWidth, font=("TkDefaultFont", self.fontSize))
        self.multButton.grid(column=2, row=1, pady=5)

        self.divideButton = ctk.CTkButton(self.mainFrame, text="/", width=self.buttonWidth, font=("TkDefaultFont", self.fontSize))
        self.divideButton.grid(column=1, row=1, pady=5)

        self.addButton = ctk.CTkButton(self.mainFrame, text="+", width=self.buttonWidth, font=("TkDefaultFont", self.fontSize))
        self.addButton.grid(column=3, row=2, rowspan=2, pady=5, sticky="ns")

        self.equalButton = ctk.CTkButton(self.mainFrame, text="=", width=self.buttonWidth, font=("TkDefaultFont", self.fontSize))
        self.equalButton.grid(column=3, row=4, rowspan=2, pady=5, sticky="ns")

        self.clearButton = ctk.CTkButton(self.mainFrame, text="CE", width=self.buttonWidth, font=("TkDefaultFont", self.fontSize))
        self.clearButton.grid(column=0, row=1, pady=5)

        # Creation of the number buttons on the keypad 0-9
        self.sevenButton = ctk.CTkButton(self.mainFrame, text="7", width=self.buttonWidth, font=("TkDefaultFont", self.fontSize))
        self.sevenButton.grid(column=0, row=2, pady=5)

        self.eightButton = ctk.CTkButton(self.mainFrame, text="8", width=self.buttonWidth, font=("TkDefaultFont", self.fontSize))
        self.eightButton.grid(column=1, row=2, pady=5)

        self.nineButton = ctk.CTkButton(self.mainFrame, text="9", width=self.buttonWidth, font=("TkDefaultFont", self.fontSize))
        self.nineButton.grid(column=2, row=2, pady=5)

        self.fourButton = ctk.CTkButton(self.mainFrame, text="4", width=self.buttonWidth, font=("TkDefaultFont", self.fontSize))
        self.fourButton.grid(column=0, row=3, pady=5)

        self.fiveButton = ctk.CTkButton(self.mainFrame, text="5", width=self.buttonWidth, font=("TkDefaultFont", self.fontSize))
        self.fiveButton.grid(column=1, row=3, pady=5)

        self.sixButton = ctk.CTkButton(self.mainFrame, text="6", width=self.buttonWidth, font=("TkDefaultFont", self.fontSize))
        self.sixButton.grid(column=2, row=3, pady=5)

        self.oneButton = ctk.CTkButton(self.mainFrame, text="1", width=self.buttonWidth, font=("TkDefaultFont", self.fontSize))
        self.oneButton.grid(column=0, row=4, pady=5)

        self.twoButton = ctk.CTkButton(self.mainFrame, text="2", width=self.buttonWidth, font=("TkDefaultFont", self.fontSize))
        self.twoButton.grid(column=1, row=4, pady=5)

        self.threeButton = ctk.CTkButton(self.mainFrame, text="3", width=self.buttonWidth, font=("TkDefaultFont", self.fontSize))
        self.threeButton.grid(column=2, row=4, pady=5)

        self.zeroButton = ctk.CTkButton(self.mainFrame, text="0", width=self.buttonWidth, font=("TkDefaultFont", self.fontSize))
        self.zeroButton.grid(column=1, row=5, pady=5)