"""
一、bytes 转 list 变成数字的原理
bytes 底层本质是二进制字节序列，以 8 位（1 字节） 为一个存储单元，单个字节取值范围 0~255。
对 bytes 对象做遍历 / list() 转换时，会逐个取出每 8 位二进制，自动换算成十进制整数，存入列表。
本质：list(bytes) 就是把每个字节的原始数值，以十进制形式拆解出来。

二、print 打印 bytes 的显示规则
输出开头带 b'...'，是 Python 标识这是 bytes 字节类型，普通字符串 str 没有前缀 b。
打印 bytes 时遵循两套规则：
ASCII 可打印字符（英文、数字、空格、常规标点）：直接原样显示；
非 ASCII 字符（中文、日文、特殊符号）：用 \xHH 十六进制转义形式展示，每一个 \xHH 代表1 个字节。

三、bytes 类型本质
b'xxx' 是 Python bytes 字节类型的字面量写法。
和普通字符串 str 完全不同：
str：面向人类的文本字符；
bytes：面向底层的原始二进制字节数据，存储的是 0~255 的字节值。

四、bytes ([i]) 用法规则
bytes([i]) 作用：创建只有单个字节的 bytes 字节数组。
里面的参数 i 必须是 0～255 的整数，超出范围、字符、字符串都会直接报错。
可以把遍历 bytes 得到的十进制数字，还原回原始字节。

五、列表推导式语法糖
语法：[表达式 for 变量 in 可迭代对象] or [ 表达式 for ... ]，是 Python 标准语法糖。
等价逻辑：自动循环、执行表达式、自动把每一项装进新列表，省去手动建空列表 + append()。
示例等价：
python
运行
# 语法糖写法
[bytes([b]).decode("utf-8") for b in bytestring]

# 展开原生写法
res = []
for b in bytestring:
    item = bytes([b]).decode("utf-8")
    res.append(item)



"""