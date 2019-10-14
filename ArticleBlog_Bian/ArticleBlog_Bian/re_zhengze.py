import re
# re.findall()匹配所有满足正则的条件的字符
# string = 'hello word I am your friend_Tom'
# 原样匹配,通常结合其他匹配使用,匹配前边是字母的o

# .匹配非换行符的任意字符
# strings = "hello word \n I am your friend_Tom \t"
# result = re.findall(r"....",strings)
# \d匹配字符串当中的数字
# strings = "hello word \n I am your 19 29 friend_Tom \t"
# result = re.findall(r"\d\d",strings)
# \D匹配字符串当中的非数字
# \w匹配数字,字母,下划线
# strings = "hello word \n I am your friend_Tom \t"
# result = re.findall(r"\w",strings)
# \W匹配非数字,非字母,非下划线
# []匹配字符串中任意一个元素
# strings = "hello word \n I am your friend_Tom \t"
# result = re.findall(r"[l1]",strings)
# ()组匹配,会将组外的匹配条件,作为条件进行匹配,返回组内匹配到的内容
# strings = "hello word \n I am your \t friend_Tom \t"
# result = re.findall(r"(e)",strings)
# \d\w 匹配一个数字,字母,下划线或者下划线的数字
# strings = "hello word \n I am your 19 ,20,10 friend_Tom \t"
# result = re.findall(r"\d\w",strings)
# ()命名组 ?p<名称> 以这样的格式起名字
# strings = "hello word \n I am your 19 ,20,10 friend_Tom \t"
# result = re.findall(r"()",strings)
# *匹配0到任意多个
# +匹配1到多次
# strings = "hello word \n I am your 19 ,20,10 friend_Tom \t"
# result = re.findall(r".+",strings)
# ?匹配0-1次
# strings = "hello word \n I am your 19 ,20,10 friend_Tom \t"
# result = re.findall(r".?",strings)
# {}匹配指定次
# strings = "hello word \n I am your 19 ,20,10 friend_Tom \t"
# result = re.findall(r".{3}",strings)

# strings = "hello word \n I am your 19 ,20,10 friend_Tom \t"
# result = re.findall(r".{2,3}",strings)
# 特殊匹配
# ^开始
# strings = "hello word \n I am your 19 ,20,10 friend_Tom \t"
# result = re.findall(r"^",strings)
# $结尾
# strings = "hello word \n I am your 19 ,20,10 friend_Tom \t"
# result = re.findall(r"$",strings)
# print(result)

