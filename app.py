import os
from sys import argv, exit
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, \
    QLabel, QAction, QFileDialog, QMessageBox
from tools.settings_window import Settings
from tools.db_handler import DBHandler


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.data_file = None
        self.settings_window = Settings()
        self.setWindowTitle("Title")
        self.setGeometry(100, 100, 500, 400)
        central_widget = QLabel("Manual: how to use this awesome app")
        central_widget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.setCentralWidget(central_widget)
        self._menu()

    def _menu(self):
        menu = self.menuBar()
        file_btn = menu.addMenu("Файл")
        settings_btn = menu.addMenu("Настройки")
        run_btn = menu.addMenu("Старт")

        import_action = QAction(self)
        import_action.setText("Импорт")
        import_action.triggered.connect(self.get_file)
        exit_action = QAction(self)
        exit_action.setText("Выход")
        exit_action.triggered.connect(exit)
        set_action = QAction(self)
        set_action.setText("Параметры запуска")
        set_action.triggered.connect(self.settings_window.show)
        run_action = QAction(self)
        run_action.setText("Запуск с текущими настройками")

        file_btn.addActions((import_action, exit_action))
        settings_btn.addAction(set_action)
        run_btn.addAction(run_action)
        run_action.triggered.connect(self.run)

    def get_file(self):
        self.data_file, _ = QFileDialog.getOpenFileName()

    def run(self):
        config_files_list = os.listdir('./config')
        print(self.data_file)
        print(os.listdir('./config'))
        if config_files_list and self.data_file is not None:
            base = DBHandler(config_files_list[0], self.data_file)
            base.run()
            QMessageBox.warning(self, "ГОТОВО!", "Данные успешно перенесены в БД")
            # base.show_table()
        elif self.data_file is None:
            QMessageBox.warning(self, "ВНИМАНИЕ!", "Выберите '.xlsx' файл для загрузки данных")
        else:
            QMessageBox.warning(self, "ВНИМАНИЕ!", "Введите параметры запуска согласно инструкции")




if __name__ == "__main__":
    app = QApplication(argv)
    mw = MainWindow()
    mw.show()
    exit(app.exec())
