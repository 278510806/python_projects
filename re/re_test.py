import re

#match 对象
def match_():
    pattern = "jack"
    str_ = "hello jack and tom"

    match = re.search(pattern, str_)
    # match对象包含有关匹配的属性信息，如，原输入字符串，使用的正则表达式，以及模式在字符串中出现的位置等信息
    print(match.re.pattern, match.string, match.start(), match.end())

    s = match.start()
    e = match.end()

    print(str_[s:e])

#pattern的编译
#通过在加载模块时进行预编译所有表达式，可以把编译工作放到应用题开始时，提高了程序运行是的效率
def compile_test():
    comPatterns=[re.compile(p) for p in ['jack','mike']]
    str_="hello jack and tom"
    for pattern in comPatterns:
        if pattern.search(str_):
            print(pattern,'match!')
        else:
            print(pattern,'not match!')

#findall方法
#返回所有匹配项，并组成列表
def findall_():
    pattern='ab'
    str_='aabbaaabbaabbaacaaacaa'
    all=re.findall(pattern,str_)
    print(all)
    for match in all:
        print(match)

if __name__=='__main__':
    #match_()
    #compile_test()
    findall_()