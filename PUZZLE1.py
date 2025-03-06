import serial
from adafruit_pn532.uart import PN532_UART

class Rfid:
    def __init__(self, uart_port="/dev/serial0", baudrate=115200):
        # uart bus prev config
        self.uart_port = serial.Serial(uart_port, baudrate=baudrate, timeout=2)

        # PN532 object
        self.lector = PN532_UART(self.uart_port, debug=False)

        # lector config as card reader
        self.lector.SAM_configuration()

        # prev checks
        ic, ver, rev, support = self.lector.firmware_version
        print (f"versio firmware {ver}.{rev}")

    def read_uid(self):
        while True:
          uid=self.lector.read_passive_target(timeout=2)
          if uid:
            return ''.join([hex(byte)[2:].upper().zfill(2) for byte in uid])
          else:
            print("Apropa la targeta!")

if __name__ == "__main__":
    rf=Rfid()
        uid=rf.read_uid()
        print(f"El UID: {uid}")
        
