import sys
from PyQt5 import QtWidgets, uic,QtCore, QtGui
from PyQt5.QtCore import QObject, QThread, pyqtSignal
import random
from mainwindow import Ui_MainWindow
#from seatrac_import import seatrac_import


#random_num=None
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        
        super(MainWindow, self).__init__(*args, **kwargs)
        
        self.setupUi(self)
        #input_data={"Game" : 1, "Akshat" : "asdsdfsd", "Akash" : 3,"Agfkash" : 4}
        #self.seatrac=seatrac_import()
        #self.seatrac_read_thread()
        #self.random_thread()
        #self.input_thread()
        
    
    def input_data(self,input):
        
       
        #global random_num
        #print(random_num)
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

        self.ping_command_btn.clicked.connect(self.ping_command)
        #self.send_data_command_btn.clicked.connect(self.send_data_command)
    def clink_event(self):
        self.ping_command_btn.clicked.connect(self.ping_command)
        #self.send_data_command_btn.clicked.connect(self.send_data_command)

    def send_data_command(self):
        
        self.seatrac.seatrac_write(command="ping",payload=None)

    def ping_command(self):
        
        random_num={"value": random.randint(0, 100)}
        self.input_data(random_num)

    def seatrac_read_thread(self):
        # Step 2: Create a QThread object
        self.thread = QThread()
        # Step 3: Create a worker object
        #self.worker = Worker()
        # Step 4: Move worker to the thread
        self.seatrac.moveToThread(self.thread)
        # Step 5: Connect signals and slots
        self.thread.started.connect(self.seatrac.seatrac_read)

   
        # Step 6: Start the thread
        self.thread.start()
    
    def random_thread(self):
        self.thread = QThread()
        # Step 3: Create a worker object
        self.worker = random_class()
        # Step 4: Move worker to the thread
        self.worker.moveToThread(self.thread)
        # Step 5: Connect signals and slots
        self.thread.started.connect(self.worker.random_dict)
        self.thread.start()



global random_num,window
random_num=0
class random_class(QObject):
    def random_dict(self):
        
        import time
        global window
        while 1:
            #random_num={"value": random.randint(0, 100)}
            time.sleep(1)
            print(random_num)
            #window.clink_event(random_num)
            window.input_data(random_num)
        
            

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()
    window.clink_event()
    #window.random_thread(window.input_data)
    app.exec()
