
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

# 函数的定义
- 函数：完成特定功能的一个语句组，通过调用函数名来完成与功能
- 函数可以反馈结果
- 为函数提供不同的参数，可以实现对不同数据的处理
- 使用函数的目的
    - 降低变成的难度
    - 代码重用
    - 函数定义：使用def语句
        def<name>(<parameters>):
            <body>
        name 有效的python标识符
        parameters 参数列表
        形参 定义函数时，括号中的变量，只在函数内部有效
        实参 调用函数时，括号中的变量
        调用参数都必须初始化
        body 函数体
        return （可以返回变量，也可以返回表达式）
            - 结束函数调用，并将结果返回给调用者，该语句可选，可任意出现
            - 返回的值传递给调用程序
            - 两种形式：返回一个值；返回多个值
            - 无返回即等于 return None
            

# 函数和程序结构
- 函数可以简化程序，使程序模块化
- 用函数将复杂的程序分割成小的程序段


-内容 面向编程逻辑，第三方库的使用
-本质 理解问题的求解
-解决 各类问题

# Python特点
# 大牛Guido创立
- 是通用语言
- 是脚本语言
- 是开源语言
- 是跨平台语言
- 是多模型语言
- 用于普世的问题解决的开发，通用性
- 优势：强制可读性；较少的底层语法元素；多变成方式；支持中文字符；三方库庞大，生态高产，跨操作系统平台

更注重集成开发能力，计算机生态强大，三方库开源，Python牛逼！

# Python计算生态 = 标准库 + 第三方库
- 标准库：随解释器直接安装到操作系统中的功能模块
- 第三方库：需经过安装才能使用的功能模块
- 库、包、模块，统称“模块”

## turtle库
- 原理：有一只海龟在窗体中心，在画布上游走

## turtle库的使用
- setup(width, height, startx, starty) 不是必须的函数，4个参数后两个是可选项

# unicode 编码
- 从0 到 1114111空间，每个编码对应一个字符
- chr(x) 把Unicode编码转化成字符
- ord(x) 把字符串的内容转化为Unicode编码

# 字符串处理方法
- “方法”特指<a>.<b>()风格中的函数<b>()
- 方法本身也是函数，但与<a>有关，<a>.<b>()风格使用

# 字符串处理方法
- s.lower()或s.upper()将字符串字符全部小写或大写
- s.split("分割符")返回一个列表，由str根据sep被分割的部分组成
- s.count()返回字符串中某个元素出现的字数
- s.replace(old,new) 对字符串中的old内容替换成new
- s.center(width,"填充字符") width宽度
- s.strip(chars) 去掉s中左右侧列出的字符
- "分隔符".join(s) 在s的字符串美个元素后增加一个分隔符，主要用于格式化分割字符串
- format()方法的格式控制
    :引导
    <填充> 用于填充单个字符
    <对齐> <左对齐   >右对齐   ^居中对齐
    <宽度> 槽设定的输出宽度
    <,><.精度><类型> 
        ，是指数字的千位分隔符
        精度是浮点数小数精度 或者 字符串最大输出长度
        整数类型：b,c,d,o,x,X
        浮点数类型：e,E,f,%


# time库的使用
- time库处理时间的标准库
- 表达计算机时间
- 提供获取系统时间并格式化输出功能
- 提供系统级精准计时功能，用于程序性能分析

## time三类函数
- 时间获取：time() ctime() gmtime()
- 时间格式化：strftime() strptime()
- 程序计时：sleep() perf_counter()

### 时间获取
- time.time()
获取当前时间的时间戳，从1970年1月1日 00：00：00秒开始计时，浮点数
- time.ctime()
程序员易读时间获取最简单的方式，str
- time.gmtime()
获取易于程序处理的时间格式

### 时间格式化
- time.strftime(tpl,ts) tpl是格式化模板字符串，用来定义输出效果，ts是计算机内部时间类型变量gmtime()获取
 %Y 年份 0000-9999
 %m 月份 01-12
 %B 月份名称 英文名称
 %b 月份名称缩写 英文缩写
 %A 星期名称
 %a 星期缩写
 %H 24小时制 00-23
 %I 12小时制 00-12
 %p 上下午 AM,PM
 %M 分钟 00-59
 %S 秒 00-59
 
