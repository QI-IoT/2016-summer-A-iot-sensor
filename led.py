from neo import Gpio
from time import sleep

neo = Gpio()

pinNum = [0,1,2,3]

for i in pinNum:
    neo.pinMode(pinNum[i], neo.OUTPUT)

for x in range(15):
    num = [0,0,0,0]
    t = x + 1
    for y in range(4):
        num[y] = t%2
        t = t/2

    neo.digitalWrite(pinNum[3], num[3])
    neo.digitalWrite(pinNum[2], num[2])
    neo.digitalWrite(pinNum[1], num[1])
    neo.digitalWrite(pinNum[0], num[0])
    sleep(1)
