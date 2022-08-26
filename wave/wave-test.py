# @Author  : 汪凌峰（Eric Wang）
# @Date    : 2022/6/20

import matplotlib.pyplot as plt
# import cv2
import numpy as np

# 画3d分段函数


x = np.linspace(0, 2 * np.pi, 100)
seg1 = [1 if (i < np.pi) else 0 for i in x]
seg2 = [1 if (i >= np.pi) else 0 for i in x]
y = np.linspace(0, 0, 100)
z = 1 * seg1 + 0 * seg2

# 用三个波的叠加模拟阶梯函数，也可以说是阶梯函数分解的前三个波
y1 = np.linspace(1, 1, 100)
z1 = 4 / np.pi * np.sin(x)  # 第一个波

y2 = np.linspace(2, 2, 100)
z2 = z1 + 4 / (3 * np.pi) * np.sin(3 * x)  # 第二个波

y3 = np.linspace(3, 3, 100)
z3 = z2 + 4 / (5 * np.pi) * np.sin(5 * x)  # 第三个波

fig = plt.figure( figsize=(20,10) )
ax = fig.gca(projection='3d')
ax.plot(x, y, z, label='z=1 (0<x<pi) \nz=0 (pi<x<2*pi)')
ax.plot(x, y1, z1, label='z=4/np.pi*np.sin(x)')
ax.plot(x, y2, z2, label='z=4/np.pi*np.sin(x)+4/(3*np.pi)*np.sin(3*x)')
ax.plot(x, y3, z3, label='z=4/np.pi*np.sin(x)+4/(3*np.pi)*np.sin(3*x)+4/(5*np.pi)*np.sin(5*x)')
ax.legend()
plt.show()
# cv2.waitKey(0)
