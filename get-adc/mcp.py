import time
from mcp3021_driver import MCP3021
from adc_plot import plot_voltage_vs_time, plot_sampling_period_hist

DYNAMIC_RANGE = 5.02

adc = MCP3021(DYNAMIC_RANGE, verbose=False)

voltage_values = []
time_values = []

try:
    start_time = time.time()
    while time.time() - start_time < 3:
        v = adc.get_voltage()
        t = time.time() - start_time
        voltage_values.append(v)
        time_values.append(t)
    
    plot_voltage_vs_time(time_values, voltage_values, DYNAMIC_RANGE)
    plot_sampling_period_hist(time_values)

finally:
    adc.deinit()