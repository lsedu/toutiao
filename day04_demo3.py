from flask import Flask
from day04_demo1 import User,db
app = Flask(__name__)

'''新增一条记录，实例对象'''
user =User(mobile="15601781609",name="bobop")
db.session.add(user)
#提交数据
db.session.commit()




if __name__ == '__main__':
    app.run()