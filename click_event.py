import sys
from PyQt5 import QtWidgets, uic,QtCore, QtGui

import random
from mainwindow import Ui_MainWindow



#random_num=None
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        
        super(MainWindow, self).__init__(*args, **kwargs)
        #self.seatrac=seatrac_serial.Setrac_serial(MODEL="x150",COM_PORT="/dev/tty.usbserial-FT51FT0U",BAUD_RATE=115200)
        self.setupUi(self)
        #input_data={"Game" : 1, "Akshat" : "asdsdfsd", "Akash" : 3,"Agfkash" : 4}
        #self.seatrac=seatrac_import()
        #self.seatrac_read_thread()
        #self.random_thread()
        #self.input_thread()
        self.ping_command_btn.clicked.connect(self.clink_event)
    
    def input_data(self,input):

        self.feedback_table.setColumnCount(2)
        self.feedback_table.setRowCount(len(input))

        for count,value in enumerate(input):
            
            item = QtWidgets.QTableWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.feedback_table.setVerticalHeaderItem(count, item)
            
            item = QtWidgets.QTableWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.feedback_table.setItem(count, 0, item)

            item = QtWidgets.QTableWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
            self.feedback_table.setItem(count, 1, item)

        _translate = QtCore.QCoreApplication.translate

        for count,value in enumerate(input):
            
            item = self.feedback_table.verticalHeaderItem(count)
            item.setText(_translate("MainWindow",str(count)))
            item = self.feedback_table.item(count, 0)
            item.setText(_translate("MainWindow",value))
            item = self.feedback_table.item(count, 1)
            item.setText(_translate("MainWindow", str(input[value])))

    def clink_event(self):
        random_num={"value": random.randint(0, 100)}
        self.input_data(random_num)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()
