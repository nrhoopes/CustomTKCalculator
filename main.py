# main.py is used to tie everything together
from src.view.CalcGUI import CalcGUI # Import view

# Creation of the GUI object
gui = CalcGUI()

# launch the GUI once everything is setup and ready.
gui.launch()