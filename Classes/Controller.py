import serial

class Controller:
    port = ""
    baud = 9600
    ser = None
    commands = {
        "FORWARD": 'w'
        "BACK": 's'
        "ROT_RIGHT": 'e'
        "ROT_LEFT": 'q'
        "STRAFE_RIGHT": 'd'
        "STRAFE_LEFT": 'a'
    }
    def __init___(self, port, baud):
        self.baud = baud
        self.port = port
        self.ser = serial.Serial()
        self.ser.baud = self.baud
        self.ser.port = self.port
        self.ser.open()
        pass

    def write_2_serial(self, command)
        to_send = self.commands.get(command,"NOTCOM")
        if (to_send != "NOTCOM"):
            self.ser.write(to_send)