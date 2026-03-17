import torch
import torch.nn as nn

# 定义一个包含4个单词，每个单词用3维向量表示的嵌入层
embedding_layer = nn.Embedding(4, 3)
# 此时 embedding_layer.weight 是一个可训练参数，形状为 (4, 3)
# 例如：tensor([[ 0.5, -0.2,  0.1],  # 索引0
#               [ 1.2,  0.3, -0.5],  # 索引1
#               [-0.8,  0.9,  0.0],  # 索引2
#               [ 0.0, -0.7,  1.1]]) # 索引3

# 输入：一批单词索引
input_ids = torch.LongTensor([0, 2, 3, 1])  # 想获取第0、2、3、1个词的向量
output = embedding_layer(input_ids)

print(output)