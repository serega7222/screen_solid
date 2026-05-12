#main.py
import sys
from PySide6.QtWidgets import QApplication
#utils 
from utils.signals import MainSignals
#Model
from model.model import Main_Screen_Model
#view 
from view.main_screen import MainScreen
#controllers
from controllers.main_screen_control import OpenDialog

if __name__ == "__main__":
    app = QApplication(sys.argv)

    
    #main 
    main_signals = MainSignals() 
    #View
    main_screen = MainScreen(main_signals)
    #model
    main_model = Main_Screen_Model(main_signals)
    #control
    main_control = OpenDialog(main_signals)

    
    sys.exit(app.exec())