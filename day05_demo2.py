
#!/root/.virtualenvs/flask_py3/bin/python

# from day04_model import User,db


# from day04_demo1 import User
from day04_model import User
ret=User.query.get(1)
# ret =User.query.first()
print(ret)





