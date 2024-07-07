import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt6.QtCore import QProcess


_SCRIPT_PATHS_ = [
	('startup', "$HOME/scripts/startup.sh"),
	('shutdown', "$HOME/scripts/shutdown.sh"),
]

class ScriptRunnerWidget(QWidget):
    def __init__(self, scripts=_SCRIPT_PATHS_):
        super().__init__()
        self.initUI(scripts)
        
    def initUI(self, scripts):
        self.scripts = scripts
        layout = QVBoxLayout(self)
        
        for name, path in self.scripts:
            button = QPushButton(name, self)
            button.clicked.connect(lambda checked, path=path: self.runScript(path))
            layout.addWidget(button)

        self.setMinimumSize(200, 200)
        self.setMaximumSize(200, 200)
        self.setLayout(layout)
        self.setContentsMargins(0, 0, 0, 0)
        self.setStyleSheet("QWidget { background-color: white; }")
        # self.setScrollBarsEnabled(True)

    def runScript(self, path):
        process = QProcess(self)
        process.start(f"bash {path}")