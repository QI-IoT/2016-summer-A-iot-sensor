from neo import Gpio
import threading
import time

#init
neo = Gpio()
pin_Num = [2,3]
exit_Flag = 0

#setting pinmdoe
for i in range(2):
    neo.pinMode(pin_Num[i], neo.OUTPUT)

#threading class
class myThread (threading.Thread):
    def __init__(self, name, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay
    def run(self):
        print_time(self.name, self.delay, 10)

def print_time(threadName, delay, counter):
    while counter:
        if exit_Flag:
            threadName.exit()

        neo.digitalWrite(int(threadName),1)
        time.sleep(delay)
        neo.digitalWrite(int(threadName),0)
        time.sleep(delay)
        counter -= 1

#create treading
thread1 = myThread(2, 1) #blinking per 1sec
thread2 = myThread(3, 3) #blinking per 3sec

thread1.start()
thread2.start()
