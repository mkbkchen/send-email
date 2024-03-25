import smtplib
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr

import time 


class MailHelper:
    def __init__(self,host:str,port:int,username:str,passwd:str) -> None:
        self.host = host
        self.port = port
        self.username = username
        self.passwd = passwd

    def login(self):
        con = smtplib.SMTP_SSL(self.host, self.port)
        con.login(self.username, self.passwd)
        return con

    def send_mail(self,user:str,From:str,To:str,Header:str,content:str):
        try:
            con = self.login()
            msg = MIMEMultipart()
            # res = formataddr(["夏志",From_str]) 
            msg['From'] = From 
            msg['To'] = To
            msg['Subject'] = Header
            html = MIMEText(content, 'html', 'utf-8')  #这里支持多种文本
            msg.attach(html) 
            con.sendmail(user, To, msg.as_string()) 
            con.quit()
        except Exception as E:
            print("发送邮件错误：",E)
            

# m = Mail(host="smtp.exmail.qq.com",port=465,username="xiazhi@donson.com.cn",passwd="3qMcgifxwnx3CMSX")

# content_html = '''
# <html>
# <h1>你好啊！ </h1>
# </html>
# '''

# mail_user = 'xiazhi@donson.com.cn'
 
 
# header = "Hello" #设置邮件的头部信息
# all_mail = [ "zhangmengyue@donson.com.cn"]
# for user_mail in all_mail:
# 	m.send_mail(user="xiazhi@donson.com.cn",
#     From_str=mail_user,\
#     To=user_mail,\
#     Header=header,content=content_html)  
 
# time.sleep(2) # 



 

# list1 = [[1,2,3],[4,5,6],[7,8,9],[1,3,5]]

# new_list1 = [i[1] for i in list1 if  i[1] % 2 == 0 ] # 此时i就是每次迭代的字列表 i[i] 表示要放到新列表的元素是自列表的第2个元素

# print(new_list1) #  [2, 5, 8, 3]numbers = [1, 2, 3, 4, 5]

# numbers = [1, 2, 3, 4, 5]

# squares = [x * 2 if x < 3 else x for x in numbers ]  
# print(squares) # [1, 2, 3, 4, 5


# list_1 = [1,2,3]
# list_2 = [4,5,6]
 
# new_list = [ x + y  for x in list_1 for y in list_2]

# print(new_list) 
            
# old_dict = {"Jeck":24,"Amy":16}
# new_dict = {v:k for k,v in old_dict.items()}
# print(new_dict)

# old_dict =  {"Jeck":24,"Amy":16}

# new_dict = {k:v*2 for k,v in old_dict.items()}
# print(new_dict)
            
# def add(x, y):
#     return x + y
# result = add(3, 5)

# a = lambda x, y: x + y 
 

# def mkbk(x,y,mkbk_f):
#     return mkbk_f(x,y)


# res1 = mkbk(3,4,lambda x,y: x + y)
# res2 = mkbk(3,4,lambda x,y: x * y)
# res3 = mkbk(3,4,lambda x,y: x - y)
# print(res1,res2,res3)
            
# numbers = [1, 2, 3, 4, 5]
# # print(lambda x: x**2, numbers)  
# a = lambda x: x**2, numbers
 
#   #map()函数是一个高阶函数，它接收一个函数作为参数，并对该函数作用到可迭代对象中的每个元素上，返回一个新的可迭代对象，如列表或迭代器
# squared = list(map(lambda x: x**2, numbers))
# print(squared)  # 输出 [1, 4, 9, 16, 25]
            

my_dict = {'z': 2, 'a': 1, 'c': 3}
# for k,v in my_dict.items():
#     print(k,v)

# orted_values = sorted(my_dict.items(), key=lambda x: x[1])
# print("按值排序后的结果：", orted_values)
# # 按键（key）进行排序并输出结果
sorted_keys = sorted(my_dict.items(), key=lambda x: x[0])
print("按键排序后的结果：", sorted_keys)