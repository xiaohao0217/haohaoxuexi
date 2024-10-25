# 类继承练习：人力系统
# - 员工分为两类：全职员工 FullTimeEmployee、兼职员工 PartTimeEmployee。
# - 全职和兼职都有"姓名 name"、"工号 id"属性，
#   都具备"打印信息 print_info"（打印姓名、工号）方法。
# - 全职有"月薪 monthly_salary"属性，
#   兼职有"日薪 daily_salary"属性、"每月工作天数 work_days"的属性。
# - 全职和兼职都有"计算月薪 calculate_monthly_pay"的方法，但具体计算过程不一样。

class Employee:#定义员工这个父类
    def __init__(self, name, id):#self是指本身
        self.name = name
        self.id = id

    def print_info(self):#定义打印信息的方法
        print(f"员工名字：{self.name}，工号：{self.id}")

class FullTimeEmployee(Employee):#全职员工继承自员工类
    def __init__(self, name, id, monthly_salary):
        super().__init__(name, id)#super()表示父类
        self.monthly_salary = monthly_salary

    def calculate_monthly_pay(self):
        return self.monthly_salary

class PartTimeEmployee(Employee):
    def __init__(self, name, id, daily_salary, work_days):
        super().__init__(name, id)
        self.daily_salary = daily_salary
        self.work_days = work_days

    def calculate_monthly_pay(self):
        return self.daily_salary * self.work_days

zhangsan = FullTimeEmployee("张三", "1001", 6000)
lisi = PartTimeEmployee("李四", "1002", 230, 15)
zhangsan.print_info()
lisi.print_info()
print(zhangsan.calculate_monthly_pay())
print(lisi.calculate_monthly_pay())

    