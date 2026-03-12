import time
from r2r_adc import R2R_ADC
from adc_plot import plot_voltage_vs_time, plot_sampling_period_hist

DYNAMIC_RANGE = 3.29

adc = R2R_ADC(dynamic_range=DYNAMIC_RANGE, compare_time=0.0001, verbose=False)

voltage_values = []
time_values = []

try:
    start_time = time.time()
    while time.time() - start_time < 3.0:
        v = adc.get_sc_voltage()
        t = time.time() - start_time
        voltage_values.append(v)
        time_values.append(t)
    
    plot_voltage_vs_time(time_values, voltage_values, DYNAMIC_RANGE)
    plot_sampling_period_hist(time_values)

finally:
    adc.deinit()