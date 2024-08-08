import math
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from modules import all_widgets

MAX_WIDTH_WIDGET = 150
MAX_HEIGHT_WIDGET = 150

# TODO global manageur config file

# TODO two widget subclasses - do something from main window, or switch to new window (link to other widget)
# TODO ctrl + click back/new window will open in new window
# TODO log widget
# TODO replace dock with this
class OptionsOrBackButtonWidget(QWidget):
    pass

class LoggerWidget(QWidget):
    pass

class ToolbarWidget(QWidget):
   pass
    # TODO should be width of entire pyqt window always
    # TODO back button
    
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        # TODO window size adjustable
        self.layout = QVBoxLayout(self)
        self.setLayout(self.layout)
        self.resize(500, 500)
        
        num_widgets = len(all_widgets)

        height = math.floor(math.sqrt(num_widgets))
        width = math.ceil(num_widgets / height)
        
        # TODO make this a grid layout
        # TODO border between widgets
        # TODO and drop to switch order of widgets
        
        for widget in all_widgets:
            self.layout.addWidget(widget())

        self.setLayout(self.layout)

        
        
        

if __name__ == '__main__':
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())