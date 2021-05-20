# -*- coding = utf-8 -*-
# @Time :2021/5/19 9:41
# @Author: Hanayuzu
# @File :GUI2

from 银行管理系统2 import *
from tkinter import *
from tkinter.messagebox import showinfo, showwarning, showerror


# 注册页面控件
class CreateFrame(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.name = StringVar()
        self.call = StringVar()
        self.idcard = StringVar()
        self.pwd = StringVar()
        self.createPage()

    def createPage(self):
        Label(self, text='请填写如下个人信息进行注册：').grid(row=0, stick=W, pady=10)
        Label(self, font=('楷体', 30), text='姓名:').grid(row=1, stick=W, pady=10)
        Entry(self, textvariable=self.name, width=30, font=('楷体', 40)).grid(row=1, column=1, stick=E)
        Label(self, font=('楷体', 30), text='手机号:').grid(row=2, stick=W, pady=10)
        Entry(self, textvariable=self.call, width=30, font=('楷体', 40)).grid(row=2, column=1, stick=E)
        Label(self, font=('楷体', 30), text='身份证号:').grid(row=3, stick=W, pady=10)
        Entry(self, textvariable=self.idcard, width=30, font=('楷体', 40)).grid(row=3, column=1, stick=E)
        Label(self, font=('楷体', 30), text='密码:').grid(row=4, stick=W, pady=10)
        Entry(self, textvariable=self.pwd, width=30, font=('楷体', 40)).grid(row=4, column=1, stick=E)
        Button(self, width=15, height=2, font=('楷体', 40), text='注册!', command=self.run).grid(row=6, column=1, stick=E, pady=10)
        Button(self, width=15, height=2, font=('楷体', 40), text='返回!', command=self.back).grid(row=6, column=1, stick=W, pady=10)


    def run(self):
        name = self.name.get()
        call = self.call.get()
        idcard = self.idcard.get()
        pwd = self.pwd.get()
        yhk = time.time()
        print(name)
        user = Open_Account(name, yhk, pwd, call, '0', idcard, '0')
        user = user.Create_Account()
        print(user)
        showinfo(title='账号注册成功', message=user)

    # 返回登录页面
    def back(self):
        self.destroy()
        LoginPage(root)


# 信息页面控件
class CreateFrame2(Frame):
    def __init__(self, master=None, yhk=0, password=0):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.name = StringVar()  # 姓名
        self.call = StringVar()  # 电话
        self.idcard = StringVar()  # 身份证
        self.pwd = StringVar()  # 密码
        self.other = StringVar()  # 被转账卡号
        self.money = StringVar()  # 余额
        self.cunkaun = StringVar()  # 存款金额
        self.qukuan = StringVar()  # 取款金额
        self.zhuanzhang = StringVar()  # 转账金额
        self.yhk = yhk
        self.password = password
        self.createPage()

    def createPage(self):
        Label(self, text='尊敬的储户您好').grid(row=0, stick=W, pady=10)
        Label(self, font=('楷体', 30), text='姓名：').grid(row=1, stick=W, pady=10)
        Entry(self, textvariable=self.name, width=30, font=('楷体', 40)).grid(row=1, column=1, stick=E)
        Label(self, font=('楷体', 30), text='卡号：').grid(row=2, stick=W, pady=10)
        Entry(self, textvariable=self.idcard, width=30, font=('楷体', 40)).grid(row=2, column=1, stick=E)
        Label(self, font=('楷体', 30), text='余额：').grid(row=3, stick=W, pady=10)
        Entry(self, textvariable=self.money, width=30, font=('楷体', 40)).grid(row=3, column=1, stick=E)
        Label(self, font=('楷体', 30), text='存款：').grid(row=4, stick=W, pady=10)
        Entry(self, textvariable=self.cunkaun, width=30, font=('楷体', 40)).grid(row=4, column=1, stick=E)
        Label(self, font=('楷体', 30), text='取款：').grid(row=5, stick=W, pady=10)
        Entry(self, textvariable=self.qukuan, width=30, font=('楷体', 40)).grid(row=5, column=1, stick=E)
        Label(self, font=('楷体', 30), text='转账：').grid(row=6, stick=W, pady=10)
        Entry(self, textvariable=self.other, width=30, font=('楷体', 40)).grid(row=6, column=1, stick=E)
        Label(self, font=('楷体', 30), text='金额：').grid(row=7, stick=E, pady=10)
        Entry(self, textvariable=self.zhuanzhang, width=30, font=('楷体', 40)).grid(row=7, column=1, stick=E)
        Button(self, width=10, height=1, font=('楷体', 40), text='更新信息!', command=self.run).grid(row=8, column=1, stick=E, pady=10)
        Button(self, width=10, height=1, font=('楷体', 40), text='存款！', command=self.save).grid(row=9, column=1, stick=E, pady=10)
        Button(self, width=10, height=1, font=('楷体', 40), text='转账！', command=self.transferring_money).grid(row=8, column=1, stick=W, pady=10)
        Button(self, width=10, height=1, font=('楷体', 40), text='取款！', command=self.unsave).grid(row=9, column=1, stick=W, pady=10)

    # 更新信息
    def run(self):
        print("按了一下更新信息！")
        print(self.yhk, self.password)
        user = Get_info()
        info = user.get_info(self.yhk, self.password)[0]
        self.name.set(info[1])
        self.idcard.set(self.yhk)
        self.money.set(info[5])
        print(info)

    # 存款
    def save(self):
        print("按了一下存款！")
        money = self.cunkaun.get()
        print(money)
        user = Get_info()
        user.saving_money(self.yhk, money)

    # 取款
    def unsave(self):
        print("按了一下取款！")
        money = self.qukuan.get()
        print(money)
        user = Get_info()
        user.withdrawal(self.yhk, money)

    # 转账
    def transferring_money(self):
        print("按了一下转账！")
        money = self.zhuanzhang.get()
        yhk2 = self.other.get()
        user = Get_info()
        user.transfer(self.yhk, yhk2, money)



# 锁定与解锁页面控件
class QueryFrame(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.itemName = StringVar()
        self.yhk = StringVar()
        self.password = StringVar()
        self.createPage()

    def createPage(self):
        Label(self, text='转账界面')
        Label(self, font=('楷体', 30), text='卡号：').grid(row=1, stick=W, pady=10)
        Entry(self, textvariable=self.yhk, width=30, font=('楷体', 40)).grid(row=1, column=1, stick=E)
        Label(self, font=('楷体', 30), text='密码：').grid(row=2, stick=W, pady=10)
        Entry(self, textvariable=self.password, width=30, font=('楷体', 40)).grid(row=2, column=1, stick=E)
        Button(self, width=10, height=1, font=('楷体', 40), text='查询信息!', command=self.search).grid(row=3, column=1, stick=E, pady=10)
        Button(self, width=10, height=1, font=('楷体', 40), text='解锁卡卡!', command=self.unblocking).grid(row=3, column=1, stick=W, pady=10)
        Button(self, width=10, height=1, font=('楷体', 40), text='锁定卡卡!', command=self.blocking).grid(row=4, column=1, stick=W, pady=10)
        Button(self, width=10, height=1, font=('楷体', 40), text='返回主页！', command=self.back).grid(row=4, column=1, stick=E, pady=10)

    def search(self):
        user = Get_info()
        a = self.yhk.get()
        user = user.transfer_info(a)
        print(user[0])
        if user[0][7] == '0':
            showinfo(title="卡号为：" + user[0][2], message="您的账户正常喵！")
        else:
            showinfo(title="卡号为：" + user[0][2], message="您的账户被锁定辣！")

    def blocking(self):
        user = Get_info()
        yhk = self.yhk.get()
        pwd = self.password.get()
        info = user.get_info(yhk, pwd)
        if info:
            showinfo("卡号为：" + info[0][2], message="账号已成功解锁喵")
            user.blocky(yhk)

    def unblocking(self):
        user = Get_info()
        yhk = self.yhk.get()
        pwd = self.password.get()
        info = user.get_info(yhk, pwd)
        print(yhk)
        if info:
            showinfo("卡号为：" + info[0][2], message="账号已成功解锁喵")
            user.unblocky(yhk)

    def back(self):
        self.destroy()
        LoginPage(root)

# 进入注册页的
class MainPage(object):

    def __init__(self, master=None):
        self.root = master
        self.root.geometry('%dx%d' % (1100, 600))  # 设置窗口大小
        self.createPage()

    def createPage(self):
        self.info = CreateFrame(self.root)
        self.block = QueryFrame(self.root)
        self.info.pack()
        menubar = Menu(self.root)
        menubar.add_command(label='账号注册', command=self.inputData)
        menubar.add_command(label='解锁与锁定', command=self.queryData)
        self.root['menu'] = menubar  # 设置菜单栏

    def queryData(self):
        self.info.pack_forget()
        self.block.pack()

    def inputData(self):
        self.info.pack()
        self.block.pack_forget()

# 进入信息页的
class Info_Page(object):

    def __init__(self, master=None, yhk='0', password='0'):
        self.root = master
        self.root.geometry('%dx%d' % (1200, 800))  # 设置窗口大小
        self.yhk = yhk
        self.password = password
        self.createPage()

    def createPage(self):

        print('info')
        self.info = CreateFrame2(self.root, self.yhk, self.password)
        self.queryPage = QueryFrame(self.root)
        self.info.pack()
        menubar = Menu(self.root)
        menubar.add_command(label='账号信息', command=self.inputData)
        menubar.add_command(label='锁定与解锁', command=self.queryData)
        self.root['menu'] = menubar  # 设置菜单栏

    def queryData(self):
        self.info.pack_forget()
        self.queryPage.pack()


    def inputData(self):
        self.info.pack()
        self.queryPage.pack_forget()


class LoginPage(object):


    def __init__(self, master=None):
        self.root = master
        self.root.geometry('%dx%d' % (300, 180))  # 设置窗口大小
        self.username = StringVar()
        self.password = StringVar()
        self.createPage()

    def createPage(self):
        self.page = Frame(self.root)
        self.page.pack()
        Label(self.page).grid(row=0, stick=W)
        Label(self.page, text='账户: ').grid(row=1, stick=W, pady=10)
        Entry(self.page, textvariable=self.username).grid(row=1, column=1, stick=E)
        Label(self.page, text='密码: ').grid(row=2, stick=W, pady=10)
        Entry(self.page, textvariable=self.password, show='*').grid(row=2, column=1, stick=E)
        Button(self.page, text='登陆', command=self.loginCheck).grid(row=3, stick=W, pady=10)
        Button(self.page, text='注册', command=self.register).grid(row=3, stick=W, pady=10, column=1)
        Button(self.page, text='退出', command=self.page.quit).grid(row=3, column=1, stick=E)

    # 注册按钮，跳转到注册页面
    def register(self):
        self.page.destroy()
        MainPage(self.root)

    # 登录按钮，判断后跳转到信息页面
    def loginCheck(self):
        user = Get_info()
        yhk = self.username.get()
        password = self.password.get()
        rel_pass = user.get_info(yhk, password)
        if not rel_pass:
            showinfo(title='错误', message='账号或密码错误！')
        else:
            if rel_pass[0][7] == '1':
                showinfo(title='_(:з」∠)_', message='这个账号被锁定了呜~')
            else:
                showinfo(title='正确', message='欢迎欢迎喵！')
                self.page.destroy()

                Info_Page(self.root, yhk, password)



