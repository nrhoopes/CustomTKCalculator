import tkinter as tk
import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class CalcGUI():
    def __init__(self):
        self.root = ctk.CTk()
        self.root.geometry("400x550")
        self.root.title("Calculator")

    # Public method launch
    # 
    # Used to launch the actual GUI after setup is completed.
    def launch(self):
        self.root.mainloop() # launch program