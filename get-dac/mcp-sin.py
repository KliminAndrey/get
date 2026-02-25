import mcp4725_driver as mcp
import signal_generator as sg
import time

amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000

if __name__ == "__main__":
    try:
        mcp1 = mcp.MCP4725(5)
         
        while True:
            val = sg.get_sin_wave_amplitude(signal_frequency, time.time())
            # print(val)
            mcp1.set_voltage(amplitude * val)
            sg.wait_for_sampling_period(sampling_frequency)

    finally:
        mcp1.deinit()

