import RPi.GPIO as GPIO
import time


class R2R_ADC:
    def __init__(self, dynamic_range, compare_time = 0.01, verbose = False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time
        
        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.comp_gpio, GPIO.IN)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial = 0)
        
    
    def deinit(self):
        GPIO.output(self.bits_gpio, 0)
        GPIO.cleanup()

    def number_to_dac(self, number):
        GPIO.output(self.bits_gpio, [int(i) for i in bin(number)[2:].zfill(8)])

    def sequential_counting_adc(self):
        for i in range(2**8):
            self.number_to_dac(i)
            time.sleep(self.compare_time)
            v = GPIO.input(self.comp_gpio)

            # print(f't {i} { v}')
            if GPIO.input(self.comp_gpio) == 1:
                return i
        return 2**8 - 1

    def get_sc_voltage(self):
        num = self.sequential_counting_adc()
        if self.verbose:
            print(num)
        v = self.dynamic_range * num / (2**8-1)
        return v

if __name__ == "__main__":
    try:
        adc = R2R_ADC(3.29, verbose=False)
        
        while True:
            try:
                print(adc.get_sc_voltage())
            except ValueError:
                print("error\n")

    finally:
        adc.deinit()