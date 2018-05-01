import textwrap

str_='''
        Python, an object-oriented programming language for computer programming, was invented in 1989 by 
    Guido van Rossum of the Netherlands and the first public release in 1991.
'''
#切割为每10个字符为一组，组成的list
print(textwrap.wrap(str_,width=10))
#切割为每10个字符为一组的字符串
print(textwrap.fill(str_,width=10))

print(textwrap.indent(str_,prefix=' '))