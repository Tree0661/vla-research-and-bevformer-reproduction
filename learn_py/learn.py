

"""
print("你好，世界")
print(888)
print("你好" ",世界")
print("1+1="+"2")    #字符串《=》加引号   加号用于字符串（变量）之间的拼接
print("1+1=",2)   #逗号相当于空格
print(1+1)   #结果是2
"""


"""
name = "梨花"
address = "河南省"
tel = 123456
tel_str = str(tel)
print("我是：" + name + "，我住在：" + address + "，我的电话是：" + tel_str)
"""


"""
num1 = 12
num2 = 2
num3 = 3.1213
me = "我在%s个人中排第%s名" % (num1,num2)
print(me)
print("我在%s个人中排第%s名" % (num1,num2))
print("我在%d个人中排第%d名" % (num1,num2))
print("我的工资为%.2f万元每月" % num3)
print("我的工资为%10.1f万元每月" % num3)
print(f"我的工资为{num3}万元每月")
"""


"""
print(type("你好"))
a = type(45)
print(a)
"""


"""
num1 = 67
num1_str = str(num1)
print(num1_str, type(num1), type(num1_str))
num2 = 7.98
num2_int = int(num2)
print(num2_int, type(num2), type(num2_int))
"""


"""
num1 = 2
num2 = 3
print(num1**num2)
print(num2//num1)
print(num2/num1)
print(num2%num1)
"""


"""
字符串的定义及转义字符
print("'你好世界'")
print('"你好世界"')
str1 = "\"你好世界\""
print(str1)
"""


"""
print("请输入你的名字：")
name = input()  input接受的数据类型为str（字符串）  可以通过 num = int(num) 转换 or num = int(input())
print(f"你的名字是: {name}")
print("你的名字是: %s" % name)
"""


"""
bool1 = False
bool2 = True
print(f"bool1 代表 {bool1},bool2 代表 {bool2}")
bool3 = 5>1
bool4 = 4<2
print(f"bool3 代表 {bool3},bool4 代表 {bool4},bool3的数据类型是{type(bool3)}")
num1 = 1
num2 = 2
  #第一个代码比较了 num1 == num2，然后将结果插入字符串
  #第二个代码先将 num1 插入字符串，然后将整个字符串与 num2 比较
  print("num1 = num2 的结果是%s" % (num1 == num2))
  print("num1 = num2 的结果是%s" % num1 == num2)
"""


"""
age = 19
if age >= 18:
    print("我已经成年了")
else:
    print("我没有成年")
print("时间过得真快")
"""


"""
age = int(input("请输入你的年纪："))
if age <18:
    print("未成年")
elif 18<=age<=65:
    print("已成年，人未老")
else:
    print("老年人")
"""


"""
if int(input("请输入你的身高：(cm)")) > 120:
    print("需要满足特定条件才能免费进入")

    if int(input("请输入你的vip等级：")) >3:
        print("可以免费进入")
    else:
        print("你需要买票")
else:
    print("可以免费进入")
"""


"""
i = 1
sum = 0
while i <=100:
    sum = sum + i
    i += 1
print(sum)
"""


"""
import random
num = random.randint(1,100)

flag = True
while flag:
    num_guess = int(input("请输入你猜测的数字："))
    if num_guess == num:
        print("你猜对了")
        flag = False
    elif num_guess > num:
        print("你猜的数字过大")
    else:
        print("你猜的数字过小")
"""


"""
print("Hello,",end='')   打印语句不换行
print("World!")
print("hello \tworld")   字符串的对齐
print("bye \tworld")
"""


"""
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f"{j}*{i}={i*j}\t",end='')
        j += 1
    i += 1
    print() #输出一个换行
"""


"""
name = "inherit"
for x in name:
    print(x,end='')
print()
count = 0
for x in name:
    print(x)
    count += 1
print(count)
"""


"""
for x in range(5):
    print(x)   # 0,1,2,3,4
for x in range(5,10):
    print(x,end='')    # 5,6,7,8,9
print()
for x in range(2,10,3):
    print(x)    # 2,5,8
"""


"""
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j}*{i}={i*j}\t",end='')
    print()
"""


