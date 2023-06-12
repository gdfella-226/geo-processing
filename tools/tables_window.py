import json
import os

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QGridLayout, QComboBox, QPushButton
from tools.db_handler import DBHandler


class Tables(QWidget):
    def __init__(self, config_file):
        super().__init__()
        self.config_file = config_file
        self.setWindowTitle("Таблица")
        self.setGeometry(50, 50, 250, 200)
        layout = QGridLayout()
        self.setLayout(layout)

        base = DBHandler(config_file, None)
        tables = [i[0] for i in base.get_tables()]
        self.combo = QComboBox(self)
        for i in tables:
            self.combo.addItem(i)
        if not tables:
            self.combo.addItem("data")
        layout.addWidget(self.combo)
        next_btn = QPushButton('Далее', self)
        next_btn.clicked.connect(self.next)
        layout.addWidget(next_btn)

    @pyqtSlot()
    def next(self):
        table = self.combo.currentText()
        user_data = {"table": table} if table else {"table": "data"}
        with open(os.path.join('./config', self.config_file), 'r', encoding='UTF-8') as config_file:
            data = json.load(config_file)
            data.update(user_data)
        with open(os.path.join('./config', self.config_file), 'w', encoding='UTF-8') as config_file:
            json.dump(data, config_file)

        self.close()
