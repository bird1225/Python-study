import numpy as np
import scipy.signal as signal
import scipy.interpolate as inter
import scipy.integrate as integrate
import scipy.fftpack as fft
import matplotlib.pyplot as plt


def Orderspectrum(x, Fs, rpm):
    """
    Calculate the order sprectrum of the selected waveform


    parameters
    ----------
    x: array-like
    Fs: Float, Sampling Frequency
    rpm: array-like
    """
    L = len(x)
    t = np.linspace(1 / Fs, L / Fs, L)
    Omax = Fs / (2 * max(rpm / 60))
    fsp = 4 * (2 * Omax)  # sampling frequency
    upFactor = 15  # Upsampling factor = 15 !
    xUp = signal.resample(x, upFactor * L)
    timeUp = np.arange(0, len(xUp)) / (upFactor * Fs)
    f_rpmUP = inter.interp1d(t, rpm, kind='linear', fill_value='extrapolate')
    rpmUP = f_rpmUP(timeUp)
    phaseUP = integrate.cumtrapz(rpmUP / (60 * upFactor * Fs), initial=0)
    constPhase = np.linspace(phaseUP[0], phaseUP[-1], int(phaseUP[-1] * fsp))
    K2 = (np.diff(phaseUP) > 0)
    strickincridx = np.array(np.zeros(len(phaseUP)))
    strickincridx[0] = True
    strickincridx[1:] = K2
    strID = np.array([strickincridx], dtype=bool).flatten()
    phaseUP = phaseUP[strID]
    f_xp = inter.interp1d(phaseUP, xUp, kind='linear', fill_value='extrapolate')
    xp = f_xp(constPhase)

    w = np.hamming(len(xp))
    y_order = fft.fft(xp * w) / len(xp)
    y_order = abs(y_order)[:len(y_order) // 2]
    L_order = np.ceil(len(y_order) * Omax / fsp)
    x_order = np.linspace(0, fsp * L_order / len(y_order) / 2, int(L_order))
    y_order = y_order[:int(L_order)]

    plt.figure()
    plt.plot(x_order, y_order, 'b')
    plt.title('Order Spectrum')
    plt.ylabel('Power')
    plt.xlabel('Order [num]')
    plt.grid()
    plt.show()

    return x_order, y_order




## Case 1
#
# import array
# import wave
# import math
#
# def sinesweep(f0, f1, sweeptime, samplingrate, peak):
#     k = math.exp(math.log(float(f1) / f0) / sweeptime)
#     data_len = sweeptime * samplingrate
#     data = array.array('i', [0] * data_len)
#     dt = 1.0 / samplingrate
#     t = 0.0
#     p = 2 * math.pi * f0 / math.log(k)
#     for i in range(data_len):
#         data[data_len - i - 1] = int(peak * math.sin(p * (pow(k, t) - 1)))
#         t += dt
#     return data
#
#
# def sindata(f0, time, samplingrate, peak):
#     data = [int(peak * math.sin(2 * math.pi * f0 * x / samplingrate)) for x in range(int(time * samplingrate))]
#     return array.array('h', data)
#
# SAMPLING_RATE = 1024
# SWEEP_TIME = 2
# F0 = 20
# F1 = 25
# PEAK = 0x2000
# data1 = sinesweep(F0, F1, SWEEP_TIME, SAMPLING_RATE, PEAK)
# data2 = sinesweep(50, 55, SWEEP_TIME, SAMPLING_RATE, PEAK)
# data = np.array (data1) + np.array (data2)
# yf = fft.fft(data)
# P2 = np.abs(yf / len(yf))
# P1 = P2[0:int((len(yf) / 2))]
#
# P1[1:-2] = 2 * P1[1:-2]
# xf = fft.fftfreq(len(data), 1 / SAMPLING_RATE)[:int(len(data) / 2)]  #
# plt.figure()
# plt.subplot(2, 1, 1)
# plt.title("sweep data")
# plt.plot(data)
# plt.subplot(2, 1, 2)
# plt.plot(xf, P1)
# plt.show()
#
#
# rpm = np.arange(20, 25, 5/2048)
# rpm = rpm * 60
# Orderspectrum(data, SAMPLING_RATE, rpm)



## Case 2

import math
fs = 600
t1 = 5
t = np.arange(0, t1, 1/fs)
f0 = 10
f1 = 40
rpm = 60 * np.linspace(f0, f1, len(t))

o1 = 1
o2 = 0.5
o3 = 4
o4 = 6

a1 = 1
a2 = 0.5
a3 = np.sqrt(2)
a4 = 2

ph = 2 * math.pi * integrate.cumtrapz(rpm/60)/fs

test = np.dot(np.array([o1, o2, o3, o4]).reshape((4, 1)), ph.reshape((1, -1)))
test3 = np.cos(test)
x2 = np.dot(np.array([a1, a2, a3, a4]).reshape((1, 4)), test3)
plt.figure()
plt.plot(x2.flatten())
plt.show()

yf = fft.fft(x2.flatten())
P2 = np.abs(yf / len(yf))
P1 = P2[0:int((len(yf) / 2))]

P1[1:-2] = 2 * P1[1:-2]
xf = fft.fftfreq(len(x2.flatten()), 1 / fs)[:int(len(x2.flatten()) / 2)]  #
plt.plot(xf, P1)



Orderspectrum(x2.flatten(), fs, rpm[1:])

