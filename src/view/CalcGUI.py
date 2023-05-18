import tkinter as tk
import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class CalcGUI():
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

    # Public method basicCalc
    #
    # Populates the main window with widget for a basic calculator
    def basicCalc(self):
        self.buttonWidth = 75

        # Creation of the operation box at the top of the window.
        self.opBox = ctk.CTkEntry(self.mainFrame, height=75, width=350, justify="right", font=("TkDefaultFont", 30))
        self.opBox.grid(column=0, row=0, columnspan=4, pady=5)

        
        self.subButton = ctk.CTkButton(self.mainFrame, text="-", width=self.buttonWidth, font=("TkDefaultFont", 30))
        self.subButton.grid(column=3, row=1, pady=5)

        self.multButton = ctk.CTkButton(self.mainFrame, text="*", width=self.buttonWidth, font=("TkDefaultFont", 30))
        self.multButton.grid(column=2, row=1, pady=5)

        self.divideButton = ctk.CTkButton(self.mainFrame, text="/", width=self.buttonWidth * 2 + 10, font=("TkDefaultFont", 30))
        self.divideButton.grid(column=0, row=1, columnspan=2, pady=5)

        self.addButton = ctk.CTkButton(self.mainFrame, text="+", width=self.buttonWidth, font=("TkDefaultFont", 30))
        self.addButton.grid(column=3, row=2, rowspan=2, pady=5, sticky="ns")

        self.equalButton = ctk.CTkButton(self.mainFrame, text="=", width=self.buttonWidth, font=("TkDefaultFont", 30))
        self.equalButton.grid(column=3, row=4, rowspan=2, pady=5, sticky="ns")


        self.sevenButton = ctk.CTkButton(self.mainFrame, text="7", width=self.buttonWidth, font=("TkDefaultFont", 30))
        self.sevenButton.grid(column=0, row=2, pady=5)

        self.eightButton = ctk.CTkButton(self.mainFrame, text="8", width=self.buttonWidth, font=("TkDefaultFont", 30))
        self.eightButton.grid(column=1, row=2, pady=5)

        self.nineButton = ctk.CTkButton(self.mainFrame, text="9", width=self.buttonWidth, font=("TkDefaultFont", 30))
        self.nineButton.grid(column=2, row=2, pady=5)

        self.fourButton = ctk.CTkButton(self.mainFrame, text="4", width=self.buttonWidth, font=("TkDefaultFont", 30))
        self.fourButton.grid(column=0, row=3, pady=5)

        self.fiveButton = ctk.CTkButton(self.mainFrame, text="5", width=self.buttonWidth, font=("TkDefaultFont", 30))
        self.fiveButton.grid(column=1, row=3, pady=5)

        self.sixButton = ctk.CTkButton(self.mainFrame, text="6", width=self.buttonWidth, font=("TkDefaultFont", 30))
        self.sixButton.grid(column=2, row=3, pady=5)

        self.oneButton = ctk.CTkButton(self.mainFrame, text="1", width=self.buttonWidth, font=("TkDefaultFont", 30))
        self.oneButton.grid(column=0, row=4, pady=5)

        self.twoButton = ctk.CTkButton(self.mainFrame, text="2", width=self.buttonWidth, font=("TkDefaultFont", 30))
        self.twoButton.grid(column=1, row=4, pady=5)

        self.threeButton = ctk.CTkButton(self.mainFrame, text="3", width=self.buttonWidth, font=("TkDefaultFont", 30))
        self.threeButton.grid(column=2, row=4, pady=5)

        self.zeroButton = ctk.CTkButton(self.mainFrame, text="0", width=self.buttonWidth, font=("TkDefaultFont", 30))
        self.zeroButton.grid(column=1, row=5, pady=5)