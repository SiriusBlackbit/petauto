import sys
import keyboard
import pyautogui
import random
import time
from threading import Thread,Lock
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
fip =  './images/f.png'
yip = './images/y.png'


class DvApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

        self.im = False
        self.lock = Lock()
        keyboard.add_hotkey('1', self.st)
        keyboard.add_hotkey('2', self.sp)


    def initUI(self):
        layout = QVBoxLayout()

        self.stm = QPushButton("自动开蛋", self)
        self.stm.clicked.connect(self.st)
        layout.addWidget(self.stm)

        self.stp = QPushButton("停止开蛋", self)
        self.stp.clicked.connect(self.sp)
        layout.addWidget(self.stp)

        self.setLayout(layout)
        self.setWindowTitle('Dv脚本')
        self.resize(200,80)
        self.move(5,5)
        self.show()

    def st(self):
        if not self.im:
            self.im = True
            self.mt = Thread(target=self.rm)
            self.mt.start()

    def sp(self):
        self.im = False

    def click_image(self,ip):
        try:
            location = pyautogui.locateOnScreen(ip, confidence=0.8)  # confidence 参数是 OpenCV 的特性，0.8 表示匹配度
            if location is not None:
                x, y, width, height = location.left, location.top, location.width, location.height
                click_x = x + random.randint(width // 3, width // 2)
                click_y = y + random.randint(height //3, height // 2)
                clicks = 1
                interval = 0
                pyautogui.click(click_x, click_y, clicks=clicks, interval=interval)
        except pyautogui.ImageNotFoundException:
            return None

    def rm(self):
        while self.im:
            mwt = random.uniform(0, 0.3)
            self.click_image(fip)
            time.sleep(mwt)
            self.click_image(yip)
            time.sleep(mwt)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DvApp()
    sys.exit(app.exec())

