import torch
import numpy as np

xy = np.loadtxt('diabetes.csv.gz', delimiter=',', dtype=np.float32)
x_data = torch.from_numpy(xy[:, :-1]) #将xy中除最后一列之外的所有列作为特征数据（x），并转换为PyTorch张量
                                      #xy[:, :-1]表示所有行，从第一列到倒数第二列
y_data = torch.from_numpy(xy[:, [-1]])  #xy[:, -1]表示提取所有行，最后一列标签数据（y）
                                        #xy[:, [-1]]提取最后一列并保持二维结构

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        #一个3层全连接神经网络（多层感知机）
        self.linear1 = torch.nn.Linear(8, 6)
        self.linear2 = torch.nn.Linear(6, 4)
        self.linear3 = torch.nn.Linear(4, 1)
        self.sigmoid = torch.nn.Sigmoid()
    def forward(self, x):
        #每层后使用 Sigmoid，将输出压缩到 [0, 1] 区间，表示患病概率
        x = self.sigmoid(self.linear1(x))
        x = self.sigmoid(self.linear2(x))
        x = self.sigmoid(self.linear3(x))
        return x

model = Model()
criterion = torch.nn.BCELoss(reduction='mean') #reduction='mean' 表示对 batch 内所有样本的损失取平均
optimizer = torch.optim.SGD(model.parameters(), lr=0.1) #通过 model.parameters() 获取所有可训练参数（权重和偏置）

for epoch in range(100):
    # Forward
    y_pred = model(x_data)
    loss = criterion(y_pred, y_data)
    print(epoch, loss.item())
    # Backward
    optimizer.zero_grad()
    loss.backward()
    # Update
    optimizer.step()