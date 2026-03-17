import numpy as np
import torch
from torch.utils.data import Dataset, DataLoader


class DiabetesDataset(Dataset):
    def __init__(self, filepath):
        xy = np.loadtxt(filepath, delimiter=',', dtype=np.float32)
        self.len = xy.shape[0]
        self.x_data = torch.from_numpy(xy[:, :-1])
        self.y_data = torch.from_numpy(xy[:, [-1]])

    def __getitem__(self, index):   #魔术方法 __getitem__ 方法：按索引获取单个样本
        return self.x_data[index], self.y_data[index]

    def __len__(self):  #__len__ 方法：定义数据集大小
        return self.len


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(8, 6)
        self.linear2 = torch.nn.Linear(6, 4)
        self.linear3 = torch.nn.Linear(4, 1)
        self.sigmoid = torch.nn.Sigmoid()

    def forward(self, x):
        x = self.sigmoid(self.linear1(x))
        x = self.sigmoid(self.linear2(x))
        x = self.sigmoid(self.linear3(x))
        return x


if __name__ == '__main__':
    # 创建数据集和数据加载器
    dataset = DiabetesDataset('diabetes.csv.gz')
    train_loader = DataLoader( #分批次加载数据
        dataset=dataset,
        batch_size=32,  #每批处理32个样本
        shuffle=True,  #打乱数据顺序
        num_workers=2  #控制并行数据加载的子进程数量
    )

    # 初始化模型
    model = Model()

    # 定义损失函数和优化器
    criterion = torch.nn.BCELoss(reduction='mean')
    optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

    # 训练循环
    for epoch in range(100):
        for i, data in enumerate(train_loader, 0): # 同时获取索引 i 和数据项 data
                                                   # 第 1 次  i=0  第 1 批数据 (样本 0~31) ……
                                                   # i 每 epoch 重置为 0，仅表示当前 epoch 内的批次序号
                                                   #epoch = 样本数/batch_size
            # 1. 准备数据
            inputs, labels = data
            # 2. 前向传播
            y_pred = model(inputs)
            loss = criterion(y_pred, labels)
            print(epoch, i, loss.item())
            # 3. 反向传播
            optimizer.zero_grad()
            loss.backward()
            # 4. 更新参数
            optimizer.step()
