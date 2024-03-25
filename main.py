from send import MailHelper

class MailTemplate:
    '''
        邮箱发送模版，定义了，谁来法，发给谁，发什么
    '''
    def __init__(self,memo:str,from_user:str,receive_users:list,cc_user:list,file_path,is_valid:bool,subject:str|None):
        self.memo =memo 
        self.from_user = from_user  
        self.receive_users = receive_users
        self.cc_user = cc_user 
        self.file_path = file_path
        self.is_valid = is_valid
        self.subject = subject

class Sender:
    def __init__(self,email_host:str,email_port:int,username:str,email:str,password:str):
        '''Sender class'''
        '''
            self.email_host = email_host # 邮箱服务器地址
            self.email_port = email_port # 邮箱服务器端口
            self.username = username # 发送邮件的地址用户名：比如 张三
            self.email =  self.email # 发送邮件的地址 
            self.password = password # 发送邮件的密码
        '''
        self.email_host = email_host
        self.email_port = email_port
        self.username = username
        self.email =  email
        self.password = password
    
    def send(self,all_send_mail):
        '''
            all_send_mail 包含所有邮件模版对象的列表
        '''
        for mail_template in all_send_mail:
            
            mail_helper = MailHelper(host=self.email_host,port=self.email_port,username=self.username,passwd=self.password)
            try:
                mail_helper.send_mail(
                    user=self.username,
                    From=self.email,
                    To=mail_template.send_mail,
                    Header="123123",
                    content="Content"
                )
            except Exception:
                print("发送失败：",mail_template.Memo)
         

######################################################################
######################### 发送邮件的配置 ###############################
__WECHAT_CONFIG__  = {
        "username":"夏志", # 企业微信中文名
        "email":"xiazhi.donson@gmail.com",# 企业微信email
        "password":"3qMcgifxwnx3CMSX",    # 发送邮件安全代码
        "email_host":"smtp.exmail.qq.com",# 企业邮箱地址(官方提供)
        "email_port":465                  # 企业邮箱端口(官方提供)  SSL协议，邮件加密 
    }
###################################################################### 


def main():
    sender_obj = Sender(email_host=__WECHAT_CONFIG__["email_host"],
                    email_port=__WECHAT_CONFIG__["email_port"],
                    username=__WECHAT_CONFIG__["username"],
                    email=__WECHAT_CONFIG__["email"],
                    password=__WECHAT_CONFIG__["password"])

    # sender_obj = Sender(**__SEND_CONFIG__)  #快捷写法

    mail_config = [
        {"memo":"江西东信的邮件","receive_users":["zhengmengyue@donson.com","xiazhi@donson.com"],"cc_users":["xiazhi@donson.com.cn"],"file_path":"./testdir","suject":None}

    ]

    all_mail_template = []

    for row_config in mail_config:
        pass

    sender_obj.send(mail_config)


    # all_email_list.append(MailTemplate(memo="江西东信的邮件",
    #                                from_user=send_users['emil'],
    #                                receive_users=res,cc_user=res,
    #                                file_path='./testdir',is_valid=False,subject=None))


if __name__ == "__main__":
    main()
# all_mail_settings = []
# res = [val['emil'] for val in receive_users] 
# # 发给mkbk的邮件
# all_email_list = []


# # 每需要发送一个邮件，就增加一个配置
# all_email_list.append(MailTemplate(memo="江西东信的邮件",
#                                    from_user=send_users['emil'],
#                                    receive_users=res,cc_user=res,
#                                    file_path='./testdir',is_valid=False,subject=None))

# sender_obj.send_mail(all_email_list)

a = str("123")



 