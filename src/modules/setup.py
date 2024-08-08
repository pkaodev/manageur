import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout
from PyQt6.QtCore import QProcess

class SettingsWidget(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		layout = QGridLayout(self)
		self.setLayout(layout)

		colors = ["red", "green", "blue", "yellow"]
		positions = [(0, 0), (0, 1), (1, 0), (1, 1)]

		for position, color in zip(positions, colors):
			button = self.createButton(color)
			button.setFixedSize(75, 75)
			layout.addWidget(button, *position)

	def createButton(self, color):
		button = QPushButton(color)
		button.setStyleSheet(f"background-color: {color};")
		return button
