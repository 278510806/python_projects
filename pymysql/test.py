import pymysql

USER='root'
PASSWORD='a123'
HOST='localhost'
DATABASE='python_test'

def simpleInsert():
    '''
    插入数据操作
    :return:
    '''
    db=pymysql.connect(HOST,USER,PASSWORD,DATABASE)

    cursor=db.cursor()

    sql='''insert into person(username,pwd) values('jack','1234')'''

    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    db.close()




def argInsert(username,pwd):
    '''
    带参数的插入数据操作
    :param username:
    :param pwd:
    :return:
    '''
    db = pymysql.connect(HOST, USER, PASSWORD, DATABASE)
    cursor=db.cursor()
    sql="insert into person(username,pwd) values('%s','%s')" % (username,pwd)
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()
    db.close()



def argUpdate(username,password):
    pass
def argDelete(username,password):
    pass

def argQuery(id):
    db = pymysql.connect(HOST, USER, PASSWORD, DATABASE)
    cursor = db.cursor()
    sql="select * from person where id>%d" %(id)
    try:
        cursor.execute(sql)
        result=cursor.fetchall()
        print(type(result))
        for row in result:
            print('%d,%s,%s' % (row[0],row[1],row[2]))
        #db.commit()
    except Exception as e:
        print(e)
        #db.rollback()
    db.close()

#argInsert('tom','4321')

argQuery(1)