#======================string模块=============================================
import string

# Templete类
vals={'name':'jack','sex':'male','age':20}
# $var和${var}效果一样，${var}可以区分两边的字符
# 模板不考虑类型，值会自动转换为字符串，再将字符串插入到文本中
person=string.Template('''
    name:$name
    sex:$sex
    age:$age
    desc:$name and ${sex} and $age
''')
# substitutefangfa
print(person.substitute(vals))

person2=string.Template("person2 description:$missing and $age and $sex")
try:
    print(person2.substitute(vals))
except KeyError as e:
    print(e)
#safe_substiute:如果没有对应的key值，使用safe_substiute方法可以不抛出异常
print(person2.safe_substitute(vals))


