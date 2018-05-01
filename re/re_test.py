import re

pattern="jack"
str_="hello jack and tom"

match=re.search(pattern,str_)
#match对象包含有关匹配的属性信息，如，原输入字符串，使用的正则表达式，以及模式在字符串中出现的位置等信息
print(match .re.pattern,match.string,match.start(),match.end())