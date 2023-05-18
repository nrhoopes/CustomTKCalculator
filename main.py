# main.py is used to tie everything together
from src.view.CalcGUI import CalcGUI # Import view
from src.controller.CalcController import calcController

# Creation of the GUI object
gui = CalcGUI()

# Creation of the controller object, passing the GUI
controller = calcController(gui)

# Pass the controller object to the GUI
gui.setController(controller)

# launch the GUI once everything is setup and ready.
gui.launch()