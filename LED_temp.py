from neo import Gpio
import threading
import time

#init
neo = Gpio()
pinNum = [2,3]
check_Flag = 0
count = 100

#setting pinmdoe
for i in range(2):
    neo.pinMode(pinNum[i], neo.OUTPUT)

class LED_Thread (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        LED_Func()

def LED_Func():
    while 1:
        if check_Flag == 2:
            neo.digitalWrite(3, 0)
            neo.digitalWrite(2, 1)
        elif check_Flag == 3:
            neo.digitalWrite(2, 0)
            neo.digitalWrite(3, 1)
        elif check_Flag == 0:
            neo.digitalWrite(2, 0)
            neo.digitalWrite(3, 0)

LED_Process = LED_Thread()
LED_Process.start()

while count:
    raw = int(open("/sys/bus/iio/devices/iio:device0/in_voltage0_raw").read())
    scale = float(open("/sys/bus/iio/devices/iio:device0/in_voltage_scale").read())
    vout = raw * scale
    v20 = 345
    temp = vout - v20 + 20

    if temp <= 26:
        check_Flag = 2
    elif temp >= 40:
        check_Flag = 3
    else:
        check_Flag = 0

    print ("input voltage = {0:.4f} mV".format(vout))
    print ("temperature = {0:.1f} C".format(temp))
    time.sleep(1)
    count -= 1
