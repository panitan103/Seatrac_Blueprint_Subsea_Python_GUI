import sys, os
from PyQt5 import QtWidgets, uic,QtCore, QtGui
#from PyQt5.QtCore import QObject, QThread, pyqtSignal
import time
import seatrac_serial
import threading
import serial,pynmea2
import random


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        
        super(MainWindow, self).__init__(*args, **kwargs)
        ui_path = os.path.dirname(os.path.abspath(__file__))
        uic.loadUi(os.path.join(ui_path, "mainwindow.ui"), self)

        self.seatrac=seatrac_serial.Setrac_serial(MODEL="x150",COM_PORT="COM4",BAUD_RATE=115200)

        
        
    def input_data(self,input):

        self.feedback_table.setColumnCount(2)
        self.feedback_table.setRowCount(len(input))

        
        
        _translate = QtCore.QCoreApplication.translate

        for count,value in enumerate(input):

            item = QtWidgets.QTableWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignCenter|QtCore.Qt.AlignVCenter)
            self.feedback_table.setItem(count, 0, item)

            item = QtWidgets.QTableWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignCenter|QtCore.Qt.AlignVCenter)
            self.feedback_table.setItem(count, 1, item)

            item.setText(_translate("MainWindow",str(count)))
            item = self.feedback_table.item(count, 0)
            item.setText(_translate("MainWindow",value))
            item = self.feedback_table.item(count, 1)
            item.setText(_translate("MainWindow", str(input[value])))
        self.feedback_table.hide()
        self.feedback_table.show()
         

    def clink_event(self):
        self.ping_command_btn.clicked.connect(self.ping_command)
        self.send_data_command_btn.clicked.connect(self.send_data_command)
        self.status_command_btn.clicked.connect(self.seatrac_read_status)
        #self.status_command_btn.clicked.connect(self.random_number)

    def send_data_command(self):
        
        self.seatrac.serial_write(self.seatrac.send_data_x150_command("ST_CID_NAV_STATUS_SEND","beacon_id_01",self.send_data_input.text()))

    def ping_command(self):
        
        
        self.seatrac.serial_write(self.seatrac.ping_x150_command("ST_CID_PING_SEND","beacon_id_01","ST_AMSG_REQX"))
    
        
    def seatrac_read_command(self):
        while 1:    
            serial_input=(self.seatrac.serial_read())
            command_encrypt,command_decrypt=self.seatrac.decrypt_command(status=False,command=True)
            if (command_encrypt is not None and command_decrypt is not None)and (command_decrypt["CmdId"]=="ST_CID_PING_RESP" or command_decrypt["CmdId"]=="ST_CID_XCVR_TX_MSG"):
            #if (command_encrypt is not None and command_decrypt is not None):
                
                self.input_data(command_decrypt)
                
    def seatrac_read_status(self):
        #serial_input=(self.seatrac.serial_read())
        seatrac_read_status_flag=True
        while seatrac_read_status_flag:
            status_encrypt,status_decrypt=self.seatrac.decrypt_command(status=True,command=False)
            if (status_encrypt is not None and status_decrypt is not None):
                self.input_data(status_decrypt)
                #print(status_decrypt)
                seatrac_read_status_flag=False
            


    def gps(self):
        _translate = QtCore.QCoreApplication.translate

        while 1:
            try :

                gps_read = self.gps_port.readline().decode()
                msg = pynmea2.parse(gps_read)
                if gps_read.find('GGA') > 0:
                    
                    

                    item = self.gps_table.item(0, 0)
                    item.setText(_translate("MainWindow",str(round(msg.latitude,8))))
                    item = self.gps_table.item(0, 1)
                    item.setText(_translate("MainWindow", str(round(msg.longitude,8))))
                    item = self.gps_table.item(0, 2)
                    item.setText(_translate("MainWindow", str(msg.num_sats)))
                self.gps_table.hide()
                self.gps_table.show()
            except:
                print("wait for gps module" )
                pass

    def random_number(self):
        random_flag=True

        while random_flag:

            random_num={"value": random.randint(0, 100),"value_1": random.randint(0, 100),"value_3": random.randint(0, 100)}

            print(random_num)
            time.sleep(0.5)
            if random_num["value"] %3 ==0:
                
                self.input_data(random_num)
                
                #random_flag=False
                

if __name__ == "__main__":
    #try:
        app = QtWidgets.QApplication(sys.argv)

        window = MainWindow()
        window.show() 
        window.clink_event()
        
        
        
        seatrac_read_thread = threading.Thread(target=window.seatrac_read_command)
        seatrac_read_thread.start()
        
        window.gps_port = serial.Serial(port="COM6", baudrate = 4800)
        gps_read_thread = threading.Thread(target=window.gps)
        gps_read_thread.start()   
        '''
        random_thread = threading.Thread(target=window.random_number)
        random_thread.start()  
        '''
        

    #except:
        #print("some error detected")
        #pass
