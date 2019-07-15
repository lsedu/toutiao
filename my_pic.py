import base64
f = open('static/img/001.png','rb') #二进制方式打开图文件
ls_f=base64.b64encode(f.read()) #读取文件内容，转换为base64编码
f.close()
# print(ls_f)

# base64字符串转化为图片
# imgdata = base64.b64decode(ls_f)
# file =open('static/img/001_2.png','wb')
# file.write(imgdata)
# file.close()