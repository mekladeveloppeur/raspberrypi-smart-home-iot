from sensors import dht11
from sensors import mq2

while True:

    t, h = dht11.read_dht()

    if t:
        print("Temp:", t)

    if mq2.gas_detect():
        print("Gas detected")
