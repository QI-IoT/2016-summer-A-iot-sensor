import threading
import time
from bluetooth import *

data = 0
temp = 0

server_sock=BluetoothSocket( RFCOMM )
server_sock.bind(("",PORT_ANY))
server_sock.listen(1)

port = server_sock.getsockname()[1]

uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

advertise_service( server_sock, "SampleServer",
                   service_id = uuid,
                   service_classes = [ uuid, SERIAL_PORT_CLASS ],
                   profiles = [ SERIAL_PORT_PROFILE ],
                    )

class BT_send_Thread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        BT_send_Func()

class BT_recv_Thread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        BT_recv_Func()


def BT_send_Func():
    while True:
        if int(data) == 1:
            client_sock.send("temperature = {0:.1f} C".format(temp))
            time.sleep(1)
        elif int(data) == 2:
            pass


def BT_recv_Func():
    print("Waiting for connection on RFCOMM channel %d" % port)
    client_sock, client_info = server_sock.accept()
    print("Accepted connection from ", client_info)
    try:
        while True:
            data = client_sock.recv(1024)
            if len(data) == 0: break
            print("received [%s]" % data)
    except IOError:
        pass



BT_send_process = BT_send_Thread()
BT_recv_process = BT_recv_Thread()

BT_send_process.start()
BT_recv_process.start()

while 1:
    raw = int(open("/sys/bus/iio/devices/iio:device0/in_voltage0_raw").read())
    scale = float(open("/sys/bus/iio/devices/iio:device0/in_voltage_scale").read())
    vout = raw * scale
    v20 = 345
    temp = vout - v20 + 20
