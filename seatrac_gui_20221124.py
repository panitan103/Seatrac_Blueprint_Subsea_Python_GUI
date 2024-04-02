import sys
from PyQt5 import QtWidgets, uic,QtCore, QtGui
from PyQt5.QtCore import QObject, QThread, pyqtSignal
import time
from mainwindow import Ui_MainWindow
import seatrac_serial
import threading
import serial,pynmea2

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        
        super(MainWindow, self).__init__(*args, **kwargs)
        self.seatrac=seatrac_serial.Setrac_serial(MODEL="x150",COM_PORT="/dev/tty.usbserial-FT51FT0U",BAUD_RATE=115200)
        
        
        self.setupUi(self)
        self.clink_event()
        
        self.seatrac=seatrac_serial.Setrac_serial(MODEL="x150",COM_PORT="/dev/tty.usbserial-FT51FT0U",BAUD_RATE=115200)
        seatrac_read_thread = threading.Thread(target=self.seatrac_read_command)
        seatrac_read_thread.start()

        self.gps_port = serial.Serial(port="/dev/tty.usbserial-120", baudrate = 4800)
        gps_read_thread = threading.Thread(target=self.gps)
        gps_read_thread.start()

    def input_data(self,input):

        self.feedback_table.setColumnCount(2)
        self.feedback_table.setRowCount(len(input))
        self.feedback_table.hide()
        self.feedback_table.show()
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
        self.ping_command_btn.clicked.connect(self.ping_command)
        self.send_data_command_btn.clicked.connect(self.send_data_command)
        self.status_command_btn.clicked.connect(self.seatrac_read_status)

    def send_data_command(self):
        self.seatrac_write(command="data",payload=None)
        

    def ping_command(self):
        
        self.seatrac_write(command="ping",payload=None)

    def seatrac_read_command(self):
        while 1:    
            serial_input=(self.seatrac.serial_read())
            command_encrypt,command_decrypt=self.seatrac.decrypt_command(status=False,command=True)
            if (command_encrypt is not None and command_decrypt is not None)and (command_decrypt["CmdId"]=="ST_CID_PING_RESP" or command_decrypt["CmdId"]=="ST_CID_XCVR_TX_MSG"):
            #if (command_encrypt is not None and command_decrypt is not None):
                
                self.input_data(command_decrypt)
                time.sleep(0.5)

    def seatrac_read_status(self):
        #serial_input=(self.seatrac.serial_read())
        status_encrypt,status_decrypt=self.seatrac.decrypt_command(status=True,command=False)
        if (status_encrypt is not None and status_decrypt is not None):
            self.input_data(status_decrypt)
            #print(status_decrypt)
            

    def seatrac_write(self,command,payload):
        if command == "ping":
            self.seatrac.serial_write(self.seatrac.ping_x150_command("ST_CID_PING_SEND","beacon_id_01","ST_AMSG_REQX"))
        elif command == "data":
            self.seatrac.serial_write(self.seatrac.send_data_x150_command("ST_CID_NAV_STATUS_SEND","beacon_id_01",self.send_data_input.text()))

    def gps(self):
        _translate = QtCore.QCoreApplication.translate

        while 1:
            #try :
                gps_read = self.gps_port.readline().decode()
                msg = pynmea2.parse(gps_read)
                if gps_read.find('GGA') > 0:
                    self.gps_table.hide()
                    self.gps_table.show()

                    item = self.gps_table.item(0, 0)
                    item.setText(_translate("MainWindow",str(round(msg.latitude,8))))
                    item = self.gps_table.item(0, 1)
                    item.setText(_translate("MainWindow", str(round(msg.longitude,8))))
                    item = self.gps_table.item(0, 2)
                    item.setText(_translate("MainWindow", str(msg.num_sats)))

            #except:
                #print("wait for gps module" )
                #pass
    
if __name__ == "__main__":
    try:
        app = QtWidgets.QApplication(sys.argv)

        window = MainWindow()
        window.show()    
        app.exec()
    except:
        print("some error detected")
        pass
