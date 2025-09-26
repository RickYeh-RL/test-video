'''
Copy and pasted from the pyqt6 demo, but changed names to pyside6
Pyqt6 and pyside6 have very similar interfaces
'''

# Sample videos can be found here: https://github.com/anrayliu/pyvidplayer2-test-resources/tree/main/resources


from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6.QtCore import QTimer
from pyvidplayer2 import VideoPySide
from pyvidplayer2.video import READER_FFMPEG, READER_DECORD, READER_OPENCV, READER_IMAGEIO, READER_AUTO


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.canvas = QWidget(self)
        self.setCentralWidget(self.canvas)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(16)

    def paintEvent(self, _):
        video.draw(self, (0, 0))

VIDEO_PATH = r""
video = VideoPySide(VIDEO_PATH, reader = READER_OPENCV)
video.change_resolution(720)

app = QApplication([])
win = Window()
win.setWindowTitle(f"pyside6 support demo")
win.setFixedSize(*video.current_size)
win.show()
app.exec()

video.close()
