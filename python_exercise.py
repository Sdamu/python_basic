
# coding: utf-8

# In[1]:


format = "Hello, %s. %s enough for ya?"


# In[3]:


values = ('world', 'Hot')


# In[4]:


print(format % values)


# In[5]:


format = "Pi with three decimals: %.3f"


# In[7]:


from math import pi
print (format % pi)


# In[8]:


# 如果需要转换的元组作为转换表达式的一部分存在，那么必须将它用圆括号括起来，避免出错
"%s plus %s equals %s" % (1, 1, 2)


# ## 3.3.1 简单转换

# 简单转换只需要写出转换类型，使用起来很简单：

# In[9]:


'Price of eggs: $%d' % 42


# In[1]:


'Hexadeciaml price of eggs: %x' %42


# ## 3.4 字符串方法
# 这一节介绍一些比较常见的字符串方法: 

# ### 3.4.1 find
# find 方法乐意在一个比较长的字符串中查找子串。它返回子串所在位置的最左端索引。如果没有找到则返回 -1.

# In[2]:


'With a moo-moo here. and a moo-moo there'.find('moo')


# In[4]:


title = "Monty Python's Flying Circus"
title.find('Monty')


# In[5]:


title.find('Python')


# In[6]:


title.find('Flying')


# In[7]:


title.find('Zirquss')


# **需要注意的是，函数 find 返回的并不是布尔值。如果返回的是0，则说明在位置 0 处找到了想要找的字符串**
# 此外，这个方法还可以接受可选的起始点和结束点参数：

# In[8]:


subject = '$$$ Get rich now!!! $$$'
subject.find('$$$')


# In[9]:


subject.find('$$$', 1) # 只提供起始点位置


# In[10]:


subject.find('!!!')


# In[12]:


subject.find('!!!',0,16)


# **注意，由起始和终止指定的范围（第二个和第三个参数）包含第一个索引，但是并不包含第二个索引，这在 python 中是一个惯例**

# ### 3.4.2 join
# join 方法是一个非常重要的字符串方法，它是 split 方法的逆方法，用来连接序列中的元素。

# In[13]:


seq = [1, 2, 3, 4, 5]
sep = '+'
sep.join(seq)  # 连接数字列表


# In[14]:


seq = ["1", "2", "3", "4", "5"]
sep.join(seq)  # 连接字符串列表


# In[16]:


dirs = '', 'usr','bin', 'env'
'/'.join(dirs)


# In[17]:


print('C:'+ '\\'.join(dirs))


# 可以看到，需要被连接的序列元素必须都是字符串。注意最后两个例子中使用了目录的列表，而在格式化时，根据不同系统下的约定，使用了不同的分隔符号

# ### 3.4.3 lower
# lower 方法返回字符串的小写字母版

# In[18]:


"Tronheim Hammer Dance".lower()


# 如果想要比那些“不区分大小写”的代码的话，那么这个方法就派上用场了————代码会忽略大小写状态。
# 例如，如果想在列表中查找一个用户名是否存在：列表中包含字符串 ‘gumby’,而用户输入的是 ‘Gumby’，就找不到了
# 如果存储的是 “Gumby” 而用户输入 ‘gumby’ 甚至是 ‘GUMBY’，结果也是一样的。解决方法就是在存储和搜索时把所有名字都转换成为小写。如下所示：

# In[19]:


name = 'Gumby'


# In[20]:


names = ['gumby', 'smith', 'jones']


# In[22]:


if name.lower() in names:
    print ('Found it!')


# ### 3.4.4 replace
# replace 方法返回某字符串的所有匹配项均被替换之后得到字符串。

# In[23]:


"This is a test".replace('is', 'eez')


# ### 3.4.5 split
# 这是一个非常重要的字符串方法，它是 join 的逆方法，用来将字符串分割成为序列。

# In[24]:


'1+2+3+4+5'.split('+')


# In[25]:


'/usr/bin/env'.split('/')


# In[26]:


'Using the default'.split()


# **注意，如果不提供任何分隔符，则程序会把所有空格作为分隔符（空格，制表，换行等）。**

# ### 3.4.6 strip
# strip 方法返回去除两侧（不包括内部）空格的字符串：

# In[1]:


'        internal whitespace is kept        '.split()


# 这个方法和 lower 方法一起使用的话就可以很方便的对比输入和存储的值。
# 假设用户在输入名字的时候无意中在名字后面加上了空格：

# In[2]:


names = ['gumby', 'smith', 'jones']
name = 'gumby '
if name in names: 
    print('Found it!')


# In[3]:


if name.strip() in names:
    print('Found it!')


# 此外，这个函数也可以指定需要去除的字符，将他们列为参数即可。

# In[4]:


'*** SPAM * for * everyone!!! ***'.strip(' *!')


# 出现上面这个结果的原因是，**这个方法只能去除两侧的字符，所以字符串中间的星号并没有被去掉。**

# ### 3.4.7 translate
# translate 方法和 replace 方法一样，可以替换字符串中的某些部分，但是和前者不同的是，translate 方法只处理单个字符
# 使用这个方法的方式有很多（比如替换换行符或者其他因平台而异的特殊字符）。但是让我们考虑一个简单的例子（很简单的例子）：
# 假设需要将纯正的英文文本转换为带有德国口音的版本。为此，需要把字符 c 替换为 z。
# 使用 translate 转换之前，需要先完整一张转换表。转换表中是以某字符替换某字符的对应关系。因为这个表（事实上是字符串）有多达256个项目，我们还是不要自己写了, 使用string 模块里面的 maketrans 函数即可。
# maketrans 函数接受两个参数：两个等长的字符串，表示第一个字符串中的每个字符都用第二个字符串中相同位置的字符替换。
# 例子如下所示：

# In[5]:


from string import maketrans
table = maketrans('cs', 'kz')


# In[6]:


import string


# # 4.字典

# 我们已经了解到，列表这种数据结构适合于将值组织到一个结构中，并且通过编号对其进行引用。在下面的内容中，将会接触到一种新的数据结构，这种数据结构称为“映射”(mapping)。字典是Python 中唯一內建的映射类型。字典中的值并没有特殊的顺序，但是都存储在一个特定的键(key)下。键可以使数字、字符甚至是元组。

# ## 4.1 字典的使用
# 字典这个名称已经给出了有关这个数据结构功能的一些提示：一方面，对于普通的书来说，都是按照从头到尾的顺粗进行阅读。但是如果愿意，也可以快速翻到某一页，这有点像 Python 中的列表。另一方面，构造字典的目的，不管是现实中的字典还是在 Python 中的字典，都是为了可以通过轻松的查找某个特定的词语（键），从而找到它的定义（值）。
# 在某些情况下，字典比列表更加适用，比如说：
# - 表示一个游戏棋盘的状态，每个键都是有坐标值组成的元素
# - 存储文件修改时间，用文件名作为键
# - 数字电话/地址簿

# ## 4.2 创建和使用字典

# In[1]:


phonebook={'Alice':'2341', 'Beth':'9102', 'Cecil':3258}


# 字典由多个键值以及与其对应的键-值对组成（我们也把键-值对 称为项）。在上面的例子中，名字是键，电话号码是值。每个键和它的值之间用冒号（：）进行隔开，项之间的项用逗号隔开，而整个字典有一对大括号括起来。
# **需要注意的是**，字典中的键是唯一的，而值并不唯一。
