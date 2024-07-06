import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle(("Manageur"))
        self.setGeometry(100, 100, 280, 80)
        self.helloMsg = QLabel("meow", parent=self)
        self.helloMsg.move(60, 15)



# import os
# import subprocess

# def _python_interpreter():
#     return "/home/work/repos/non-ayora/PatManager/.venv/bin/python3"

# def _PatManager_script_path():
# 	return os.path.join(os.path.dirname(__file__), 'main.py')

# def start_PatManager():
# 	subprocess.run([_python_interpreter(), _PatManager_script_path()])

if __name__ == '__main__':
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())