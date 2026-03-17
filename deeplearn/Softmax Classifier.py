import torch
from torchvision import transforms  #torchvision.transforms：用于图像预处理
from torchvision import datasets #torchvision.datasets：提供常用数据集
from torch.utils.data import DataLoader  #DataLoader：高效加载数据集并生成批次
import torch.nn.functional as F
import torch.optim as optim

#定义批量大小和预处理流程
batch_size = 64
transform = transforms.Compose([
    transforms.ToTensor(),  # 将PIL图像转为Tensor（值域[0,1]）
    transforms.Normalize((0.1307,), (0.3081,))#将像素值从 [0, 1] 范围转换为均值接近 0、标准差接近 1 的分布
])
train_dataset = datasets.MNIST(root='../dataset/mnist/',
                               train=True, # train=True：加载训练集； False加载测试集
                               download=True,
                               transform=transform)
train_loader = DataLoader(train_dataset,
                          shuffle=True,
                          batch_size=batch_size)  # DataLoader：将数据集打包为可迭代对象
                                                  # 一个batch的形状为 [batch_size, 1, 28, 28] 通道数×高度×宽度
test_dataset = datasets.MNIST(root='../dataset/mnist/',
                              train=False,
                              download=True,
                              transform=transform)
test_loader = DataLoader(test_dataset,
                         shuffle=False,
                         batch_size=batch_size)


class Net(torch.nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.l1 = torch.nn.Linear(784, 512)
        self.l2 = torch.nn.Linear(512, 256)
        self.l3 = torch.nn.Linear(256, 128)
        self.l4 = torch.nn.Linear(128, 64)
        self.l5 = torch.nn.Linear(64, 10)

    def forward(self, x):
        x = x.view(-1, 784)  # 将输入张量重塑为二维（-1表示自动推断批量大小）
                             # PyTorch的Linear层（全连接层）只接受二维输入 要求输入格式：[batch_size, features]
                             # 28×28=784个特征
        x = F.relu(self.l1(x))
        x = F.relu(self.l2(x))
        x = F.relu(self.l3(x))
        x = F.relu(self.l4(x))
        return self.l5(x)


model = Net()
criterion = torch.nn.CrossEntropyLoss() #交叉熵损失 处理分类任务，内部包含Softmax和NLLLoss
optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.5) #动量因子（累积历史梯度，加速收敛并减少震荡）


def train(epoch):
    running_loss = 0.0
    for batch_idx, data in enumerate(train_loader, 0): #batch_idx 从0开始索引
        inputs, target = data
        optimizer.zero_grad()

        outputs = model(inputs)
        loss = criterion(outputs, target)
        loss.backward()
        optimizer.step()

        running_loss += loss.item()
        if batch_idx % 300 == 299: # 每300个batch打印一次
            print('[%d, %5d] loss: %.3f' % (epoch + 1, batch_idx + 1, running_loss / 300))
            running_loss = 0.0


#测试函数
def test():
    correct = 0 # 正确数
    total = 0
    # PyTorch 默认会跟踪所有张量操作以构建计算图
    with torch.no_grad(): #关闭自动梯度计算 仅关注预测结果的准确性
        for data in test_loader:
            images, labels = data # images：形状为 [batch_size, 1, 28, 28] 的张量
            outputs = model(images)

            #对于每个输入样本，找出模型认为最可能的预测结果
            """ outputs = tensor([
    [0.1, 0.05, 0.02, 0.01, 0.01, 0.01, 0.01, 0.79, 0.01, 0.01],  # 样本1
    [0.01, 0.85, 0.05, 0.02, 0.01, 0.01, 0.01, 0.01, 0.02, 0.02],  # 样本2
    [0.02, 0.01, 0.01, 0.01, 0.90, 0.01, 0.01, 0.01, 0.01, 0.01]   # 样本3
]) """
            _, predicted = torch.max(outputs, dim=1) # 返回指定维度上的最大值(0.79 0.85 0.90)及其索引(7 1 4)
                                                     # predicted 的结果是：tensor([7, 1, 4])
                                                     # _ 表示不关心这个变量

            total += labels.size(0) # 当前批次的样本数量
            correct += (predicted == labels).sum().item() #布尔张量 转换为 0/1 张量后求和 转换为 Python 数值
    print('Accuracy on test set: %d %%' % (100 * correct / total))


if __name__ == '__main__':
    for epoch in range(10):
        train(epoch)
        test()