import poplib

p=poplib.POP3('pop3.163.com')
p.user('yourmailusername')
p.pass_('yourmailpass')

stat,msgs,siz=p.retr(p.stat()[0])
for line in msgs:
    print(line)
p.close()