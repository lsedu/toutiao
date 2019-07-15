#!/usr/bin/env python
from sqlalchemy import func
from sqlalchemy.orm import load_only

from day04_model import User, Relation, db, UserProfile

#1，普通查询
# ret=User.query.get(1)
# ret =User.query.first()

#2过滤查询
#2-1，查询id为1的用户
# ret =User.query.filter(id ==22)  #XXX
# ret =User.query.get(1)
# ret =User.query.filter(User.id ==1).first()   #单个 filter后加  .first() 多个用 .all()
# ret =User.query.filter_by(id=22).first()

#2-3,查询name为bobo的用户
# ret =User.query.filter_by(name ='bobo').first()

#2-4,查询name 为bobo 并且id 为25的用户
# ret =User.query.filter(User.name == 'bobo',User.id == 25).first()
# ret = User.query.filter_by(name = 'bobo',id =25).first()

#2-5,查询 id >10 的用户
# ret = User.query.filter(User.id >10).all()
# ret =User.query.filter_by(id =18).first() # filter_by 只能用在 = 号情况

#2-6，查询name ，以bobo开头
# ret =User.query.filter(User.name.startswith('bobo')).all()
# ret = User.query.filter_by()

#3，综合查询
#3-1，查询所有用户且按照id 倒序
# select * from user_basic order by user_id desc;
# ret = User.query.order_by(User.id.desc()).all()   #.desc()

#3-2,偏移为2，限制3条查询
# select * from user_basic limit 2,3
# ret =User.query.offset(2).limit(3).all()

#3-3,查询name以bo开始，以id降序，偏移1，显示3
# select *from user_basic where user_name like 'bo%' order by user_id desc limit 1,3;
# ret = User.query.filter(User.name.startswith('bo')).order_by(User.id.desc()).offset(1).limit(3).all()
#不要漏了 .all()  ，   .startswith() 注意拼写

#3-4,查询name以bo开始，显示用户名字和手机号
# select user_name,mobile from user_basic where user_name like 'bo%';
# load_only(类名.属性) 注意格式
# ret = User.query.options(load_only(User.name,User.mobile )).filter(User.name.startswith('bo')).all()
# ret = User.query.options(load_only(User.name,User.mobile )).filter(User.id ==1).first()

#4,使用SQLAlchemy进行分组聚合查询： 格式：db.session.query(xxx).group_by(xxx).all()
# 4-1查询每一个人关注的用户数
# XXX:   select user_id,count(r.target_user_id) from user_relation as r inner join user_basic as b group by b.user_id;
# select user_id,count(target_user_id) from user_relation  group by user_id;
# ret=db.session.query(Relation.user_id,func.count(Relation.target_user_id)).group_by(Relation.user_id).all()
#注意点 func.count() , db.session.query() ,此处指定字段没有使用 .options(load_only())

#5,使用SQLAlchemy定义relationship字段进行关联查询。。要在模型中加入外键，映射
#5.1 查询id 为1 的用户性别：
# select p.gender from user_profile as p inner join user_basic as b where b.user_id =1;
# ret = User.query.filter(User.id == 18).first()  #print(ret.profile.gender)

#sql:
#INFO sqlalchemy.engine.base.Engine SELECT user_profile.user_id AS user_profile_user_id, user_profile.create_time AS user_profile_create_time, user_profile.update_time AS user_profile_update_time, user_profile.gender AS user_profile_gender, user_profile.birthday AS user_profile_birthday, user_profile.real_name AS user_profile_real_name, user_profile.id_number AS user_profile_id_number, user_profile.id_card_front AS user_profile_id_card_front, user_profile.id_card_back AS user_profile_id_card_back, user_profile.id_card_handheld AS user_profile_id_card_handheld, user_profile.register_media_time AS user_profile_register_media_time, user_profile.area AS user_profile_area, user_profile.company AS user_profile_company, user_profile.career AS user_profile_career
# FROM user_profile WHERE user_profile.user_id = %s

#5.2 查询 id为1 的用户关注了哪些用户：


print('ret:%s'%ret)
# print(ret.profile.gender)
# print(ret.profile_photo)
# print(ret.name)
# print(ret.mobile)




