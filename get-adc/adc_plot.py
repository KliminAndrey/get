import matplotlib.pyplot as plt

def plot_voltage_vs_time(time, voltage, max_voltage):
    plt.figure(figsize=(10, 6))
    plt.plot(time, voltage)
    plt.title('U(t)')
    plt.xlabel('t, с')
    plt.ylabel('U, В')
    plt.xlim(0, max(time))
    plt.ylim(0, max_voltage * 1.05)
    plt.grid(True)
    plt.show()
    
    
def plot_sampling_period_hist(time):
    sampling_periods = [time[i+1] - time[i] for i in range(len(time)-1)]
    plt.figure(figsize=(10, 6))
    plt.hist(sampling_periods)
    plt.title('Распределение измерений по времени')
    plt.xlabel('t, с')
    plt.ylabel('n')
    plt.xlim(0, 0.06)
    plt.grid(True)
    plt.show()