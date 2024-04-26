# -*- coding: utf-8 -*-
"""
Created on Wed Oct 03 19:01:11 2018

Generation and demodulation of DSB-SC signal

@author: Vamsi Krishna
"""

# PLOT POWER SPECTRUM
from scipy import signal
from scipy.signal import butter, lfilter
import numpy as np
import matplotlib.pyplot as plt

N = 1e5 # Number of samples for visualization as a waveform
Ac = 1 # Carrier peak amplitude 
Am = 0.5 # Message signal peak amplitude
freq_c = 10e3 # carrier frequency
freq_m = 500 # message frequency
fs = 2.5*(freq_c+freq_m) # sampling frequency is at least twice the highest frequency

def butter_lowpass(cutoff, fs, order=4):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq # the critical frequencies must be normalized
    b, a = butter(order, normal_cutoff, btype='lowpass', analog=False)
    return b, a

def butter_lowpass_filter(data, cutoff, fs, order=4):
    b, a = butter_lowpass(cutoff, fs, order=order) # a and b coefficients of the LPF modeled as FIR/IIR filter
    y = lfilter(b, a, data) # filter output
    return y

order=4
cutoff=freq_m

time = np.arange(N) / fs # time instants of the samples of duration (1/fs) seconds
c = Ac*np.cos(2*np.pi*freq_c*time) # Carrier signal
m = Am*np.cos(2*np.pi*freq_m*time) # Message signal
s= m*c # DSB-SC signal
y=s*c # product modulator output at receiver

x = butter_lowpass_filter(y, cutoff, fs, order) # demodulated signal

#
#### Either use signal.welch or signal.spectrogram
# Set first argument to s, y or x to see the spectrum of DSBSC wave, product modulator output at the receiver or demodulated signal
f, Pxx_spec = signal.welch(s, fs, 'flattop', 1024, scaling='spectrum',return_onesided=True) # for two sided spectrum set False
# f, t, Pxx_spec = signal.spectrogram(s, fs)

plt.figure()
plt.plot(f,np.sqrt(Pxx_spec)) # magnitude spectrum
# plt.plot(f,Pxx_spec) # power spectrum
#plt.semilogy(f, np.sqrt(Pxx_spec)) # magnitude spectrum in decibels (20*log_10(value))
plt.xlabel('frequency [Hz]')
plt.ylabel('Magnitude')
plt.title('Power spectrum')
plt.show()

plt.plot(time[0:200],x[0:200]) # demodulated signal waveform
plt.xlabel('Time (seconds)')
plt.ylabel('Voltage [volts]')
plt.title('Demodulated signal')
plt.grid()

