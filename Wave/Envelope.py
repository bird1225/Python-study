# @Author  : 汪凌峰（Eric Wang）
# @Date    : 2022/8/23
#包络解调程序
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.fftpack import hilbert,fft,ifft
path = r'C:\Users\Deng\Desktop\测试\4.txt'
data = pd.read_csv(path,header=None)           #读取数据
fs = 25600                                     #采样频率
n = 1                                          #选择分析列数
fmin = 1000                                     #选取频率范围：最小
fmax = 8000                                    #选取频率范围：最大
m = len(data)
f = np.arange(0,m)*fs/m                        #频域波形很坐标 ：频率
f_half = f[0:int(np.round(m / 2))]             #取一半
fmin_number = int(np.round(fmin*m/fs))         #获取点数
fmax_number = int(np.round(fmax*m/fs))
y_new = [0*i for i in range(m)]                #快速创建一个元素为0的列表
y = np.array(data[n-1])
y_fft = fft(y)                                 #fft
y_new[fmin_number:fmax_number] = y_fft[fmin_number:fmax_number]             #替换元素
y_new[m-fmax_number:m-fmin_number] = y_fft[m-fmax_number:m-fmin_number]     #替换元素
y_ifft = ifft(y_new).real                                                   #逆变换并取复数的实部
H = np.abs(hilbert(y_ifft)-np.mean(y_ifft))                                 #包络
HP = np.abs(fft(H-np.mean(H)))*2/m
HP_half = HP[0:int(np.round(m / 2))]                                         #取一半
plt.figure()
plt.plot(f_half,HP_half)
plt.xlim([0,800])
plt.grid(linestyle = '--')
plt.show()
