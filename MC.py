import random
import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def draw_square():
    global insum
    square = plt.Rectangle((0, 0), 1, 1, fc='b')  # 创建一个蓝色正方形
    plt.gca().add_patch(square)  # 添加正方形到当前图形
    n = 100000
    T=[0]*n
    # 随机生成一系列横坐标和纵坐标
    X = np.random.uniform(0, 1, n)
    Y = np.random.uniform(0, 1, n)
    # 设置点的颜色
    for i in range(n):
        if pow(X[i]*X[i]+Y[i]*Y[i],0.5)<1:
            T[i]=1
            insum=insum+1
        else:
            T[i]=100
    # 绘制散点
    plt.scatter(X, Y,c=T,s=1)
    plt.axis('scaled')  # 设置坐标轴比例相等

    plt.text(0, 1.1, "π="+str(insum/n*4),size=14)
    plt.show()

insum=0
draw_square()

