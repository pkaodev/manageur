import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt6.QtCore import QProcess

class SettingsWidget(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		layout = QVBoxLayout()
		self.setLayout(layout)

		colors = ["red", "green", "blue", "yellow"]

		for color in colors:
			button = self.createButton(color)
			button.setFixedSize(75, 75)
			layout.addWidget(button)

	def createButton(self, color):
		button = QPushButton(color)
		button.setStyleSheet(f"background-color: {color}")
		return button