"""
money = 10000
for i in range(1,21):
    import random
    num = random.randint(1, 10)

    if num < 5:
        print(f"员工{i}的绩效不足，本月不发工资")
        continue
    else:
        if money >=1000:
            money -= 1000
            print(f"员工{i}的绩效足够，本月发工资1000元")
        else:
            print("财务紧张，下月再发")
"""


"""
def say_hi():
    print("hi")
say_hi()
def add(a,b,c,d):
    result = a+b+c+d
    print(result)
add(1,2,3,4)
def mul(a,b,c,d):
    return a*b*c*d
print(f"{mul(1,2,3,4)}")
def add_mul(a,b,c,d):
    result = a+b+c+d + mul(a,b,c,d)
    print(result)
add_mul(1,2,3,4)
"""


"""
num = 100
def test1():
    print("test1:%d" % num)
def test2():
    global num  #在函数中修改全局变量的方法,加此行前后打印出的是：100 200 100 // 100 200 200
    num = 200
    print("test2:%d" % num)
test1()
test2()
print("%d" % num)
"""


"""
my_list = [[1,2,3],[4,5,6],[7,8,9]]     #列表
print(my_list)
print(type(my_list))
print(my_list[0])
print(my_list[0][0])   #1
print(my_list[-1][-1])  #9
"""


"""
# 列表的操作
my_list = ["in","it","is"]
index_is = my_list.index("is")
print("\"is\"在列表的索引值为%d" % index_is)
my_list[0] = "on"
print(f"修改后的列表为{my_list}")
my_list.insert(1,"uid")
print(f"插入后的列表为{my_list}")
my_list.append("over")   #追加单个
print(f"追（附）加后的列表为{my_list}")
my_list1 = ["if","hello"]
my_list.extend(my_list1)   #批量追加
print(f"批量追加后的列表为{my_list}")

my_list = ["in","it","is"]
del my_list[0]
print(f"删除后的列表为{my_list}")

my_list = ["in","it","is"]
element = my_list.pop(1)
print(f"通过pop方法删除后的列表为{my_list},删除的元素为{element}")

my_list = ["in","it","it","is"]
my_list.remove("it")  #删除元素在列表中的第一个匹配项
print(f"通过remove方法删除后的列表为{my_list}")
my_list.clear()
print(f"被清空后的列表为{my_list}")

my_list = ["in","it","it","is"]
num1 = my_list.count("it")
print(f"it在列表中出现了%d次" % num1)
num2 = len(my_list)
print("列表中元素数目为%d" % num2)
"""


"""
my_list = [1,2,3,4,5,6,7,8,9]
len_my_list = len(my_list)
index = 0
while index < len_my_list:
    print(my_list[index])
    index += 1
for i in range(len_my_list):
    print(my_list[i],end='')
"""


"""
t1 = (1,True,"hello")   #元组（只可读的列表） tuple
print(t1)
print(type(t1))
t2 = (True,)  #逗号不可省略
"""


"""
my_str = "hello world"  #字符串，不支持修改
element1 = my_str[2]
element2 = my_str[-1]
print(element1, element2)

my_str1 = my_str.replace("l","o")
print(f"修改后的新字符串为{my_str1}")
my_str_list = my_str.split(" ")
print(f"将字符串进行split分割（在每处空格分割）后得到列表{my_str_list}")

my_str = "  hello world "
new_str = my_str.strip()  #不传参数默认去除首尾空格
print(new_str)

my_str = "ll  hello world l"
new_str1 = my_str.strip("l")  #去前后指定字符串
print(new_str1)
"""


"""
#序列的切片
list1 = [0,1,2,3,4,5,6,7,8,9]
new_list1 = list1[0:5:2]   #起始，结束，步长 步长为负表示反向取
print(new_list1)
t1 = (0,1,2,3,4,5,6,7,8,9)
new_t1 = t1[0:5]
print(new_t1)
str1 = "hello world"
new_str1 = str1[::-1]   #翻转字符串
print(new_str1)
"""


