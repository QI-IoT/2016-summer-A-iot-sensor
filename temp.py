import time

count = 20

while count:
    raw = int(open("/sys/bus/iio/devices/iio:device0/in_voltage0_raw").read())
    scale = float(open("/sys/bus/iio/devices/iio:device0/in_voltage_scale").read())
    vout = raw * scale
    v20 = 345
    temp = vout - v20 + 20
    
    print ("input voltage = {0:.4f} mV".format(vout))
    print ("temperature = {0:.1f} C".format(temp))
    time.sleep(1)
    count -= 1
