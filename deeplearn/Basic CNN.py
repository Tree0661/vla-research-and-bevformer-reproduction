import torch
from torchvision import transforms
from torchvision import datasets
from torch.utils.data import DataLoader
import torch.nn.functional as F
import torch.optim as optim

# 设置超参数和数据预处理
batch_size = 64
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.1307,), (0.3081,))
])

# 加载数据集
train_dataset = datasets.MNIST(root='../dataset/mnist/',
                               train=True,
                               download=True,
                               transform=transform)
train_loader = DataLoader(train_dataset,
                          shuffle=True,
                          batch_size=batch_size)

test_dataset = datasets.MNIST(root='../dataset/mnist/',
                              train=False,
                              download=True,
                              transform=transform)
test_loader = DataLoader(test_dataset,
                         shuffle=False,
                         batch_size=batch_size)


# 定义神经网络模型
class Net(torch.nn.Module):
    def __init__(self):
        super().__init__()
        # 输出通道：指卷积层产生的特征图数量，也就是卷积核的数量
        self.conv1 = torch.nn.Conv2d(1, 10, kernel_size=5) # 输入通道1→输出10, 5x5卷积核
        self.conv2 = torch.nn.Conv2d(10, 20, kernel_size=5)# 10→20通道
        self.pooling = torch.nn.MaxPool2d(2) # 2x2最大池化 最大池化：保留最显著的特征（更适合视觉任务）
                                             # 平均池化：保留区域平均信息
        self.fc = torch.nn.Linear(320, 10) # 全连接层(320→10)

    def forward(self, x):
        batch_size = x.size(0)
        # 第一层卷积 [64,1,28,28] → [64,10,24,24] → [64,10,12,12]
        x = F.relu(self.pooling(self.conv1(x)))
        # 第二层卷积 [64,10,12,12] → [64,20,8,8] → [64,20,4,4]
        x = F.relu(self.pooling(self.conv2(x)))
        # 展平 [64,20,4,4] → [64, 320] (20*4*4=320)
        x = x.view(batch_size, -1)
        # 全连接输出 [64,320] → [64,10] (10个类别)
        x = self.fc(x)
        return x


# 创建模型实例并移动到设备
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
model = Net()
model.to(device)

# 定义损失函数和优化器
criterion = torch.nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.5)


# 训练函数
def train(epoch):
    running_loss = 0.0
    for batch_idx, data in enumerate(train_loader, 0):
        inputs, target = data
        inputs, target = inputs.to(device), target.to(device)

        optimizer.zero_grad()

        # 前向传播 + 反向传播 + 优化
        outputs = model(inputs)
        loss = criterion(outputs, target)
        loss.backward()
        optimizer.step()

        running_loss += loss.item()
        if batch_idx % 300 == 299:
            print('[%d, %5d] loss: %.3f' % (epoch + 1, batch_idx + 1, running_loss / 300))
            running_loss = 0.0


# 测试函数
def test():
    correct = 0
    total = 0
    with torch.no_grad():
        for data in test_loader:
            inputs, target = data
            inputs, target = inputs.to(device), target.to(device)
            outputs = model(inputs)
            _, predicted = torch.max(outputs.data, dim=1)
            total += target.size(0) #.size(0) 获取张量在第0维度（即批量维度）的大小
            correct += (predicted == target).sum().item()
    print('Accuracy on test set: %d %% [%d/%d]' % (100 * correct / total, correct, total))


# 训练和测试循环
if __name__ == '__main__':
    for epoch in range(10):
        train(epoch)
        test()

