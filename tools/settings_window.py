import json
import os
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout, QLineEdit, QCheckBox, QPushButton
from tools.tables_window import Tables


class Settings(QWidget):
    """
        This "window" is a QWidget.
        It appears by choice "edit settings" option on main screen.
        Data from this window composes in config.json
    """

    def __init__(self):
        super(Settings, self).__init__()
        self.setWindowTitle("Настройки запуска")
        self.setGeometry(100, 100, 500, 400)
        layout = QGridLayout()
        self.setLayout(layout)
        self.tables_window = None

        labels = [
            QLabel("База данных:"),
            QLabel("Пользователь:"),
            QLabel("Пароль:"),
            QLabel("Хост:"),
            QLabel("Порт:")
        ]
        self.inputs = []
        for i in range(len(labels)):
            self.inputs.append(QLineEdit())
            if labels[i].text() == "Пароль:":
                self.inputs[i].setEchoMode(QLineEdit.Password)
            """if labels[i].text() == "Таблица:":
                table_box = QComboBox(self)"""

            layout.addWidget(labels[i], i, 0)
            layout.addWidget(self.inputs[i], i, 1)
        overwrite = QCheckBox("Перезапись", self)
        layout.addWidget(overwrite, i + 1, 0)
        self.inputs.append(overwrite)
        save_btn = QPushButton('Сохранить', self)
        save_btn.clicked.connect(self.save)
        layout.addWidget(save_btn, i + 1, 1)

    @pyqtSlot()
    def save(self):
        user_data = {
            "database": self.inputs[0].text(),
            "user": self.inputs[1].text(),
            "password": self.inputs[2].text(),
            "host": self.inputs[3].text(),
            "port": self.inputs[4].text(),
            "overwrite": self.inputs[5].isChecked()
        }
        print(user_data)
        with open(os.path.join('./config', 'test_config.json'), 'w+', encoding='UTF-8') as config_file:
            json.dump(user_data, config_file)
        self.tables_window = Tables('test_config.json')
        self.tables_window.show()
        self.close()


