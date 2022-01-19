from bluepy import btle

value = [0]*30


class MyDelegate(btle.DefaultDelegate):
    def __init__(self):
        btle.DefaultDelegate.__init__(self)
        # ... initialise here

    def handleNotification(self, cHandle, data):
        # ... perhaps check cHandle
        # ... process 'data'
        #print(type(data))
        #print(dir(data))
        print(data)
        print(data[0])
        
        value.pop(0)
        value.append(data[0])
        
# Initialisation  -------
address = "ED:E0:B7:80:25:96"
service_uuid = "27763b10-999c-4d6a-9fc4-c7272be10900"
char_uuid = "27763b21-999c-4d6a-9fc4-c7272be10900"

p = btle.Peripheral(address)
p.setDelegate(MyDelegate())

# Setup to turn notifications on, e.g.
svc = p.getServiceByUUID(service_uuid)
ch = svc.getCharacteristics(char_uuid)[0]

"""
setup_data for bluepy noification-
"""
#setup_data = b"\x01\x00"
#ch.write(setup_data)
#p.writeCharacteristic(ch.valHandle + 1, setup_data)

ch_data = p.readCharacteristic(ch.valHandle + 1)
print(type(ch_data))
print(ch_data)

print("=== Main Loop ===")

while True:
    if p.waitForNotifications(1.0):
        # handleNotification() was called
        continue

    #print("Waiting...")
    # Perhaps do something else here



    sudo gatttool -b ED:E0:B7:80:25:96 -t random -I



import asyncio
from bleak import BleakClient

address = "ED:E0:B7:80:25:96"
MODEL_NBR_UUID = "27763b10-999c-4d6a-9fc4-c7272be10900"

async def main(address):
    async with BleakClient(address) as client:
        model_number = await client.read_gatt_char(MODEL_NBR_UUID)
        print("Model Number: {0}".format("".join(map(chr, model_number))))

asyncio.run(main(address))