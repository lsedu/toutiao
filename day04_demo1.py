from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand

'''
1-数据库配置
2-编写模型类

'''

app = Flask(__name__)
#1-数据库配置
class Config(object):
    SQLALCHEMY_DATABASE_URI ="mysql://root:mysql@127.0.0.1/toutiao"
    SQLALCHEMY_TRACK_MODIFICATIONS =True  #
    # SQLALCHEMY_ECHO = True #打印sql语句

app.config.from_object(Config)

#方式1，创建SQLAlchemy对象
db =SQLAlchemy(app)
#创建启动命令管理对象
manager =Manager(app)
#创建数据库迁移工具对象
# Migrate(app,db)
migrate = Migrate(app,db)
#向启动命令管理对象中添加迁移命令
manager.add_command("db",MigrateCommand)


class User(db.Model):
    """
    用户基本信息
    """
    __tablename__ = 'user_basic'

    class STATUS:
        ENABLE = 1
        DISABLE = 0

    id = db.Column('user_id', db.Integer, primary_key=True, doc='用户ID')
    # mobile = db.Column(db.String, doc='手机号')

    mobile = db.Column(db.VARCHAR(11), doc='手机号')
    password = db.Column(db.String(32), doc='密码')
    name = db.Column('user_name', db.String(20), doc='昵称')
    profile_photo = db.Column(db.String(20), doc='头像')
    last_login = db.Column(db.DateTime, doc='最后登录时间')
    is_media = db.Column(db.Boolean, default=False, doc='是否是自媒体')
    is_verified = db.Column(db.Boolean, default=False, doc='是否实名认证')
    introduction = db.Column(db.String(20), doc='简介')
    certificate = db.Column(db.String(20), doc='认证')
    article_count = db.Column(db.Integer, default=0, doc='发帖数')
    following_count = db.Column(db.Integer, default=0, doc='关注的人数')
    fans_count = db.Column(db.Integer, default=0, doc='被关注的人数（粉丝数）')
    like_count = db.Column(db.Integer, default=0, doc='累计点赞人数')
    read_count = db.Column(db.Integer, default=0, doc='累计阅读人数')

    account = db.Column(db.String(20), doc='账号')
    email = db.Column(db.String(20), doc='邮箱')
    status = db.Column(db.Integer, default=1, doc='状态，是否可用')

    #模型迁移时要求字段包含长度限制，varchar,string
# sqlalchemy.exc.CompileError: (in table 'user_profile', column 'real_name'): VARCHAR requires a length on dialect mysql

class UserProfile(db.Model):
    """
    用户资料表，不常用
    """
    __tablename__ = 'user_profile'

    class GENDER:
        MALE = 0
        FEMALE = 1

    id = db.Column('user_id', db.Integer, primary_key=True, doc='用户ID')
    gender = db.Column(db.Integer, default=0, doc='性别')
    birthday = db.Column(db.Date, doc='生日')
    real_name = db.Column(db.String(20), doc='真实姓名')
    id_number = db.Column(db.String(18), doc='身份证号')
    id_card_front = db.Column(db.String(128), doc='身份证正面')
    id_card_back = db.Column(db.String(128), doc='身份证背面')
    id_card_handheld = db.Column(db.String(128), doc='手持身份证')
    ctime = db.Column('create_time', db.DateTime, default=datetime.now, doc='创建时间')
    utime = db.Column('update_time', db.DateTime, default=datetime.now, onupdate=datetime.now, doc='更新时间')
    register_media_time = db.Column(db.DateTime, doc='注册自媒体时间')

    area = db.Column(db.String(20), doc='地区')
    company = db.Column(db.String(20), doc='公司')
    career = db.Column(db.String(20), doc='职业')


class Relation(db.Model):
    """
    用户关系表
    """
    __tablename__ = 'user_relation'

    class RELATION:
        DELETE = 0
        FOLLOW = 1
        BLACKLIST = 2

    id = db.Column('relation_id', db.Integer, primary_key=True, doc='主键ID')
    user_id = db.Column(db.Integer, doc='用户ID')
    target_user_id = db.Column(db.Integer, doc='目标用户ID')
    relation = db.Column(db.Integer, doc='关系')
    ctime = db.Column('create_time', db.DateTime, default=datetime.now, doc='创建时间')
    utime = db.Column('update_time', db.DateTime, default=datetime.now, onupdate=datetime.now, doc='更新时间')


