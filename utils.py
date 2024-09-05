from PyQt5.QtCore import QTime, QThread, pyqtSignal
from PyQt5.QtWidgets import QLabel

# lcd_clock
def showTime(self):
    current_time = QTime.currentTime()
    time_text = current_time.toString('hh:mm:ss')
    self.display(time_text)

def close_software(MainWindow):
    MainWindow.close()