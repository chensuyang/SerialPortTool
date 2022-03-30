import main_window_work
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import Qt
import qtmodern.styles
import qtmodern.windows

if __name__ == '__main__':

    # 适配高清屏
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)

    app = QApplication(sys.argv)

    qtmodern.styles.dark(app)

    main_window = main_window_work.main_window_work()
    win = qtmodern.windows.ModernWindow(main_window)

    # 显示主窗口
    win.show()

    sys.exit(app.exec_())
