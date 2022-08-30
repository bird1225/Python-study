# @Author  : 汪凌峰（Eric Wang）
# @Date    : 2022/6/15

import numpy as np
import pylab as pl


def fft_combine(freqs, n, loops=1):
    length = len(freqs) * loops
    data = np.zeros(length)
    index = loops * np.arange(0, length, 1.0) / length * (2 * np.pi)
    for k, p in enumerate(freqs[:n]):
        if k != 0: p *= 2  # 除去直流成分之外，其余的系数都*2
        data += np.real(p) * np.cos(k * index)  # 余弦成分的系数为实数部
        data -= np.imag(p) * np.sin(k * index)  # 正弦成分的系数为负的虚数部
    return index, data


# 产生size点取样的三角波，其周期为1
# def triangle_wave(size):
#    x = np.arange(0, 1, 1.0/size)
#    y = np.where(x<0.5, x, 0)
#    y = np.where(x>=0.5, 1-x, y)
#    return x, y


# 产生size点取样的方波，其周期为1
def square_wave(size):
    x = np.arange(0, 1, 1.0 / size)
    y = np.where(x < 0.5, 1.0, 0)
    return x, y


fft_size = 256

# 计算方波和其FFT
x, y = square_wave(fft_size)
fy = np.fft.fft(y) / fft_size

# 绘制三角波的FFT的前20项的振幅，由于不含下标为偶数的值均为0， 因此取
# log之后无穷小，无法绘图，用np.clip函数设置数组值的上下限，保证绘图正确
pl.figure()
# np.clip(x,3,8):给数值设定范围，对于小于3的数，全部变成3，大于8的数全部变成8
pl.plot(np.clip(20 * np.log10(np.abs(fy[:20])), -120, 120), "o")
pl.xlabel("frequency bin")
pl.ylabel("power(dB)")
pl.title("FFT result of triangle wave")

# 绘制原始的三角波和用正弦波逐级合成的结果，使用取样点为x轴坐标
pl.figure()
pl.plot(y, label="original triangle", linewidth=2)
for i in [0, 1, 3, 5, 7, 9]:
    index, data = fft_combine(fy, i + 1, 2)  # 计算两个周期的合成波形
    pl.plot(data, label="N=%s" % i)
pl.legend()
pl.title("partial Fourier series of triangle wave")
pl.show()
