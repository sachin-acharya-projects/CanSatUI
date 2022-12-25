from PyQt5 import QtCore, QtGui, QtWidgets
from Communication import Communication
from Database import Database
from plotters import PlotAcceleration
import pyqtgraph as pg, time

class MyThread(QtCore.QThread):
    update_progress = QtCore.pyqtSignal(name="Updated Value")
    def __init__(self, parent):
        super(MyThread, self).__init__(parent)
        self.isDone = False
    def run(self):
        while True:
            if self.isDone:
                break
            time.sleep(100)
            self.update_progress.emit()
    def stop(self):
        self.isDone = True
    
class Ui_MainWindow(object):
    def setupUi(self, MainWindow: QtWidgets.QMainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(790, 596)
        # Configurations
        pg.setConfigOption('background', (33, 33, 33))
        pg.setConfigOption('foreground', (197, 198, 199))
        self.serial_connection = Communication()
        self.database = Database()
        MainWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        
        MainWindow.setStyleSheet("QMainWindow {\n"
"    background: #222;\n"
"}\n"
"#frame {\n"
"    background: #333;\n"
"    padding: 2px;\n"
"}\n"
"#titleIcon {\n"
"    padding: 2px;\n"
"}\n"
"#main_title, #title_pretext {\n"
"    color: #ccc;\n"
"}\n"
"#about_me, #closeWindow {\n"
"    border-radius: 2px;\n"
"    background: #222;\n"
"    border: 1px solid  rgb(153, 153, 153);\n"
"    color: white; /* Change Programatically */\n"
"}\n"
"QProgressBar {\n"
"    border-style: solid;\n"
"    background-color: rgb(196, 196, 255);\n"
"    border-radius: 2px;\n"
"    color: #333;\n"
"    /*Change Font Famaily*/\n"
"}\n"
"QProgressBar::chunk {\n"
"    border-radius: 2px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.006, y1:0.147727, x2:1, y2:1, stop:0.0965909 rgba(199, 44, 77, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QScrollArea {\n"
"    padding: 10px;\n"
"    background: #222;\n"
"    border-color: #222;\n"
"}\n"
"#scrollAreaWidgetContents {\n"
"    border-color: #222;\n"
"    background: #222;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(0, 72))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 72))
        self.frame.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_4.setContentsMargins(12, 10, 12, 6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.titleIcon = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titleIcon.sizePolicy().hasHeightForWidth())
        self.titleIcon.setSizePolicy(sizePolicy)
        self.titleIcon.setMinimumSize(QtCore.QSize(50, 50))
        self.titleIcon.setMaximumSize(QtCore.QSize(50, 50))
        self.titleIcon.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.titleIcon.setText("")
        self.titleIcon.setPixmap(QtGui.QPixmap(":/resources/icon.png"))
        self.titleIcon.setScaledContents(True)
        self.titleIcon.setObjectName("titleIcon")
        self.horizontalLayout.addWidget(self.titleIcon)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.main_title = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_title.sizePolicy().hasHeightForWidth())
        self.main_title.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(204, 204, 204))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(204, 204, 204))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(204, 204, 204))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(204, 204, 204, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(204, 204, 204))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(204, 204, 204))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(204, 204, 204))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(204, 204, 204, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(204, 204, 204))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(204, 204, 204))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(204, 204, 204))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(204, 204, 204, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.main_title.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bangers")
        font.setPointSize(23)
        self.main_title.setFont(font)
        self.main_title.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.main_title.setObjectName("main_title")
        self.verticalLayout_2.addWidget(self.main_title)
        self.title_pretext = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_pretext.sizePolicy().hasHeightForWidth())
        self.title_pretext.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(9)
        font.setBold(False)
        self.title_pretext.setFont(font)
        self.title_pretext.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.title_pretext.setObjectName("title_pretext")
        self.verticalLayout_2.addWidget(self.title_pretext)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(9)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.about_me = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.about_me.sizePolicy().hasHeightForWidth())
        self.about_me.setSizePolicy(sizePolicy)
        self.about_me.setMinimumSize(QtCore.QSize(25, 25))
        self.about_me.setMaximumSize(QtCore.QSize(25, 25))
        self.about_me.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.about_me.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/resources/circle-info-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.about_me.setIcon(icon)
        self.about_me.setObjectName("about_me")
        self.horizontalLayout_2.addWidget(self.about_me)
        self.batteryIndicator = QtWidgets.QProgressBar(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.batteryIndicator.sizePolicy().hasHeightForWidth())
        self.batteryIndicator.setSizePolicy(sizePolicy)
        self.batteryIndicator.setMaximumSize(QtCore.QSize(40, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.batteryIndicator.setFont(font)
        self.batteryIndicator.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.batteryIndicator.setProperty("value", 24)
        self.batteryIndicator.setAlignment(QtCore.Qt.AlignCenter)
        self.batteryIndicator.setObjectName("batteryIndicator")
        self.horizontalLayout_2.addWidget(self.batteryIndicator)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem2)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.horizontalLayout.setStretch(1, 1)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 758, 446))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        
        # self.graphicsView = pg.GraphicsView(self.scrollAreaWidgetContents)
        self.graphicsView = pg.GraphicsView()
        self.graphicsLayout = pg.GraphicsLayout()
        self.graphicsView.setCentralItem(self.graphicsLayout)
        self.acceleration = PlotAcceleration()
        
        lb = self.graphicsLayout.addLayout(colspan=1)
        lb.addItem(self.acceleration)
        
        self.timer = MyThread(MainWindow)
        self.timer.update_progress.connect(self.update)
        self.timer.start()
        
        self.gridLayout_2.addWidget(self.graphicsView, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 2, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(13, 5, 0, 5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.start_storage = QtWidgets.QPushButton(self.centralwidget)
        self.start_storage.setObjectName("start_storage")
        self.horizontalLayout_3.addWidget(self.start_storage)
        self.maximize_window = QtWidgets.QPushButton(self.centralwidget)
        self.maximize_window.setObjectName("maximize_window")
        self.horizontalLayout_3.addWidget(self.maximize_window)
        self.close_window = QtWidgets.QPushButton(self.centralwidget)
        self.close_window.setObjectName("close_window")
        self.close_window.clicked.connect(self.closeProperly)
        self.horizontalLayout_3.addWidget(self.close_window)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def closeProperly(self):
        if self.timer.isRunning():
            self.timer.terminate()
        MainWindow.close()
    def update(self):
        print("In we go")
        try:
            value_chain = []
            value_chain = self.serial_connection.getData()
            if len(value_chain) > 1:
                print(value_chain)
                self.acceleration.update(*value_chain[:3])
                self.database.guardar(value_chain)
        except IndexError as e:
            print(str(e))
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Data Visualizations"))
        self.main_title.setText(_translate("MainWindow", "Data Visualizations"))
        self.title_pretext.setText(_translate("MainWindow", "Graphical Presentation of Sensor data from CanSat — Sachin Acharya"))
        self.start_storage.setText(_translate("MainWindow", "Start Storage"))
        self.maximize_window.setText(_translate("MainWindow", "Maximize"))
        self.close_window.setText(_translate("MainWindow", "Close"))
import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
