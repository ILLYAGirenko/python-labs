import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QPushButton


class SimpleApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PyQt5 Lab')
        self.resize(300, 150)

        layout = QVBoxLayout()

        self.lbl = QLabel('Аналіз фреймворку PyQt')
        self.btn = QPushButton('Закрити')
        self.btn.clicked.connect(self.close)

        layout.addWidget(self.lbl)
        layout.addWidget(self.btn)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = SimpleApp()
    w.show()
    sys.exit(app.exec_())