- time.strptime(str,tpl) str是字符串形式的时间值，tp是格式化模板字符串，时间字符串转化为系统时间格式（gmtime(）格式相同）


### 程序计时
- sleep() 产生时间，括号中时间是以秒级计算
- perf_counter() 测量时间，cpu级的时间，由于计数起点并不确定，所以要连续调用计算差值


# python 小结
- 第一周 python的基本语法元素
    - 缩进、注释、命名、变量、保留字
    - 数据类型、字符串、整数、浮点数、列表
    - 赋值语句，分支语句、函数
    - input()、print()、eval()、print()格式化
- 第二周 python基本图形绘制
    - 从计算机技术演进角度看待python语言
    - 海龟绘图体系及import保留字用法
    - penup() pendown() pensize() pencolor()
    - fd() circle() seth()
    - 循环语句 for in range
- 第三周 基本数据类型
    - 数据类型：整数、浮点数、复数
    - 数据类型运算操作符、运算函数
    - 字符串类型：表示、索引、切片
    - 字符串操作符、处理函数、处理方法、.format()格式化
    - time库：time() gmtime() ctime()  strftime() strptime() sleep() perf_counter()
    
    
# 第四周 程序的控制结构
- 顺序结构
- 分支结构
- 循环结构

## 程序的分支结构
- 单分支结构
    if 条件：
        执行语句

- 二分支结构
    if 条件：
        执行语句
    else：
        执行语句

- 多分支结构  //注意多分支条件之间的覆盖；程序可运行，但不正确，要注意多分支；分支结构是程序的重要框架，读程序先看分支
    if 条件：
        执行语句
    elif 条件：
        执行语句
    ....
    else：
        执行语句
        
- 条件判断
    !=
    ==
    <=
    >=
    <
    >

- 条件组合保留字
    and
    or
    not
    
- 异常处理 //try 和 except，使用后可以让程序不报错，但是逻辑还是可能错误
    try:
        语句1
    except <异常名称>：  //若填写异常类型名称，仅在该错误下执行语句2
        语句2
    else:  //对应语句3在不发生异常时执行
        语句3 
    finally：   //语句4一定会执行
        语句4

## 程序的循环结构
- 遍历循环 for
    for _ in 遍历结构：
        语句
    由保留字for in组成，完整遍历所有元素后结束
    每次循环，所获得元素放入循环变量，并执行一定语句
    - 应用
        计数循环（N次）
        for i in range（N）：
            语句块
        for i in range(M,N,K):  //从M到N，以K为步长（间隔）
            语句块
        字符串遍历循环
        for c in s：
            语句块
        列表遍历循环
        for item in ls:
            语句块
        文件遍历循环
        for line in fi：
            语句块
        - fi是一个文件标识符，遍历每行，产生循环
        

- 无限循环 while
    由条件控制的循环运行方式：
        while 条件：
            语句块
        - 反复执行语句块，直到条件不符合，结束循环
    
- 循环控制保留字
    break   跳出并结束当前整个循环， 执行循环后的语句
    continue 结束当次循环，继续执行后续次数循环
    break和continue都可以和for、while结合使用

- 循环的高级用法
    for 循环 in 遍历结构：
        语句块
    else：
        语句块
    
    while 条件：
        语句块
    else：
        语句块
        
    - 如果当循环没有被break语句退出，执行else语句
    - else语句块作为“正常”完成循环的奖励
    - 这里else的作用与异常处理中的else相似
    

## random库使用
- 使用随机数的python标准库
- 伪随机数：才用梅森旋转算法生成伪随机序列中元素
- random库用于生成随机数

- 两类函数，常用8个
    - 基本 seed()，random()
        random.seed() 根据 随机数种子 使用 梅森旋转算法 产生 随机序列，默认的种子数使用当前系统时间
        random.random() 生成从0开始到1之间的随机小数
    - 扩展 randint(),randrange(),
        random.randint(a,b) 生成一个[a, b]之间的随机整数
        random.randrange(m,n,k) 生成一个[m, n)以k为步长的随机整数
        random.getrandbits(k) 生成一个k比特长的随机整数
        random.uniform(a, b) 生成一个[a,b]之间的随机小数
        random.choice(seq) 从序列seq中随机选择一个元素
        random.shuffle(seq) 将序列seq中元素随机排列，返回打乱后的序列
        
- 需掌握的能力
    - 能够利用随机数种子产生“确定”伪随机数
    - 能够产生随机整数
    - 能够对序列类型进行随机操作
    
## 圆周率计算
- 蒙特卡洛法
- 代码如果太长，可以加一个反斜杠然后换行输入

## 思维
- 计算思维是一个抽象的过程，用计算机自动化求解
- 数学思维是找到公式，利用公式求解


# 第五周 函数和代码复用
- 函数的理解和定义
    函数是一段代码的表示
        def 函数名(必选参数，可选参数)：
            函数体
            return 返回值
    - 函数定义时，所指定的参数是一种占位符
    - 函数定义后，如果不经过调用，不会被执行
    - 函数定义时，参数是输入，函数体是处理，结果是输出（IPO）
    - 可选参数传递
    - 可变参数传递
        def 函数名(参数，*arg, **kwarg):
            函数体
            return 0个或多个返回值 //返回元祖类型

## 局部变量和全局变量
- 局部变量和全局变量是不同变量
- 局部变量是函数内部的占位符，与全局变量可能重名，但不同
- 函数运算结束后，局部变量被释放
- 可以使用global保留字在函数内使用全局变量

## lambda函数(谨慎使用)
- 返回函数名作为结果
- lambda函数是一种匿名函数，即没有名字的函数
- 使用lambda保留字定义，函数名是返回结果
- 用于定义简单的，能够在一行内表示的函数
    函数名 = lambda 参数 ： 表达式
    等价于 def return的函数
    f = lambda x, y : x + y
    f(10, 15)

## pyinstaller库
- 打包py文件作为exe可运行文件
- 操作指令：
    -h 帮助
    --clean 清除临时文件
    -D,--onedir 默认值，生成dist文件夹
    -F，--onefile 在dist文件夹中只生成独立的打包
    -i<图标名.icon>指定图片成为打包文件的图标icon
    
    
# 第六周 组合数据类型
序列、字典
集合、整数、浮点数、字符串、元组，都是不可变的数据类型

## 集合类型及操作
1.集合类型的定义
    集合是多个元素的无序组合
    - 集合类型与数学中的集合概念一致
    - 集合元素之间无序，每个元素唯一，不存在相同元素
    - 集合元素不可更改，不能是可变数据类型
    - 集合用大括号｛｝表示，元素间用逗号分隔
    - 建立集合类型用｛｝或set（）
    - 建立空集合，必须使用set（）

2.集合操作符
S|T 并   包含ST中所有的元素
S&T 交   包含同时在ST中的元素
S-T 差   包含S的元素但不在T的元素
S^T 补   包含S中和T不相同的元素
S <= T 或者S < T 判断S和T的子集关系
S >= T 或者S > T 判断S和T的包含关系
4个增强操作符
S |= T  更新S，包括在集合S和T中的所有元素
S -= T  更新S，包含在集合S但不在T重中的所有元素
S &= T  更新S，包含同时在S和T中的元素
S ^= T  更新S，包含集合S和T中的非相同元素

3.集合处理方法
S.add(x) 如果x不在集合S中，将x增加到S中
S.discard(x) 移除S中的元素x，如果x不在集合S中，不报错
S.remove(x) 移除S中的元素x，如果x不在集合S中，产生KeyErroor异常
S.clear() 移除S中所有元素
S.pop() 随机返回S的一个元素，更新S，若S为空产生KeyError异常
S.copy() 返回集合S的一个副本
len(S) 返回集合S的元素个数
x in S 判断S中元素x，x在集合S中，返回True，否则返回False
x not in S 判断S中元素x，x不在集合S中，返回True，否则返回False
set(x) 将其他类型变量x转变为集合类型

4.集合类型应用场景
    - 包含关系的比较
        "p" in {"p", "y", 123}
        返回布尔值
    - 数据去重
        集合类型所有元素无重复
    
5.集合小结
- 集合使用{}和set()函数创建
- 集合间操作：交（&），差（-），并（|），补（^）、比较（< = >）
- 集合类型方法：.add(),.discard()不会报错,.pop()
- 集合的应用：包含关系的比较，数据去重

## 序列类型及操作
1.序列的定义
序列是具有先后关系的一组元素
- 序列是一维元素的向量，元素类型可以不同
- 类似数学元素序列
- 元素间由序号引导，通过下标访问序列的特定元素

序列是一个基类类型，三种衍生扩展类型
    ①.字符串类型
    ②.元组类型
    ③.列表类型

2.序列处理函数及方法
6个操作符
- 序列类型通用操作符
x in s
x not in s
s + t   两个序列连接
s * n 或 n * s   数次表示
s[i]    索引
s[i:j]或s[i:j:k]     切片

- 序列类型通用函数和方法
5个函数和方法
len(s)  返回序列s的长度
min(s)  s中最小的元素，s的元素需要可以比较
max(s)  s中最大的元素，s的元素需要可以比较
s.index(x)或者s.index(x,i,j)  返回序列s从i开始到j位置中第一次出现元素x的位置
s.count(x)  返回序列s中出现x的总次数


## 元组类型定义
元组是序列类型的一种扩展
- 元组是一种序列类型，一旦创建不能修改
- 使用小括号()或tuple()创建，元素间用逗号，分隔
- 可以使用或不使用小括号

元组继承序列类型的全部通用操作
- 元组继承了序列类型的全部通用操作
- 元组因为创建后不能修改，因此没有特殊操作
- 使用或不适用小括号

## 列表类型定义
1.列表的定义
列表是序列类型的一种扩展，十分常用
- 列表是一种序列类型，创建后可以随意被修改
- 使用[]或list()创建，元素间用逗号，分隔
- 列表中各元素类型可以不同，也没有长度限制
仅仅通过 = 将一个列表变量赋值给另一个列表变量，那么两个列表变量指向同一个列表

3.列表类型的操作函数和方法
ls[i] = x 替换ls中第i个元素为x
ls[i:j:k] = lt 用列表lt中元素代替ls里的切片元素
del ls[i] 删除列表第i个元素
del ls[i:j:k] 删除切片ls的子列表
ls += lt 更新列表，将列表lt的元素增加到ls里
ls *= n 更新列表，元素重复n次
ls.appand(x)
ls.clear() 清空列表元素
ls.copy() 新建一个列表并将元素复制
ls.insert(i,x) 在第i个元素替换为x
ls.pop(i) 删除i元素，默认从最后一位开始删除
ls.remove(x) 删除ls中出现的第一个元素x
ls.reverse() 倒序列表

## 序列类型应用场景
- 元组用于元素不改变的应用场景，更多用于固定搭配场景
- 列表更加灵活，它是最常用的序列类型
- 最主要作用：表示一组有序数据，进而对他们进行操作
    ★元素遍历
    ★数据保护
        如果不希望数据被程序所改变，转换成元组类型

序列类型、列表类型，重点



## 字典类型及操作
1.字典类型定义
理解“映射”
- 映射是一种键（索引）和值（数据）的对应
字典类型是“映射”的体现
- 键值对：键是数据索引的扩展
- 字典是键值对的集合，键值对之间无序
- 采用大括号{}和dict()创建，键值对用冒号：表示

2.字典类型操作函数和方法
del d[k]    删除字典d中键k对应的数据值
k in d      判断键k是否在字典d中，如果在返回True，否则返回False
d.keys()    返回字典d中所有的键信息
d.values()  返回字典d中所有的值信息
d.items()   返回字典d中所有的键值对信息
d.get(k,<default>)  键k存在，则返回相应值，不在则返回<default>值
d.pop(k,<default>)  键k存在，则取出相应值,且删除该键值对，不在则返回<default>值
d.popitem()     随机从字典d中取出一个键值对，以元组形式返回
d.clear()   删除所有的键值对
len(d)      返回d中元素的个数

3.字典类型应用场景
映射的表达
- 映射无处不在，键值对无处不在
- 例如：统计数据出现次数，数据是键，次数是值
- 最主要作用：表达键值对数据，进而操作它们

元素遍历
for i in d：
    <语句块>

## jieba库
1.jieba是优秀的中文分词第三方库
- 中文文本需要通过分词获得单个的词语
- jieba是优秀的中文分词第三方库
- jieba库提供三种分词模式，最简单只需要掌握一个函数

2.jieba库的使用
jieba分词依靠中文词库
- 利用一个中文词库，确定汉字之间的关联概率
- 汉字间概率大的组成词组，形成分词结果
- 除了分词，用户还可以添加自定义的词组

3.jieba分词的三种模式
精确模式、全模式、搜索引擎模式
- 精确模式：把文本精确的切分开，不存在冗余单词
- 全模式：把文本中所有可能的词语都扫描出来，有冗余
- 搜索引擎模式：在精确模式基础上，对长词语再次切分

4.jieba库常用函数
jieba.lcut(s)   精确模式，返回一个列表类型的分词结果
jieba.lcut(s,cut_all= True) 全模式，返回一个列表类型的分词结果，存在冗余
jieba.lcut_for_search(s)    搜索引擎模式，返回一个列表类型的分词，存在冗余
jieba.add_word(w)   向分词词典增加新词w




# 第七周 文件和数据格式化
- 文件的理解 //文件是数据的抽象和集合
    - 文件是存储在存储器上的数据序列
    - 文件是数据存储的一种形态
    - 文件展现形态：文本文件和二进制文件
    
## 文件的理解
- 文本文件和二进制文件只是文件的展示方式
- 本质上，所有文件都是二进制形式存储
- 形式上，所有文件才用两种方式展示
    
## 文件的使用
文件是数据的抽象和集合
1.文本文件vs二进制文件
    文本文件：
        - 由单一特定编码组成的文件，如UTF-8编码
        - 由于存在编码，也被看成是存储着的长字符串
        - 适用于例如：.txt文件、.py文件
    二进制文件：
        - 直接由比特0和1组成，没有同一字符编码
        - 一般存在二进制0和1的组织结构，即文件格式
        - .png文件、.avi文件
        
2.所有文件都可以以二进制形式打开
"中国是个伟大的国家！"
- 文本形式  中国是个伟大的国家
- 二进制形式 b'\xd6\xd0\xfa\xca\xc7\xb8\xf6\xb0\xb4\xf3\xb5\xc4\xb9\xfa\xbc\xd2\xa3\xa1'

## 文件的执行
tf = open('文件名','rt’) 文本方式打开
print(tf.readline())
tf.close()

tf = open('文件名','rb’) 二进制方式打开
print(tf.readline())
tf.close()

 变量名 = open(‘文件名’，‘打开模式’)
文件句柄    文件路径，若同源可省路径     打开模式 - 文件、二进制、读、写
文件路径  
    此时的绝对路径为 D:\PYE\f.txt
    表达可以使用四种方式：
        1."D:/PYE/f.txt" 绝对路径表达方式1
        2."D:\\PYT\\f.txt" 绝对路径表达方式2
        3."./PYT/f.txt" 相对路径 此时路径同源目录
        4."f.txt" 相对路径 此时路径同文件夹

打开模式
    r -- 只读模式，默认值，如果文件不存在，返回FileNotFoundError
    w -- 覆盖写模式，文件不存在则创建，存在则完全覆盖
    x -- 创建写模式，文件不存在则创建，存在则返回FileExistsError
    a -- 追加写模式，文件不存在则创建，存在则在文件最后追加内容
    b -- 二进制文件模式
    t -- 文本文件模式，默认值
    + -- 与r、w、x、a一同使用，在原功能基础上使文件具备同时读写能力

f = open("file")  - 文本形式，只读模式，默认值
f = open("file","rt")  - 文本形式，只读模式，同默认值
f = open("file","w")  - 文本形式，覆盖写模式
f = open("file","a+")  - 文本形式，追加写模式+读文件
f = open("file","x")  - 文本形式，创建写模式
f = open("file","b")  - 二进制形式，只读模式
f = open("file","wb")  - 二进制形式，覆盖写模式

文件关闭
    变量名.close()
    文件句柄

程序运行时，如果只将文件打开，而不关闭，则在运行过程中，文件一直是打开的
而在程序正常退出时，python解释器会自动将文件关闭


## 文件内容读取
<f>.read(size = -1) 读入全部内容，如果给出参数，读入前size长度的字符信息
<f>.readline(size = -1) 读入一行内容，如果给出参数，读入前size长度字符信息
<f>.readlines(hint = -1) 读入文件所有行，以每行为元素行程列表，如果给出参数，读入前hint行

## 文件的全文本操作
遍历全文本：
    - 方法一
        tf = open("t.txt","rt")
        txt = tf.read()
        tf.close()
        print(txt)
    - 方法二
        tf = open("t.txt","rt")
        txt = tf.read(2)
        while txt !="":
            txt = txt.read(2)
        tf.close()
逐行遍历文件：
    - 方法一：//一次读入，分行处理
        tf = open("t.txt","rt")
        for i in tf.readlines():
            print(i)
        tf.close()
    - 方法二：//分行读入，逐行处理
        tf = open("t.txt","r")
        for line in tf:
            print(line)
        tf.close()

## 数据的文件写入
<f>.write(s)  向文件写入一个字符串或字节流
<f>.writelines(lines)  将一个元素全为字符串的列表写入文件
<f>.seek(offset)  改变当前文件操作指针的位置 0 - 文件开头 ； 1 - 当前位置 ； 2 - 文件结尾

## 文件使用小结
- 文件的使用方法：打开-操作-关闭
- 文本文件&二进制文件：open()和close()
- 文件的读取：read(),readline(),readlines()
- 文件的写入：write(),writelines(),seek()

## 自动轨迹绘制
- 需求：根据脚本来绘制图形
- 不是写代码而是写数据绘制轨迹
- 数据脚本是自动化的第一步

- 基本思路
    - 定义数据文件格式（接口）
    - 编写程序，根据文件接口解析参数绘制图形
    - 编制数据文件
    
## 一维、二维数据处理
// 一维数据
由对等关系的有序或无需数据构成，采用线性方式组合

// 二维数据
由多个一位数据构成，是一维数据的组合形式

// 多维数据
由一维数据或二维数据在新维度上的扩展

// 高维数据
仅利用最基本的二元关系展示数据间的复杂结构
dict 键值对
｛
    'first': 'Tian',
    'last':'xiao,'
    'address':{
        'nihao':'shiba",
        'wpei':'nia'
    }
｝

// 数据的操作周期
存储 <-> 表示 <-> 操作
数据存储（存储格式）   数据表示（数据类型）  数据操作（操作方式）

### 一维数据
1.一维数据的表示
    - 如果数据间有序：使用列表类型
        - 列表类型可以表达一维有序数据
        - for循环可以遍历数据，进而对每个数据进行处理
    - 如果数据间无序：使用集合类型
        - 集合类型可以表达一维无序数据
        - for循环可以遍历数据，进而对每个数据进行处理

2.一维数据存储
    ① 使用一个或多个空格分隔进行存储，不换行（缺点：数据中不能存在空格）
    ② 使用英文半角逗号分隔数据进行存储，不换行（缺点：数据中不能存在英文半角逗号）
    ③ 其他方式，使用其他符号或符号组合分隔，建议采用特殊符号（缺点：在数据中不能存在这些特殊符号）

3.一维数据处理
    - 将存储的数据读入程序
        从空格分隔的文件中读入数据  ls = txt.split()
        从特殊符号分隔的文件中读入数据  ls = txt.split("$")
    - 将程序表示的数据写入文件
        采用空格分隔方式将数据写入文件  f.write(" ".join(ls))
        
// 一维数据小结
- 数据的维度：一维、二维、多维、高维
- 一维数据的表示：列表（有序） 集合（无序）
- 一维数据的存储：空格、都好、特殊符号
- 一维数据的处理：字符串方法，.split()和.join()

### 二维数据
1.二维数据的表示
    - 使用列表类型——二维列表
    - 列表类型可以表达二维数据

2.二维数据的格式化和处理
    - 使用两层for循环遍历每个元素
    - 外层列表中每个元素可以对应一行，也可以对应一列

3.CSV格式与二维数据存储
    - CSV数据存储格式 Comma-Separated Values
    - 国际通用的一二维数据存储格式，一般.csv扩展名
    - 每行一个一维数据，采用逗号分隔，无空行
    - Excel和一般编程软件都可以读入或存为csv文件
    
4.CSV数据存储格式
- 如果某个元素缺失，逗号仍要保留
- 二维数据的表头可以作为数据存储，也可以另行存储
- 逗号为英文半角逗号，逗号与数据之间没有额外的空格

5.二维数据的存储
- 按行存或者按行存都可以，由程序决定
- 一般索引习惯：ls[row][column]，先行后列
- 根据一般习惯，外层列表每个元素是一行，按行存

6.二维数据的读入处理
    - 从CSV格式的文件中读入数据
        fo = open(fname)
        ls = []
        for line in fo:
            line = line.replace("\n","")
            ls.append(line.split(","))
        fo.close()
    - 将数据写入CSV格式的文件
        ls = [[], [], []] #二维列表
        f = open(fname, "w")
        for item in ls:
            f.write(",".join(item) + "\n")
        f.close()
    - 二维数据的逐一处理
        ls = [[1, 2], [3, 4], [5, 6]]
        for row in ls:
            for column in row:
                print(column)

7.小结
- 二维数据的表示：列表类型
- CSV格式：逗号分隔表示一维，按行分隔表示二维
- 二维数据的处理：for循环+.split()和.join()

### wordcloud库
1.wordcloud库是优秀的词云展示第三方库
    - 将词云以词语为基本单位，更直观和艺术的展示出来
    
2.wordcloud库基本使用
    wordcloud库把词云当做一个WordCloud对象
    - wordcloud.WordCloud()代表一个文本对应的词云
    - 可以根据文本中词语出现的频率等参数绘制词云
    - 绘制词云的形状、尺寸、颜色都可以设定

3.wordcloud常规方法
    ① w = wordcloud.WordCloud()
        - 以WordCloud对象为基础
        - 配置参数、加载文本、输出文件
        - 配置参数：
            font_path
            max_word
            max_font_size
            min_font_size
            background_color
            mask——配合scipy.misc下的imread函数使用，设置词云显示的形状
    ② w.generate(txt)
        向WordCloud对象w中加载文本txt
    ③ w.to_file(filename)
        将词云输出为图像文件，.png或.jpg
        
        
# 第八周 程序设计方法
## Python程序设计思维
- 自顶向下和自底向上
- 计算思维
    天气预报，MM5模型，进行超级运算
    实证思维+逻辑思维
    
- 量化分析
    机器学习
    
抽象问题的计算过程，利用计算机自动化求解
- 计算思维基于计算机强大的运算能力及海量数据
- 抽象计算过程，注意设计和构成，而非因果
- 变成是将计算思维变成现实的手段

## 计算生态与python语言
1.计算生态
1998年标志着开源生态的建立

没有顶层设计、以功能为单位具备三个特点：
- 竞争发展
- 相互依存
- 迅速更迭

- 以开源项目为代表的大量三方库
    Python语言提供>13万第三方库
- 库的建设经过野蛮生长和自然选择
    同一个功能，Python语言2个以上第三方库
- 库指尖相互关联使用，依存发展
    python库间广泛联系，逐级封装
- 社区庞大，新技术更迭迅速
    AlphaGo深度学习算法采用python开源
    
API（应用程序编写接口）！= 生态
API是经过设计的产物，与生态并不相同

创新：跟随创新、集成创新、原始创新
    - 加速科技类应用创新的重要支撑
    - 发展科技产品商业价值的重要模式
    - 国家科技体系安全和稳固的基础

优秀的三方库：Numpy、request库


2.用户体验
实现功能 -> 用户体验
- 用户体验指用户对产品建立的主观感受和认识
- 关心功能实现，更要关心用户体验，才能做出好产品
- 编程只是手段，不是目的，程序最终为人类服务

方法1：进度展示
    - 如果程序需要计算时间，可能产生等地啊，请增加进度展示
    - 如果程序有若干步骤，需要提示用户，请增加进度展示
    - 如果程序可能存在大量次数的循环，请增加进度展示
    
方法2：异常处理
    - 当获取用户输入，对合规性需要检查，需要异常处理
    - 当读写文件时，对结果进行判断，需要异常处理
    - 当进行输入输出时，对运算结果进行判断，需要异常处理

其他类方法
- 打印输出：特定位置，输出程序运行的过程信息
- 日志文件：对程序异常及用户使用进行定期记录
- 帮助信息：给用户多种方式提供帮助信息

3.基本的程序设计模式
从IPO开始
- input
- Processing
- output

①自顶向下设计

②模块化设计
- 通过函数或对象封装将程序划分为模块及模块间的表达
- 具体包括：主程序、子程序、子程序间关系
- 分而治之：一种分而治之、分层抽象、体系化的设计思想

- 紧耦合：两个部分之间交流很多，无法独立存在
- 松耦合：两个部分之间交流较少，可以独立存在
- 模块内部紧耦合、模块之间松耦合

③配置化设计
- 引擎+配置：程序执行和配置分离，将可选参数配置化
- 将程序开发编程配置文件编写，扩展功能而不修改程序
- 关键在于接口设计，清晰明了、灵活可扩展

应用开发的四个步骤
1.产品定义
2.系统架构
3.设计与实现
4.用户体验

## 单元小结
- 计算思维：抽象计算过程和自动化执行
- 计算生态：竞争发展、相互依存、快速更迭
- 用户体验：进度展示、异常处理等
- IPO、自顶向下、模块化、配置化、应用开发的四个步骤

#第九周 计算生态概览
## 从数据处理到人工智能
1.数据表示->数据清洗->数据统计->数据可视化->数据挖掘->人工智能
- 数据表示：采用合适方法用程序表达数据
- 数据清洗：数据归一化、数据转化、异常值处理
- 数据统计：数据的概要理解、数量、分布、中位数等
- 数据可视化：直观展示数据内涵的方式
- 数据挖掘：从数据分析获得知识，产生数据外的价值
- 人工智能：数据、语言、图像、视觉等方面深度分析与决策

2.三方库的学习
- python库之数据分析
- python库之数据可视化
- python库之文本处理
- python库之机器学习

### Numpy：表示N维数组的最基础库
- python接口使用，C语言实现，计算速度友谊
- python数据分析及科学计算的基础库，支撑Pandas等
- 提供直接的矩阵运算、广播函数、线性代数等

### Pandas:python数据分析高层次应用库
- 提供了简单易用的数据结构和数据分析工具
- 理解数据类型与索引的关系，操作索引即操作数据
- Python最主要的数据分析功能库，基于Numpy进行开发
    Series = 索引 + 一维数据
    DataFrame = 行列索引 + 二维数据
    
### Scipy：数学、科学和工程计算功能库
- 提供了一批数学算法及工程数据运算功能
- 类似于Matlab，可用于如傅里叶变换、信号处理等应用
- Python最主要的科学计算功能库，基于Numpy开发
- 主要功能：傅里叶变换类、信号处理类、线性代数类、图像处理类、稀疏图压缩类、稀疏图运算类、优化算法类



## Python库之数据可视化
### Matplotlib：高质量的二维数据可视化功能库
- 提供了超过100种数据可视化展示效果
- 通过matplotlib.pyplot子库调用各可视化效果
- Python最主要的数据可视化功能库，基于Numpy开发

### Seaborn：统计类数据可视化功能库
- 提供了一批高层次的统计类数据可视化展示效果
- 主要展示数据间分布、分类和现行关系等内容
- 基于Matplotlib开发，支持Numpy和Pandas

### Mayavi：三维科学数据可视化功能库
- 提供了一批简单易用的3D科学计算数据可视化展示效果
- 目前版本是Mayavi2，三维可视化最主要的第三方库
- 支持Numpy、TVTK、Traits、Envisage等第三方库



## Python库之文本处理
### PyPDF2：用来处理pdf文件的工具集
- 提供了一批处理PDF文件的计算功能
- 支持获取信息、分隔/整合文件、加密解密等
- 完全使用Python语言实现，不需要额外依赖，功能稳定
PyPDF2.PdfFileMerger()pdf文件整合

### NLTK：自然语言文本处理第三方库
- 提供了一批简单易用的自然语言文本处理功能
- 支持语言文本分类、标记、语法句法、语义分析
- 最优秀的Python自然语言处理库

### Python-docx：创建或更新Microsoft Word文件的第三方库
- 提供创建或更新.doc .docx等文件的计算功能
- 增加并配置段落、图片、表格、文字等，功能全面



## 机器学习
### Scikit-learn：机器学习方法工具集
- 提供一批统一化的机器学习方法功能接口
- 提供聚类、分类、回归、强化学习等计算功能
- 机器学习最基本且最优秀的Python第三方库

### TensorFlow：AlphaGo背后的机器学习计算框架
- 谷歌公司推动的开源机器学习框架
- 将数据流图作为基础，图节点代表运算，边代表张量
- 应用机器学习方法的一种方式，支撑谷歌人工智能应用

### MXNet：基于神经网络的深度学习计算框架
- 提供可扩展的神经网络及深度学习计算功能
- 可用于自动驾驶、机器翻译、语音识别等众多领域
- Python最重要的深度学习计算框架

## 单元小结
分析Numpy、Pandas、Scipy
可视化matplotlib、seaborn、mayavi
文本处理PyPDF2、nltk、Python-docx
机器学习scikit-learn、TensorFlow、MXNet
