# -*- coding = utf-8 -*-
# @Time :2021/5/17 9:40
# @Author: Hanayuzu
# @File :银行管理系统2.0


from pymysql import *
import time

class User(object):

    def __init__(self, name=0, yhk=0, password=0, call_number=0, money=0, id_card=0, block=0):
        self.name = name
        self.yhk = yhk
        self.password = password
        self.call_number = call_number
        self.money = money
        self.id_card = id_card
        self.block = block
        self.conn = connect(host='127.0.0.1',
                            user='admin123',
                            password='admin123',
                            port=3306,
                            db='Bank')

    def start(self):
        menu = '''
    =======================金职银行管理系统=======================
    0 : 开户          1 : 取款          2 : 转账          3 : 解锁  
    
    4 : 查询          5 : 存款          6 : 锁定          7 : 退出  
    =======================金职银行管理系统=======================
'''
        return menu

# 开户类，单独调用来开户
class Open_Account(User):

    def __init__(self, name=0, yhk=0, password=0, call_number=0, money=0, id_card=0, block=0):
        User.__init__(self, name, yhk, password, call_number, money, id_card, block)
    # 开始方法，输出开户菜单
    def start(self):
        menu = '''
    ===========================开户系统===========================
    ===========================开户系统===========================
    ===========================开户系统===========================
'''
        return menu

    def Create_Account(self):
        cur = self.conn.cursor()
        sql = "INSERT INTO `users` (name, yhk, password, callnumber, money, idcard, block) " \
              "VALUES ('{}',MD5({}),'{}',{},0,'{}','0')" \
            .format(self.name, self.yhk, self.password, self.call_number, self.id_card)
        cur.execute(sql)
        sql2 = "SELECT id,yhk FROM `users` GROUP BY id DESC LIMIT 1"
        cur.execute(sql2)
        data = cur.fetchall()
        return ('\n尊敬的', self.name + '先生', '恭喜您成为本行第 `' + str(data[0][0]) + '` 位用户\n'
              + '您的银行卡号为：' + data[0][1] + '\n请妥善保存喵~')


class Get_info(User):

    # 获取银行卡信息的类
    def __init__(self, id_card=0, name=0, yhk=0, password=0, call_number=0, money=0, block=0):
        User.__init__(self, name, yhk, password, call_number, money, id_card, block)

    # 获取所有信息
    def get_info(self, yhk, password):
        cur = self.conn.cursor()
        sql = "SELECT * FROM `users` WHERE `yhk`='{}' AND `password`='{}'".format(yhk, password)
        cur.execute(sql)
        data = cur.fetchall()
        return data

    # 获取所有信息，不用密码
    def transfer_info(self, yhk):
        cur = self.conn.cursor()
        sql = "SELECT * FROM `users` WHERE `yhk`='{}'".format(yhk)
        cur.execute(sql)
        data = cur.fetchall()
        return data

    def saving_money(self, yhk, money):
        cur = self.conn.cursor()
        sql = "UPDATE users SET money=((SELECT money WHERE yhk='{}') + {}) WHERE yhk='{}'".format(yhk, money, yhk)
        cur.execute(sql)

    def withdrawal(self, yhk, money):
        cur = self.conn.cursor()
        sql = "UPDATE users SET money=((SELECT money WHERE yhk='{}') - {}) WHERE yhk='{}'".format(yhk, money, yhk)
        cur.execute(sql)

    def transfer(self, yhk, yhk2, money):
        cur = self.conn.cursor()
        sql = "UPDATE users SET money=((SELECT money WHERE yhk='{}') - {}) WHERE yhk='{}'".format(yhk, money, yhk)
        sql2 = "UPDATE users SET money=((SELECT money WHERE yhk='{}') + {}) WHERE yhk='{}'".format(yhk2, money, yhk2)
        cur.execute(sql)
        cur.execute(sql2)

    def blocky(self, yhk):
        cur = self.conn.cursor()
        sql = "UPDATE users SET block='1' where yhk='{}'".format(yhk)
        cur.execute(sql)
        return "锁定成功！"

    def unblocky(self, yhk):
        cur = self.conn.cursor()
        sql = "UPDATE users SET block='0' where yhk='{}'".format(yhk)
        cur.execute(sql)
        return "解锁成功！"

