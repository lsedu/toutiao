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

