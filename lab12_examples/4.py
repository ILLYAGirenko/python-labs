from PyQt6.QtCore import QSize, QUrl
from PyQt6.QtMultimedia import QMediaPlayer
from PyQt6.QtMultimediaWidgets import QVideoWidget
from PyQt6.QtWidgets import (QApplication, QFileDialog, QPushButton, QVBoxLayout, QWidget)


class VideoPlayerWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Advanced PyQt6 Player")

        # Ініціалізація компонентів плеєра
        self.viewer = QVideoWidget()
        self.viewer.setMinimumSize(QSize(500, 350))
        self.player = QMediaPlayer()

        self.loadVideoBtn = QPushButton("Відкрити MP4 файл...")
        self.loadVideoBtn.clicked.connect(self.open_video_file)

        # Вертикальне розміщення
        layout = QVBoxLayout()
        layout.addWidget(self.viewer)
        layout.addWidget(self.loadVideoBtn)
        self.setLayout(layout)

    def open_video_file(self):
        # Стандартний діалог ОС для вибору файлу
        filename, _ = QFileDialog.getOpenFileName(self, "Оберіть відео", filter="Video (*.mp4)")
        if filename:
            # Передача файлу у плеєр
            self.player.setSource(QUrl.fromLocalFile(filename))
            self.player.setVideoOutput(self.viewer)
            self.player.play()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = VideoPlayerWindow()
    window.show()
    sys.exit(app.exec())