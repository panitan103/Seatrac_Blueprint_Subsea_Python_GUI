# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(425, 478)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(320, 320))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.send_commnad_label = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.send_commnad_label.setFont(font)
        self.send_commnad_label.setObjectName("send_commnad_label")
        self.verticalLayout.addWidget(self.send_commnad_label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ping_command_btn = QtWidgets.QPushButton(self.tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ping_command_btn.setFont(font)
        self.ping_command_btn.setObjectName("ping_command_btn")
        self.horizontalLayout.addWidget(self.ping_command_btn)
        self.send_data_command_btn = QtWidgets.QPushButton(self.tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.send_data_command_btn.setFont(font)
        self.send_data_command_btn.setObjectName("send_data_command_btn")
        self.horizontalLayout.addWidget(self.send_data_command_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.send_data_input = QtWidgets.QLineEdit(self.tab)
        self.send_data_input.setObjectName("send_data_input")
        self.verticalLayout.addWidget(self.send_data_input)
        self.feedback_label = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.feedback_label.setFont(font)
        self.feedback_label.setObjectName("feedback_label")
        self.verticalLayout.addWidget(self.feedback_label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.data_check_box = QtWidgets.QCheckBox(self.tab)
        self.data_check_box.setObjectName("data_check_box")
        self.horizontalLayout_2.addWidget(self.data_check_box)
        self.status_check_box = QtWidgets.QCheckBox(self.tab)
        self.status_check_box.setObjectName("status_check_box")
        self.horizontalLayout_2.addWidget(self.status_check_box)
        self.ping_check_box = QtWidgets.QCheckBox(self.tab)
        self.ping_check_box.setObjectName("ping_check_box")
        self.horizontalLayout_2.addWidget(self.ping_check_box)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.feedback_table = QtWidgets.QTableWidget(self.tab)
        self.feedback_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.feedback_table.setAlternatingRowColors(False)
        self.feedback_table.setShowGrid(True)
        self.feedback_table.setWordWrap(True)
        self.feedback_table.setCornerButtonEnabled(True)
        self.feedback_table.setObjectName("feedback_table")
        self.feedback_table.setColumnCount(2)
        self.feedback_table.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.feedback_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.feedback_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.feedback_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.feedback_table.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.feedback_table.setItem(0, 1, item)
        self.verticalLayout.addWidget(self.feedback_table)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.send_data_command_btn.clicked.connect(self.send_data_command_btn.hide)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.send_data_command_btn, self.send_data_input)
        MainWindow.setTabOrder(self.send_data_input, self.data_check_box)
        MainWindow.setTabOrder(self.data_check_box, self.status_check_box)
        MainWindow.setTabOrder(self.status_check_box, self.ping_check_box)
        MainWindow.setTabOrder(self.ping_check_box, self.feedback_table)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Seatrac"))
        self.send_commnad_label.setText(_translate("MainWindow", "Send Command"))
        self.ping_command_btn.setText(_translate("MainWindow", "Ping"))
        self.send_data_command_btn.setText(_translate("MainWindow", "Data"))
        self.send_data_input.setText(_translate("MainWindow", "data_test"))
        self.feedback_label.setText(_translate("MainWindow", "Feedback"))
        self.data_check_box.setText(_translate("MainWindow", "Status"))
        self.status_check_box.setText(_translate("MainWindow", "Ping"))
        self.ping_check_box.setText(_translate("MainWindow", "Data"))
        self.feedback_table.setSortingEnabled(False)
        item = self.feedback_table.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.feedback_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "data"))
        item = self.feedback_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "value"))
        __sortingEnabled = self.feedback_table.isSortingEnabled()
        self.feedback_table.setSortingEnabled(False)
        item = self.feedback_table.item(0, 0)
        item.setText(_translate("MainWindow", "AHRS_RAW_MAG_X"))
        item = self.feedback_table.item(0, 1)
        item.setText(_translate("MainWindow", "ST_CID_STATUS"))
        self.feedback_table.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Basic"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Page"))

