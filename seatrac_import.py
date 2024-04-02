

import sys

from PyQt5.QtCore import QObject, QThread, pyqtSignal
import seatrac_serial

class seatrac_import(QObject,object):
    #def __init__(self, *args, obj=None, **kwargs):
        
        #super(seatrac_import, self).__init__(*args, **kwargs)



    seatrac=seatrac_serial.Setrac_serial(MODEL="x150",COM_PORT="/dev/tty.usbserial-FT51FT0U",BAUD_RATE=115200)


    def seatrac_read(self):

        while 1:

            serial_input=(self.seatrac.serial_read())
            status_encrypt,status_decrypt=self.seatrac.decrypt_command(status=True,command=False)
            command_encrypt,command_decrypt=self.seatrac.decrypt_command(status=False,command=True)
            if (status_encrypt is not None and status_decrypt is not None) :
                print(status_decrypt)
            if (command_encrypt is not None and command_decrypt is not None):
                print(command_decrypt)
 
    def seatrac_write(self,command,payload):
        if command == "ping":
            self.seatrac.serial_write(self.seatrac.ping_x150_command("ST_CID_PING_SEND","beacon_id_01","ST_AMSG_REQX"))
        elif command == "data":
            self.seatrac.serial_write(self.seatrac.send_data_x150_command("ST_CID_NAV_STATUS_SEND","beacon_id_01",payload))