import torch
import torch.nn.functional as F
import numpy as np
import matplotlib.pyplot as plt

x_data = torch.Tensor([[1.0], [2.0], [3.0]])
y_data = torch.Tensor([[0.0], [0.0], [1.0]])

# -------------------------------------------------------#
class LogisticRegressionModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        # 对输入张量 x 执行线性计算  输出 = x @ 权重矩阵^T + 偏置项
        self.linear = torch.nn.Linear(1, 1)


    def forward(self, x):
        y_pred = F.sigmoid(self.linear(x))  #激活函数
        return y_pred


model = LogisticRegressionModel()
# -------------------------------------------------------#
criterion = torch.nn.BCELoss(reduction='sum')  #交叉熵损失函数
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
# -------------------------------------------------------#

for epoch in range(1000):
    y_pred = model(x_data)  #自动调用__init__(self):
    loss = criterion(y_pred, y_data)
    print(epoch, loss.item())
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

x = np.linspace(0, 10, 200)  #生成测试数据 生成的数组：[0.0, 0.05025..., 10.0]（公差 ≈ 0.05025）
x_t = torch.Tensor(x).view((200, 1))  # 转换为PyTorch张量
y_t = model(x_t)
y = y_t.data.numpy()  #结果转回NumPy

plt.plot(x, y)
plt.plot([0, 10], [0.5, 0.5], c='r')
plt.xlabel('Hours')
plt.ylabel('Probability of Pass')
plt.grid()
plt.show()