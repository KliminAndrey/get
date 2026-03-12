import smbus
import time

class MCP3021:
    def __init__(self, dynamic_range, verbose=False):
        self.bus = smbus.SMBus(1)
        self.dynamic_range = dynamic_range
        self.address = 0x4D
        self.verbose = verbose

    def deinit(self):
        self.bus.close()

    def get_number(self):
        data = self.bus.read_word_data(self.address, 0)
        lower_data_byte = data >> 8
        upper_data_byte = data & 0xFF
        
        number = (upper_data_byte << 6) | (lower_data_byte >> 2)
        if self.verbose:
            print(f"Принятые данные: {data}, Старший байт: {upper_data_byte:#04x}, Младший байт: {lower_data_byte:#04x}, Число: {number}")
        return number

    def get_voltage(self):
        num = self.get_number()
        voltage = self.dynamic_range * num / 1023
        if self.verbose:
            print(f"Напряжение: {voltage:.3f} V")
        return voltage

if __name__ == "__main__":
    DYNAMIC_RANGE = 5.2

    adc = MCP3021(DYNAMIC_RANGE, True)

    try:
        while True:
            v = adc.get_voltage()
            print(v)
            time.sleep(1)
    finally:
        adc.deinit()