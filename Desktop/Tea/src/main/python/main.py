from fbs_runtime.application_context import ApplicationContext
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import *
from tea import *

import sys

class AppContext(ApplicationContext):          
    def __init__(self, app, window):
        version = self.build_settings['version']
        setUpUi(version, window)
     

        
        
    def run(self):                              
        return self.app.exec_() 
        



if __name__ == '__main__':
    app = QApplication(sys.argv) 
    MainWindow = QMainWindow()
    
    ui = AppContext(app, MainWindow)
    MainWindow.show()
    exit_code = ui.run()                  
    sys.exit(exit_code)