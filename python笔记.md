## Python标识符
- _foo 单下划线开头
    - 不能直接访问的属性，需通过类提供的接口访问
    - 不能用 from xxx import * 而导入
- __foo 双下划线开头
    - 代表类的私有成员
- ’__foo__‘ 双下环线开头和结尾
    - 代表python里特殊方法专用标识符，如__init__()代表类的构造函数
- ;分号同一行显示多条语句 print 'hello';print 'runoob';
- 30个保留字，都是小写字母开头
- 缩进必须一致，议你在每个缩进层次使用 单个制表符 或 两个空格 或 四个空格，不能混用
- 多行语句用\斜杠分行
    ```python
    total = item_one + \
        item_two + \
        item_three
    ```
- 语句中包含 [], {} 或 () 括号就不需要使用多行连接符
- 可以使用引号( ' )、双引号( " )、三引号( ''' 或 """ ) 来表示字符串，三引号特定位置可以理解为注释
- 单行注释用 # 开头，可以放在表达式行末
- 多行注释 ''' adasd''' 或者 """sdasda"""
- 同一行显示多条语句用;分号分隔
    ```python
    import sys; x = 'runoob'; sys.stdout.write(x + '\n')
    ```
- 多个语句构成代码组if、while、def和class这样的复合语句，首行以关键字开始，以冒号( : )结束，该行之后的一行或多行代码构成代码组。
- python命令执行关键词，python3 xxx.py，3是版本，如果设置了环境变量可以不带3
- pip/pip3下载依赖包专用，pip3 install xxx/ pip3 uninstall xxx 下载和卸载依赖包

## 变量赋值

- 赋值整型变量 counter = 100
- 浮点型 miles = 1000.0
- 字符串 name = "John"
- 多个变量赋值逗号分隔，等号左右对称 a, b, c = 1, 2, "john"
- 标准数据类型
    - Numbers（数字）四种类型
        - int（有符号整型）
        - long（长整型[也可以代表八进制和十六进制]）
        - float（浮点型）
        - complex（复数）
    - String（字符串）
    - List（列表），有序的对象集合
    - Tuple（元组）
    - Dictionary（字典），无序的对象集合
- 字符串切片 str
    ```python
    # 切片 [)，前开后闭区间，即包括前，不包括后
    d = '1234567'
    print(d[2]) # 下标为2的值 3
    print(d[0:2]) # 下标从0开始到下标为2结束, 12
    print(d[:2])  # 下标从0开始到下标为2结束，省略了0, 12
    print(d[-2:]) # 下标倒数第2个开始到结束, 67
    print(d[1:2]) # 下标从1开始到第二位结束, 2
    print(d[:5:2]) # 下标从0开始前五个，每隔2个取一个 135
    print(d[::2]) # 下标从0开始所有的，每隔2个取一个 1357
    print(d[:]) # 复制一份'1234567'
    ```
- 列表切片 list
    ```python
    # 切片 [)，前开后闭区间，即包括前，不包括后
    d = [1,2,3,4,5,6,7]
    print(d[2]) # 下标为2的值 3
    print(d[0:2]) # 下标从0开始到下标为2结束, 12
    print(d[:2])  # 下标从0开始到下标为2结束，省略了0, 12
    print(d[-2:]) # 下标倒数第2个开始到结束, 67
    print(d[1:2]) # 下标从1开始到第二位结束, 2
    print(d[:5:2]) # 下标从0开始前五个，每隔2个取一个 135
    print(d[::2]) # 下标从0开始所有的，每隔2个取一个 1357
    print(d[:]) # 复制一份 [1,2,3,4,5,6,7]
    ```
- 元组切片 tuple
    ```python
    # 切片 [)，前开后闭区间，即包括前，不包括后
    d = (1,2,3,4,5,6,7)
    print(d[2]) # 下标为2的值 3
    print(d[0:2]) # 下标从0开始到下标为2结束, 12
    print(d[:2])  # 下标从0开始到下标为2结束，省略了0, 12
    print(d[-2:]) # 下标倒数第2个开始到结束, 67
    print(d[1:2]) # 下标从1开始到第二位结束, 2
    print(d[:5:2]) # 下标从0开始前五个，每隔2个取一个 135
    print(d[::2]) # 下标从0开始所有的，每隔2个取一个 1357
    print(d[:]) # 复制一份(1,2,3,4,5,6,7)
    ```
- 字典，字典当中的元素是通过键来存取的，而不是通过偏移存取
    ```python
    # 其实是一个和json一直的数据结构
    tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
    ```
    - 设置key, tinydict['jon'] = '程序猿'
    - 获取单个值的方式 
        - 中括号，tinydict['dept']，注意要引号['dept']
        - get方法 tinydict.get('dept')
    - 获取所有key的方法
        ```python
        tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}
        print(tinydict.keys())
        # 输出 dict_keys(['name', 'code', 'dept'])
        ```
    - 获取所有value的方法
        ```python
        tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}
        print(tinydict.values())
        # 输出 dict_values(['john', 6734, 'sales'])
        ```
- set 和 dict 类似，不存储value，存储不重复值的数据
    ```python
    s = set([1,1, 2, 3])
    # 会自动去重 输出 {1, 2, 3}
    ```
    - 添加元素 s.add(4)
    - 删除元素 s.remove(4)

### 内置方法
- int(x [,base]) 将x转换为一个整数
- long(x [,base] ) 将x转换为一个长整数
- float(x) 将x转换到一个浮点数
- complex(real [,imag]) 创建一个复数
- str(x) 将对象 x 转换为字符串
- repr(x) 将对象 x 转换为表达式字符串
- eval(str) 用来计算在字符串中的有效Python表达式,并返回一个对象
- tuple(s) 将序列 s 转换为一个元组
- list(s) 将序列 s 转换为一个列表
- set(s) 转换为可变集合
- dict(d) 创建一个字典。d 必须是一个序列 (key,value)元组。
- frozenset(s) 转换为不可变集合
- chr(x) 将一个整数转换为一个字符
- unichr(x) 将一个整数转换为Unicode字符
- ord(x) 将一个字符转换为它的整数值
- hex(x) 将一个整数转换为一个十六进制字符串
- oct(x) 将一个整数转换为一个八进制字符串
 ## 算数运算符 
- 加减乘除取余幂
- // 取整除返回商的整数部分（向下取整） 9//2 = 4
## 比较运算符
- == (!= <>两个类似都是不等于) > < >= <= 
## 赋值运算符
- = += -= *= /= %= **= //=
## 逻辑运算符
- x and y
- x or y
- not x
## 成员运算符
- a in list，a在list中
- b not in list b不在list中
## 身份运算符
- id() 函数用于获取对象的内存地址
- x is y 类似id(x) == id(y) 判断两个标识符是否引用自同一个对象
- x is not y, 类似 id(a) != id(y) 引用的不是同一个对象
- `is 用于判断两个变量引用对象是否为同一个(同一块内存空间)， == 用于判断引用变量的值是否相等。`

## 运算符优先级 参考文档

## 条件语句
```python
if 判断条件1:
    执行语句1……
elif 判断条件2:
    执行语句2……
elif 判断条件3:
    执行语句3……
else:
    执行语句4……
```

## 循环语句：while循环、for循环、嵌套循环
- 循环控制 break、continue、pass

for
```python
sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)
```

while/break
```python
n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')
```

while/continue
```python
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)
```

## 数学包

浮点数的数学运算函数
```python
import math
print(dir(math))

'''
['__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'pi', 'pow', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']'''
```
```python
import cmath
print(dir(cmath))

'''
['__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atanh', 'cos', 'cosh', 'e', 'exp', 'inf', 'infj', 'isclose', 'isfinite', 'isinf', 'isnan', 'log', 'log10', 'nan', 'nanj', 'phase', 'pi', 'polar', 'rect', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau']
'''
```

## python 常量
- pi 圆周率
- e 自然常数

## 字符串方法
- 参考文档：https://www.runoob.com/python/python-strings.html

## 列表方法
- 参考文档：https://www.runoob.com/python/python-lists.html

## 元组方法
- 参考文档：https://www.runoob.com/python/python-tuples.html

## 字典方法
- 参考文档：https://www.runoob.com/python/python-dictionary.html

## 时间模块
- 参考文档：https://www.runoob.com/python/python-dictionary.html

## 函数
- def定义
- 拉姆达函数
- 高阶函数
- 参数设置，注意不定长度参数 *args

