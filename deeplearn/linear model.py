import numpy as np  #arange创建均匀间隔的数值序列（等差数列）
import matplotlib.pyplot as plt
x_data = [1.0,2.0,3.0]
y_data = [2.0,4.0,6.0]
def forward(x):  #定义前馈函数
    return x * w
def loss(x,y):  #定义损失函数
    y_pred = forward(x)
    return (y_pred -y) * (y_pred -y)
w_list = []
mse_list = []  #均方误差列表
for w in np.arange(0.0,4.1,0.1):  #生成的序列是：0.0, 0.1, 0.2, ..., 3.9, 4.0
                                  #与Python的range()不同，np.arange支持浮点数步长
                                  # w 表示线性模型的斜率，即y = wx,从0到4一个一个试
    print('w=',w)  #print(f"w={w:.2f}")
    l_sum = 0
    for x_val, y_val in zip(x_data, y_data):  #一一对应  1.0,2.0  2.0,4.0
        y_pred_val = forward(x_val)
        loss_val = loss(x_val, y_val)
        l_sum += loss_val
        print('\t',x_val,y_val,y_pred_val, loss_val)
    print('MSE=',l_sum / 3)
    w_list.append(w)
    mse_list.append(l_sum / 3)

plt.plot(w_list, mse_list) #绘制折线图 横坐标 纵坐标
plt.ylabel('Loss')  #设置 Y 轴标签
plt.xlabel('w')  #设置 X 轴标签
plt.show()
