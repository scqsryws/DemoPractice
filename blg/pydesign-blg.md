# 程序设计的基本方法
- IPO模式
- input 输入 一个程序的开始
- process 处理 即算法
- output 输出 一个程序的展示运算结果的方式
- def定义函数
    - 函数是一组代码的集合，用于表达一个功能，函数名称是这段代码的名字
    - 未经调用无法执行，只有通过函数名调用才能执行

# turtle库与蟒蛇实例
- 三方库调用函数

# 数据类型
- 对数据的一种划分
- 共六种数据类型：数字、字符串、元组、列表、文件、字典
## 六种数据类型
- 数字类型Number
    - 整数int、浮点数float、复数complex
    - z.real()获得复数的实数部分、z.imag()获得复数的虚数部分
    - 不同数字类型可以混合运算，运算类型以最大为标准
    - int()、float()、complex() 数据类型转换
    - 运算 +、-、*、/、//、%，三方math库调用函数使用

- 字符串类型String
    - 字符串可以索引，索引输入片段为[0:n+1),字符串总长度为n
    - 转义符 \
    - r或R 反转义
    - +和*可以连接字符串
    - 字符串处理
        s.upper 字母大写
        s.lower 字母小写
        s.capitalize 首字母大写
        s.strip 去掉两边空格及去掉指定字符
        s.split 按指定字符分割字符串为数组
        s.isdigit 判断是否是数字类型
        s.find 搜索指定字符串
        s.replace 字符串替换
        for i in str 遍历

- 元组类型Tuple
    - 有序的、不可更改的，可使用索引
    - 元组可以使空的，可以使用括号也可以不适用，元素可以是不同类型
    - *和+来连接元组
    
- 列表类型
    l.append
    l.sort
    l.reverse
    l.index
    l.insert
    l.pop
    l.remove
    l.clear
    l.copy

- 文件类型
- 字典类型

#math库与random库
- random库
    - uniform 随机取小数
    - random 随机生成小数
    - seed 给随机数一个种子，默认种子是系统时钟
    - randint 生成一个随机的整数
    - randrange(a,b,c)随机生成一个从a开始到b以c递增的数
    - choice(list) 从列表中随机返回一元素
    - shuffle(list) 将列表中元素随机打乱
    - sample(list,k) 从指定列表随机获取k个元素
    
    math库