"""
my_set1 = {1,1,1,2,2,3,4,4,5,6,7,}  #集合：无序，不可重复，可修改 <<=>> 1,2,3,4,5,6,7
my_set2 = set()
print(my_set1,type(my_set1),my_set2,type(my_set2))
my_set1.add(1)
my_set1.add(8)  #一次只能添加一个
print(my_set1)
my_set1.remove(8)
print(my_set1)
element = my_set1.pop()  #随机取出
print(element,my_set1)
my_set1.clear()
print(my_set1)

set1 = {1,2,3}
set2 = {1,3,5}
set3 = set1.difference(set2)  #集合1有而集合2中没有的
print(set3)
set1.difference_update(set2)
print(set1)   #消除集合1中有而集合2中没有的元素

set1 = {1,2,3}
set2 = {1,3,5}
set3 = set1.union(set2)
print(set3)  #合并两个集合
for x in set3:
    print(x)
"""


"""
my_dict = {"张三":90,"李四":98,"lily":94}
print(my_dict,type(my_dict))
#索引
score = my_dict["张三"]
print(f"张三的成绩是{score}")
my_dict = {
    "lily":{
        "chinese":90,
        "math":94,
        "english":93
    },
    "tom":{
        "chinese":98,
        "math":97,
        "english":94
    }
}
print(my_dict)
score = my_dict["lily"]["math"]
print(score)
"""


"""
my_dict = {"tom":90,"jack":98,"lily":94}
my_dict["jim"] = 89
print(my_dict)
my_dict["tom"] = 93
print(my_dict)
score = my_dict.pop("tom")
print(score,my_dict)
my_dict.clear()
print(my_dict)

my_dict = {"tom":90,"jack":98,"lily":94}
keys_my_dict = my_dict.keys()
print(keys_my_dict)
# 两种遍历方式
for x in keys_my_dict:
    print(x)
    print(my_dict[x])
for x in my_dict:
    print(x)
    print(my_dict[x])
num = len(my_dict)
print(num)
"""


"""
my_list = [2,1,3,5,4,]
my_tuple = (1,2,3,4,5)
my_str = "abcdefg"
my_set = {1,2,3,4,5}
my_dict = {"key1":1,"key2":2,"key3":3,"key4":4,"key5":5}
print(min(my_dict))
print(max(my_str))
print(list(my_str))
print(list(my_dict))
print(sorted(my_list)) #正向排序 五种都适用
print(sorted(my_dict,reverse=True)) #反向排序
"""


"""
def many_return():
    return 1,"hello",True
x,y,z = many_return()
print(x,y,z)
"""


"""
def message_print(mame,age,gender):
    print(mame,age,gender)
#位置传参
message_print("tom",11,"male")
#关键字传参
message_print("jim",gender = "male",age = 11)

def message_print(mame,age,gender = "male"): #默认值必须在最后
    print(mame,age,gender)
#默认传参
message_print("tom",11,"male")
message_print("tom",11,"female")
#不定长传参
def message_print(*args):   #元组形式传递
    print(args,type(args))
message_print("tom",11,"male")

def message_print(**kwargs):   #字典形式传递
    print(kwargs,type(kwargs))
message_print(name = "tom",age = 11,gender = "male")
"""


"""
#函数作为参数传递
def test(add):
    result = add(1,2)
    print(result)
def add(a,b):
    return a+b
test(add)

#匿名函数（只能用一次） lambda 传入参数: 函数体（一行代码）
def test(add):
    result = add(1,2)
    print(result)
test(lambda a,b:a*b)
"""


"""
f = open("D:\测试.txt","r",encoding="utf-8")


print(type(f))
print(type(f.read()))
print(f"read方法读取的全部内容是: {f.read()}")

my_list = f.readlines()   # 每一行当成列表的一个元素
print(type(my_list))
print(my_list)

my_list1 = f.readline()  #只读一行内容
print(type(my_list1))
print(my_list1)

for line in f:
    print(line)


f.close() #文件的关闭
"""


"""
count = 1
with open("D:\测试.txt","r",encoding="utf-8") as f:  #自动关闭文件
    for line in f:
            print(f"第{count}行的文字是{line}")
            count += 1
"""


"""
f = open("D:/test_py.txt","w",encoding="utf-8")  
# w方法会创建一个原本不存在的新文件，但是对已有的文件也会覆盖原来的文件内容
f.write("hello") #写入内存中
f.flush() #写入硬盘中
f.close() #内置了flush功能

f = open("D:/test_py.txt","a",encoding="utf-8")
# a方法会创建一个原本不存在的新文件，对已有的文件会将内容追加到末尾
f.write("\nhello")
f.close()
"""


