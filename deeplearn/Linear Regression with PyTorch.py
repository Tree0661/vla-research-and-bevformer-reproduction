import torch

x_data = torch.Tensor([[1.0], [2.0], [3.0]])  #三行一列，二维张量  PyTorch 的神经网络层要求输入是 二维张量
y_data = torch.Tensor([[2.0], [4.0], [6.0]])


class LinearModel(torch.nn.Module): #继承父类 torch.nn.Module
    def __init__(self): # __init__方法
        super().__init__()  # 调用父类的__init__方法 语法：super().成员对象/方法()

        # 创建一个可调用的对象，一个线性层 必须使用self.开头
        self.linear = torch.nn.Linear(1, 1)


    def forward(self, x): # forward方法
        y_pred = self.linear(x)
        return y_pred

model = LinearModel() #创建模型对象

criterion = torch.nn.MSELoss(reduction='sum') # 损失函数 reduction='sum' 表示对所有样本的损失求和
optimizer = torch.optim.SGD(model.parameters(), lr=0.01) # 随机梯度下降 优化器
                                                         # w = w - lr * ∂loss/∂w
                                                         # b = b - lr * ∂loss/∂b

for epoch in range(1000):
    y_pred = model(x_data)
    loss = criterion(y_pred, y_data)
    print(epoch, loss.item())

    optimizer.zero_grad() # 梯度清零
    loss.backward()
    optimizer.step()

print('w = ', model.linear.weight.item())
print('b = ', model.linear.bias.item())

x_test = torch.Tensor([[4.0]])
y_test = model(x_test)
print('y_pred = ', y_test.data)