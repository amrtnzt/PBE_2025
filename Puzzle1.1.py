class Rfid:
    def __init__(self, uart_port="/dev/serial0", baudrate=115200):
      import serial
      from adafruit_pn532.uart import PN532_UART

      #opepens the UART serial bus in raspi /dev/serial0
      uart_bus=serial.Serial(uart_port, baudrate=baudrate, timeout=2)

      #obejct pn532 to mniuplate de nfc card
      lector=PN532_UART(uart_bus, debug=False)

      lector.SAM_configuration()
      ic, ver, rev, support=lector.firmware_version()

      print (f"El lector esta llest (firmware {ver}.{rev})")
      
    def read_uid(self):
      uid=lector.read_passive_target(timeout=4)
      uid_conv=''.join([hex(byte)[2:].upper().zfill(2) for byte in uid])
      if uid 
        return uid_conv
      return "No s'ha detectat cap targeta"

if __name__=="__main__":
  rf=Rfid()
  uid=read_uid()
  print(uid)
    

