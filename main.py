
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox,QDesktopWidget
from PyQt5.QtCore import Qt
import qtmodern.styles
import qtmodern.windows
import main_window_work
if __name__ == '__main__':

    # 适配高清屏
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)

    app = QApplication(sys.argv)

    qtmodern.styles.dark(app)

    main_window = main_window_work.MainWindowWork()
    win = qtmodern.windows.ModernWindow(main_window)

    # 获取窗口大小
    screen = QDesktopWidget().screenGeometry()
    size = win.geometry()

    # 本窗体运动
    win.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)

    # 显示主窗口
    win.show()

    sys.exit(app.exec_())
