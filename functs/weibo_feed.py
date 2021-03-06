import os
import sqlite3


class WeiboFeed:
    def __init__(self):
        self.username='unknown'
        self.tool='unknown'
        self.datetime='1900-00-00 00:00'
        self.type='unknown'
        self.likes=-1
        self.comments=-1
        self.content=''
        self.forward_content =''
        self.forward_username=''
        self.url=''
        self.img=''
        self.video=''
        self.userid =0
        self.reposts=-1
        self.forward_comments=-1
        self.forward_likes = -1
        self.forward_reposts=-1
        self.forward_userid = 0
        self.blogid=0
    def insert_into_table(self):
        sql = "insert into mytable\
        (username,tool,datetime,type,likes,comments,content,forward_content,forward_username,url,img,video,userid,reposts,forward_comments,forward_likes,forward_reposts,forward_userid,blogid) " \
              "values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
        db = getDB()
        cur = db.cursor()
        cur.execute(sql, [self.username, self.tool, self.datetime, self.type,
                          self.likes,  self.comments, self.content, self.forward_content
            , self.forward_username, self.url,self.img,self.video,self.userid,self.reposts,self.forward_comments,self.forward_likes ,self.forward_reposts,self.forward_userid,self.blogid])
        db.commit()
        cur.close()
        db.close()
def getDB():
    BASE_PATH = os.path.abspath(os.path.dirname(__file__))
    sqlite_filename = os.path.join(BASE_PATH, 'Weibo.db')
    db = sqlite3.connect(sqlite_filename)
    if is_table_existed('mfytable') == False:
        cur = db.cursor()
        cur.execute('create table fmytable('
                    'username text,'
                    'tool text,'
                    'datetime text,'
                    'type text,'
                    'likes integer,'
                    'comments integer'
                    ',content text,'
                    'forward_content text,'
                    'forward_username text'
                    ',url text,'
                    'id integer PRIMARY KEY AUTOINCREMENT,'
                    'img text,'
                    'video text,'
                    'userid integer,'
                    'reposts  integer,'
                    'forward_likes integer,'
                    'forward_comments integer,'
                    'forward_reposts integer,'
                    'forward_userid integer,'
                    'blogid integer)')
    return db


def is_table_existed(table_name):
    BASE_PATH = os.path.abspath(os.path.dirname(__file__))
    sqlite_filename = os.path.join(BASE_PATH, 'Weibo.db')
    db = sqlite3.connect(sqlite_filename)
    cur = db.cursor()
    try:
        cur.execute(('select * from %s') % table_name)
    except Exception as e:
        return False
    return True


def is_row_existed(table_time, key, value):
    db = getDB()
    cur = db.cursor()
    sql = 'select count(%s) from %s where %s = ?' % (key, table_time, key)
    cur.execute(sql, [value])
    counts = cur.fetchall()
    if (int(counts[0][0]) >= 1):
        cur.close()
        db.close()
        return True
        # print('重复了', index_a.getText())
    else:
        return False
