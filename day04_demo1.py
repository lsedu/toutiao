from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand

from day04_model import User,UserProfile,Relation


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