# 对于批量添加也可使用如下语法
# db.session.add_all([user1, user2, user3])
# db.session.commit()

# user = User(mobile='15612300001', name='bobop')
# db.session.add(user)
# user = User(mobile='15612300002', name='中gong')
# db.session.add(user)
# user = User(mobile='15612300003', name='川普')
# db.session.add(user)
# user = User(mobile='15612300004', name='习特勒')
# db.session.add(user)
# user = User(mobile='15612300005', name='小ding')
# db.session.add(user)
# user = User(mobile='15612300006', name='哈哈')
# db.session.add(user)
# user = User(mobile='15612300007', name='jack')
# db.session.add(user)
# user = User(mobile='15612300008', name='bo')
# db.session.add(user)
# user = User(mobile='15612300009', name='bobo')
# db.session.add(user)
# user = User(mobile='18520395700', name='波少bo')
#
# db.session.add(user)
# db.session.commit()

# profile = UserProfile(id =2 ,gender= 1)
# profile1 = UserProfile(id =18,gender= 1)
# profile2 = UserProfile(id =19 ,gender= 1)
# profile3 = UserProfile(id =20 ,gender= 0)
# profile4 = UserProfile(id =21 ,gender= 1)
# profile5 = UserProfile(id =22 ,gender= 0)
# profile6 = UserProfile(id =23 ,gender= 1)
# profile7 = UserProfile(id =24 ,gender= 1)
# profile8 = UserProfile(id =25 ,gender= 0)
# profile9 = UserProfile(id =26 ,gender= 1)
#
# db.session.add_all([profile,profile1,profile2,profile3,profile5,profile4,profile6,profile7,profile8,profile9,])
# db.session.commit()

relation =Relation(user_id =1,target_user_id=2,relation=1)
db.session.add(relation)
relation =Relation(user_id =1,target_user_id=20,relation=1)
db.session.add(relation)
relation =Relation(user_id =1,target_user_id=23,relation=2)
db.session.add(relation)
relation =Relation(user_id =2,target_user_id=26,relation=1)
db.session.add(relation)
relation =Relation(user_id =2,target_user_id=18,relation=1)
db.session.add(relation)
relation =Relation(user_id =18,target_user_id=20,relation=1)
db.session.add(relation)
# relation =Relation(user_id =19,target_user_id=26)
# sqlalchemy.exc.OperationalError: (MySQLdb._exceptions.OperationalError) (1048, "Column 'relation' cannot be null")
# [SQL: INSERT INTO user_relation (user_id, target_user_id, relation, create_time, update_time) VALUES (%s, %s, %s, %s, %s)]
# [parameters: (19, 26, None, datetime.datetime(2019, 7, 15, 10, 42, 47, 343284), datetime.datetime(2019, 7, 15, 10, 42, 47, 343295))]
db.session.add(relation)
relation =Relation(user_id =19,target_user_id=2,relation=1)
db.session.add(relation)
relation =Relation(user_id =25,target_user_id=2,relation=1)
db.session.add(relation)
relation =Relation(user_id =26,target_user_id=1,relation=1)
db.session.add(relation)
relation =Relation(user_id =26,target_user_id=2,relation=1)
db.session.add(relation)
relation =Relation(user_id =26,target_user_id=18,relation=2)
db.session.add(relation)
# relation =Relation(user_id =26,target_user_id=19)
db.session.add(relation)
relation =Relation(user_id =26,target_user_id=20,relation=1)
db.session.add(relation)
relation =Relation(user_id =26,target_user_id=22,relation=2)
db.session.add(relation)
relation =Relation(user_id =26,target_user_id=23,relation=1)
db.session.add(relation)
db.session.commit()


# [<User 1>, <User 2>, <User 18>, <User 19>, <User 20>, <User 21>, <User 22>, <User 23>, <User 24>, <User 25>, <User 26>]

#查询-----------------------
# for each in User.query.all():
#     print(each.name)
# print(User.query.all())
# print(User.query.first().name)

# if __name__ == '__main__':
#     app.run()
#     # manager.run()
