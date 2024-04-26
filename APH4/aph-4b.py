#PES1UG22EC321
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def continuous_time_signal(t):
                                                                                                                         #PES1UG22EC302 Sushant R Naik
    return 2 * np.cos(6 * np.pi * t + 0.1) + 2 * np.cos(10 * np.pi * t + 0.2)

def ideal_sampling(signal, fs, Ts):
    # Ideal sampling of continuous-time signal
    sampled_indices = np.arange(0, len(signal), int(fs * Ts))
    sampled_signal = signal[sampled_indices]
    sampled_time = np.arange(0, len(signal), int(fs * Ts)) / fs
    return sampled_time, sampled_signal

def ideal_reconstruction(sampled_time, sampled_signal, fs):
    # Ideal reconstruction using a low-pass filter
    reconstructed_signal = signal.lfilter([1], [1, 0], sampled_signal)
    reconstructed_time = np.linspace(0, sampled_time[-1], len(reconstructed_signal))
    return reconstructed_time, reconstructed_signal

# Parameters
fs_original = 1000  # Original continuous-time signal frequency
Ts_original = 1/fs_original  # Original continuous-time signal sampling interval

# Generate continuous-time sinc signal
t_continuous = np.linspace(0, 1, 1000)
signal_continuous = continuous_time_signal(t_continuous)

# Ideal sampling
fs_sampled = 100 * fs_original  # Choose sampling frequency (e.g., 100 times higher)
Ts_sampled = 1/fs_sampled
sampled_time, sampled_signal = ideal_sampling(signal_continuous, fs_sampled, Ts_sampled)

# Ideal reconstruction
reconstructed_time, reconstructed_signal = ideal_reconstruction(sampled_time, sampled_signal, fs_sampled)

# Plotting
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(t_continuous, signal_continuous, label='Continuous-Time Signal')
plt.title('Continuous-Time Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()

plt.subplot(3, 1, 2)
plt.stem(sampled_time, sampled_signal, markerfmt='ro', basefmt='r', label='Sampled Signal')
plt.title('Sampled Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(reconstructed_time, reconstructed_signal, label='Reconstructed Signal')
plt.title('Reconstructed Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()

plt.tight_layout()
plt.show()