"""
try:
    f = open("D:/test_py.txt","r",encoding="utf-8") #文件不存在
except:
    print("出现异常了")
    f = open("D:/test_py.txt", "w", encoding="utf-8")
# 语法错误在代码执行前就会被解释器捕获，因此实际上不会进入异常处理流程,语法错误发生在编译阶段，程序根本不会运行
"""


"""
# 捕获特定的异常
try:
    print(1/0)
except ZeroDivisionError as e:  #NameError 是固定词
    print("出现了0当除数的异常")
    print(e)
# 捕获所有的异常
try:
    print(1/0)
except Exception as e:
    print(e)
"""


"""
try:
    print("hello")        # 可能有异常
except Exception as e:
    print(e)              # 有异常捕获
else:
    print("没有异常")      # 没有异常则执行
"""


"""
try:
    f = open("D:/test_py.txt","r",encoding="utf-8")
except Exception as e:
    print("出现异常了")
    f = open("D:/test_py.txt", "w", encoding="utf-8")
else:
    print("没有异常")
finally:  # finally表示有没有异常都要执行
    print("finally 表示有没有异常都要执行")
    f.close()
"""


"""
import time  # import引入time模块使用sleep函数
print("hello")
time.sleep(5)
print("world")

from time import sleep
print("hello")
sleep(5)
print("world")

import time as t
print("hello")
t.sleep(5)
print("world")
"""


"""
import my_package.my_module1
import my_package.my_utils
my_package.my_module1.info_print1()  #包，模块，具体要调用的函数/变量
my_package.my_utils.print_file("D:/test_py.txt")
"""


"""
class Student:  #设计一个类（表格）
    name = None
    age = None
    gender = None
    Nationality = None
    native_place = None     #成员对象

stu1 = Student()   #创建对象   打印表格

#对象属性进行赋值     填写表格
stu1.name = "小小灰"
stu1.age = 4
stu1.gender = "male"
stu1.Nationality = "China"
stu1.native_place = "固始"

print(stu1.name)
"""


"""
class Student:
    name = None

    def say_hi(self):   #成员方法（函数）
        print(f"hi,{self.name}")

    def say_hello(self,my_str):
        print(f"hello,{self.name},{my_str}")
stu1 = Student()

stu1.name = "tom"
stu1.say_hi()
stu1.say_hello("jim")
"""


"""
class Student:
    def __init__(self,name,age,gender):  #构造方法
        self.name = name
        self.age = age
        self.gender = gender
stu1 = Student("tom",11,"male")  #该语句执行时自动执行 __init__ 函数
print(stu1.name)
print(stu1.age)
print(stu1.gender)
"""


"""
class phone:
    __voltage = 2.1  # 私有成员变量(无法被类对象使用，但是可以被类中的其他成员使用
    def __print_message(self):  # 私有成员方法
        print("hello 灰灰")
    def say(self):
        if self.__voltage < 5:
            print("ok")
            self.__print_message()
        else:
            print("no")
phone1 = phone()
phone1.say()
"""


"""
class Phone1:
    producer = "apple"
    __voltage = 2.1
    def say(self):
        if self.__voltage < 5:
            print("ok")
        else:
            print("no")
class Phone2:
    producer = "huawei"
    def read(self):
        print("NFC read card")
class Phone3:
    def write(self):
        print("NFC write card")
class MyPhone(Phone1, Phone2, Phone3):  #继承语法
    producer = "xiaomi"

phone = MyPhone()
phone.say()
phone.read()
phone.write()
print(phone.producer)  #父类成员对象名相同，优先调用前一个，在子类中复写，会显示子类的结果
"""


"""
class Phone:
    producer = "apple"
    def read(self):
        print("NFC read card")
class MyPhone(Phone):
    producer = "xiaomi"
    def read(self):
        print("123")
        #调用父类的成员对象和成员方法
        #方法1
        print(f"{Phone.producer}")
        Phone.read(self)
        #方法2
        print(f"{self.producer}")
        print(f"{super().producer}")
        super().read()
        print("456")
phone = MyPhone()
phone.read()
"""












