#!/usr/bin/env python
from sqlalchemy.orm import load_only

from day04_model import User

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


# print('ret:%s'%ret)





