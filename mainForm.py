# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settingForm.ui'
#
# Created: Sun Feb 28 01:24:44 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!
import sys
import os
import datetime
import threading
import configparser
from PySide import QtCore, QtGui
import comment_client
import comment_handler
import danmuku_scroller


class UiForm(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.gridLayoutWidget = None
        self.gridLayout = None
        self.checkBoxTurnOn = None
        self.label = None
        self.pushButtonConnect = None
        self.checkBoxKeepTop = None
        self.pushButtonDisConn = None
        self.checkBoxReconn = None
        self.label_3 = None
        self.pushButtonTestScroll = None
        self.lineEditRoomId = None
        self.labelPeopleCount = None
        self.tabWidget = None
        self.tab = None
        self.plainTextEditLogs = None
        self.tab_2 = None
        self.gridLayoutWidget_2 = None
        self.gridLayout_2 = None
        self.label_5 = None
        self.lineEditPosX = None
        self.lineEditPosY = None
        self.label_8 = None
        self.label_7 = None
        self.lineEditWidth = None
        self.lineEditHeight = None
        self.label_6 = None
        self.label_9 = None
        self.lineEditFontSize = None
        self.label_10 = None
        self.lineEditUpdateInterval = None
        self.label_4 = None
        # 自定义
        self.client = None
        self.live_sock = None
        self.data_handler = None
        self.scroller = None
        self.recv_thread = None
        self.exeruningpath = os.path.dirname(sys.executable)

    def setup_ui(self, form):
        form.setObjectName("Form")
        form.resize(682, 470)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./icon-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        form.setWindowIcon(icon)
        self.gridLayoutWidget = QtGui.QWidget(form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 659, 431))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.checkBoxTurnOn = QtGui.QCheckBox(self.gridLayoutWidget)
        self.checkBoxTurnOn.setObjectName("checkBoxTurnOn")
        self.gridLayout.addWidget(self.checkBoxTurnOn, 1, 3, 1, 1)
        self.label = QtGui.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.pushButtonConnect = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushButtonConnect.setObjectName("pushButtonConnect")
        self.gridLayout.addWidget(self.pushButtonConnect, 0, 3, 1, 1)
        self.checkBoxKeepTop = QtGui.QCheckBox(self.gridLayoutWidget)
        self.checkBoxKeepTop.setObjectName("checkBoxKeepTop")
        self.gridLayout.addWidget(self.checkBoxKeepTop, 1, 5, 1, 1)
        self.pushButtonDisConn = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushButtonDisConn.setObjectName("pushButtonDisConn")
        self.gridLayout.addWidget(self.pushButtonDisConn, 0, 4, 1, 1)
        self.checkBoxReconn = QtGui.QCheckBox(self.gridLayoutWidget)
        self.checkBoxReconn.setObjectName("checkBoxReconn")
        self.gridLayout.addWidget(self.checkBoxReconn, 1, 4, 1, 1)
        self.label_3 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 2, 1, 1)
        self.pushButtonTestScroll = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushButtonTestScroll.setObjectName("pushButtonTestScroll")
        self.gridLayout.addWidget(self.pushButtonTestScroll, 0, 5, 1, 1)
        self.lineEditRoomId = QtGui.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditRoomId.sizePolicy().hasHeightForWidth())
        self.lineEditRoomId.setSizePolicy(sizePolicy)
        self.lineEditRoomId.setMinimumSize(QtCore.QSize(0, 0))
        self.lineEditRoomId.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEditRoomId.setObjectName("lineEditRoomId")
        self.gridLayout.addWidget(self.lineEditRoomId, 0, 2, 1, 1)
        self.labelPeopleCount = QtGui.QLabel(self.gridLayoutWidget)
        self.labelPeopleCount.setObjectName("labelPeopleCount")
        self.gridLayout.addWidget(self.labelPeopleCount, 1, 1, 1, 1)
        self.tabWidget = QtGui.QTabWidget(self.gridLayoutWidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.plainTextEditLogs = QtGui.QPlainTextEdit(self.tab)
        self.plainTextEditLogs.setGeometry(QtCore.QRect(10, 10, 631, 341))
        self.plainTextEditLogs.setReadOnly(True)
        self.plainTextEditLogs.setObjectName("plainTextEditLogs")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayoutWidget_2 = QtGui.QWidget(self.tab_2)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 651, 51))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_5 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 1, 1, 1)
        self.lineEditPosX = QtGui.QLineEdit(self.gridLayoutWidget_2)
        self.lineEditPosX.setObjectName("lineEditPosX")
        self.gridLayout_2.addWidget(self.lineEditPosX, 0, 2, 1, 1)
        self.lineEditPosY = QtGui.QLineEdit(self.gridLayoutWidget_2)
        self.lineEditPosY.setObjectName("lineEditPosY")
        self.gridLayout_2.addWidget(self.lineEditPosY, 0, 4, 1, 1)
        self.label_8 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 0, 7, 1, 1)
        self.label_7 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 5, 1, 1)
        self.lineEditWidth = QtGui.QLineEdit(self.gridLayoutWidget_2)
        self.lineEditWidth.setObjectName("lineEditWidth")
        self.gridLayout_2.addWidget(self.lineEditWidth, 0, 6, 1, 1)
        self.lineEditHeight = QtGui.QLineEdit(self.gridLayoutWidget_2)
        self.lineEditHeight.setObjectName("lineEditHeight")
        self.gridLayout_2.addWidget(self.lineEditHeight, 0, 8, 1, 1)
        self.label_6 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 0, 3, 1, 1)
        self.label_9 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 1, 1, 1, 1)
        self.lineEditFontSize = QtGui.QLineEdit(self.gridLayoutWidget_2)
        self.lineEditFontSize.setObjectName("lineEditFontSize")
        self.gridLayout_2.addWidget(self.lineEditFontSize, 1, 2, 1, 1)
        self.label_10 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 1, 3, 1, 1)
        self.lineEditUpdateInterval = QtGui.QLineEdit(self.gridLayoutWidget_2)
        self.lineEditUpdateInterval.setObjectName("lineEditUpdateInterval")
        self.gridLayout_2.addWidget(self.lineEditUpdateInterval, 1, 4, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 2, 1, 1, 5)
        self.label_4 = QtGui.QLabel(form)
        self.label_4.setGeometry(QtCore.QRect(10, 450, 604, 12))
        self.label_4.setObjectName("label_4")

        self.retranslate_ui(form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(form)
        # connect
        QtCore.QObject.connect(self.pushButtonConnect, QtCore.SIGNAL("clicked()"), self.start)
        QtCore.QObject.connect(self.pushButtonDisConn, QtCore.SIGNAL("clicked()"), self.stop)
        QtCore.QObject.connect(self.pushButtonTestScroll, QtCore.SIGNAL("clicked()"), self.test_scroll)
        # QtCore.QObject.connect(self, QtCore.SIGNAL('triggered()'), self.when_close)
        # self.checkBoxTurnOn.stateChanged.connect(self.change_scroller)

    def retranslate_ui(self, form):
        form.setWindowTitle(QtGui.QApplication.translate("Form", "弹幕姬Python版", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxTurnOn.setText(QtGui.QApplication.translate("Form", "侧边栏", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "直播间地址：http://live.bilibili.com/", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonConnect.setText(QtGui.QApplication.translate("Form", "连接", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxKeepTop.setText(QtGui.QApplication.translate("Form", "窗口置顶", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonDisConn.setText(QtGui.QApplication.translate("Form", "断开", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxReconn.setText(QtGui.QApplication.translate("Form", "自动重连", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonTestScroll.setText(QtGui.QApplication.translate("Form", "测试效果", None, QtGui.QApplication.UnicodeUTF8))
        self.labelPeopleCount.setText(QtGui.QApplication.translate("Form", "当前房间人数：Ø", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("Form", "日志", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Form", "坐标x：", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Form", "高度：", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Form", "宽度：", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Form", "坐标y：", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("Form", "字号：", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("Form", "刷新周期：", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("Form", "设置", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "Copyright © 2016 liuzc  房间号 58472  问题反馈到 liuz430524@hotmail.com", None, QtGui.QApplication.UnicodeUTF8))

    def read_conf(self):
        cf = configparser.ConfigParser()
        cf.read(self.exeruningpath + "\\danmuji.conf")
        if cf.has_section("settings"):
            if cf.has_option("settings", "roomId"):
                self.lineEditRoomId.setText(cf.get("settings", "roomId"))
            if cf.has_option("settings", "isTurnOnScroller"):
                self.checkBoxTurnOn.setChecked(cf.getboolean("settings", "isTurnOnScroller"))
            if cf.has_option("settings", "isReConn"):
                self.checkBoxReconn.setChecked(cf.getboolean("settings", "isReConn"))
            if cf.has_option("settings", "isOnTop"):
                self.checkBoxKeepTop.setChecked(cf.getboolean("settings", "isOnTop"))
            if cf.has_option("settings", "scroller_posX"):
                self.lineEditPosX.setText(cf.get("settings", "scroller_posX"))
            if cf.has_option("settings", "scroller_posY"):
                self.lineEditPosY.setText(cf.get("settings", "scroller_posY"))
            if cf.has_option("settings", "scroller_width"):
                self.lineEditWidth.setText(cf.get("settings", "scroller_width"))
            if cf.has_option("settings", "scroller_height"):
                self.lineEditHeight.setText(cf.get("settings", "scroller_height"))
            if cf.has_option("settings", "scroller_font"):
                self.lineEditFontSize.setText(cf.get("settings", "scroller_font"))
            if cf.has_option("settings", "scroller_interval"):
                self.lineEditUpdateInterval.setText(cf.get("settings", "scroller_interval"))

    def write_conf(self):
        cf = configparser.ConfigParser()
        if cf.has_section("settings") is False:
            cf.add_section("settings")
        if self.lineEditRoomId.text().isdigit():
            cf.set("settings", "roomId", self.lineEditRoomId.text())
        if self.checkBoxTurnOn.isChecked():
            cf.set("settings", "isTurnOnScroller", "True")
        else:
            cf.set("settings", "isTurnOnScroller", "False")
        if self.checkBoxReconn.isChecked():
            cf.set("settings", "isReConn", "True")
        else:
            cf.set("settings", "isReConn", "False")
        if self.checkBoxKeepTop.isChecked():
            cf.set("settings", "isOnTop", "True")
        else:
            cf.set("settings", "isOnTop", "False")
        cf.set("settings", "scroller_posX", self.lineEditPosX.text())
        cf.set("settings", "scroller_posY", self.lineEditPosY.text())
        cf.set("settings", "scroller_width", self.lineEditWidth.text())
        cf.set("settings", "scroller_height", self.lineEditHeight.text())
        cf.set("settings", "scroller_font", self.lineEditFontSize.text())
        cf.set("settings", "scroller_interval", self.lineEditUpdateInterval.text())
        cf.write(open(self.exeruningpath + "\\danmuji.conf", "w"))

    def start(self):
        room_id = self.lineEditRoomId.text()
        if room_id.isdigit():
            self.client = comment_client.CommentClient()
            self.live_sock = self.client.connect(room_id)
            if self.live_sock is not None:
                self.data_handler = comment_handler.SocketDataHandler()
                self.data_handler.speaker.connect(main_form.add_comment)
                if self.checkBoxTurnOn.isChecked():
                    pos_x = self.lineEditPosX.text()
                    if pos_x.isdigit() is False:
                        pos_x = "-1"
                    pos_y = self.lineEditPosY.text()
                    if pos_y.isdigit() is False:
                        pos_y = "-1"
                    width = self.lineEditWidth.text()
                    if width.isdigit() is False:
                        width = "-1"
                    height = self.lineEditHeight.text()
                    if height.isdigit() is False:
                        height = "-1"
                    font_size = self.lineEditFontSize.text()
                    if font_size.isdigit() is False:
                        font_size = "-1"
                    interval = self.lineEditUpdateInterval.text()
                    if interval.isdigit() is False:
                        interval = "-1"
                    is_top = self.checkBoxKeepTop.isChecked()
                    self.scroller = danmuku_scroller.RightScroller(int(pos_x), int(pos_y), int(width), int(height),
                                                                   int(font_size), int(interval), is_top)
                    self.scroller.start()
                    self.data_handler.speaker.connect(self.scroller.add_one_comment)
                self.recv_thread = threading.Thread(target=self.data_handler.recv_msg_loop, args=(self.live_sock,),
                                                    name="recv_thread")
                self.recv_thread.start()
                self.write_conf()
                self.pushButtonConnect.setEnabled(False)
                # self.recv_thread.join()
                # self.client.disconnect(self.live_sock)
        else:
            msg_box = QtGui.QMessageBox()
            msg_box.setText("请输入正确的直播房号")
            msg_box.exec_()

    def stop(self):
        if self.live_sock is not None:
            self.client.disconnect(self.live_sock)
            self.live_sock = None
        if self.data_handler is not None:
            self.data_handler.speaker.disconnect(main_form.add_comment)
            if self.scroller is not None:
                self.data_handler.speaker.disconnect(self.scroller.add_one_comment)
                self.scroller.stop()
                self.scroller = None
            self.data_handler.stop()
            self.data_handler = None
        # if self.live_sock is not None:
        #     self.client.disconnect(self.live_sock)
        # if self.scroller is not None:
        #     if self.data_handler is not None:
        #         self.data_handler.speaker.disconnect(self.scroller.add_one_comment)
        #     self.scroller.stop()

        self.pushButtonConnect.setEnabled(True)

    def closeEvent(self, event):
        self.stop()
        event.accept()
    # @QtCore.Slot(int)
    # def change_scroller(self, state):
    #     if self.scroller is not None:
    #         if state == QtCore.Qt.CheckState.Unchecked:
    #             self.scroller.setVisible(False)
    #         if state == QtCore.Qt.CheckState.Checked:
    #             self.scroller.setVisible(True)

    def test_scroll(self):
        if self.data_handler is not None and self.checkBoxTurnOn.isChecked():
            self.data_handler.speaker.emit(1, "弹幕姬：", "这是一个测试")

    @QtCore.Slot(int, str, str)
    def add_comment(self, msg_type, speaker, comment):
        if msg_type == 2:
            self.labelPeopleCount.setText(speaker + comment)
        else:
            now = datetime.datetime.now()
            self.plainTextEditLogs.appendPlainText(now.strftime("%H:%M:%S ") + speaker + comment)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    wgt = QtGui.QWidget()
    main_form = UiForm()
    main_form.setup_ui(wgt)
    main_form.read_conf()
    wgt.show()
    wgt.closeEvent = main_form.closeEvent
    sys.exit(app.exec_())
