import torch

x_data = [1.0, 2.0, 3.0]
y_data = [2.0, 4.0, 6.0]

w = torch.Tensor([1.0])  #Tensor 是 PyTorch 中的数据结构
w.requires_grad = True # 变量.requires_grad  是否记录计算图，决定是否计算梯度
                       # 只有 requires_grad=True 的 Tensor 才会被纳入计算图，用于自动求导
def forward(x):
    return x * w
def loss(x, y):
    y_pred = forward(x)
    return (y_pred - y) ** 2

print("predict (before training)",  4, forward(4).item())  #.item()表示转化为Python float

for epoch in range(100):
    for x, y in zip(x_data, y_data):
         l = loss(x, y)
         l.backward() # 自动计算计算图中所有需要梯度的张量的梯度
         print('\tgrad:', x, y, w.grad.item())  #.grad指的是梯度
         w.data = w.data - 0.01 * w.grad.data  # w.data指的是只包含数据的w，不包含计算图信息
                                               # w本身既包含计算图信息，也包含数据
         w.grad.data.zero_()  #梯度清零

    print("progress:", epoch, l.item())

print("predict (after training)", 4, forward(4).item())