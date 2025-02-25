import serial
from adafruit_pn532.uart import PN532_UART

#opepens the UART serial bus in raspi /dev/serial0
uart_bus=serial.Serial("/dev/serial0", baudrate=115200, timeout=2)

#obejct pn532 to mniuplate de nfc card
lector=PN532_UART(uart_bus, debug=False)

#configure de nfc card as reader
lector.SAM_configuration()
ic, ver, rev, support=lector.firmware_version

print (f"El lector esta llest (firmware {ver}.{rev})")

while(True):

        uid=lector.read_passive_target(timeout=5)
        if (uid):
                uid_conv=''.join([hex(byte)[2:].upper().zfill(2) for byte in uid])
                print(f"UID: {uid_conv}")
                break
        else:
                print("Apropa una targeta al lector")
