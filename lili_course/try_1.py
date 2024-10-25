print("hello world")

print("He said \"Let\'s go!\"")
#python中单双引号都能用，如果句子里面有"，前面加一个\表示句子未结束

print("hello "+"world"+"!")
#注意句子要加空格

print("Hello!\nHi!")
#\n是换行

print("""1
2
2
3
3
4""")
#三引号可实现自动换行

#使用变量,变量命名不能有空格，不能用数字开头，用下划线
greet="您好，吃了么，"
greet_chinese = greet
greet_english = "Yo what's up,"
greet = greet_english
print(greet +"张三")
print(greet +"李四")
print(greet +"席")

#math，print不要加引号，加引号是字符串
import math
a = -1
b = -2
c = 3
r1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
r2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
print(r1)
print(r2)

#ctrl+/  能将多行代码注释掉

#整数int 浮点数float
#bool类型，0和不输入任何内容的布尔类型为false
#None

#len()算长度
s = "Hello world!"
print(len(s))

#通过索引获取单个字符
print(s[0],s[11])

#bool类型
b1 = True
b2 = False

#空值类型
n = None

#type函数
print(type(s))
print(type(b1))
print(type(n))
print(type(1.5))

#input返回字符串
#整数用int
#float字符串
# user_weight = float(input("请输入您的体重(单位:kg):"))
# user_height = float(input("请输入您的身高(单位：m):"))
# user_BMI = user_weight / (user_height) ** 2
# print("您的BMI值为： " + str(user_BMI))

#if else elif
mood_index = int(input("对象今天的心情指数是："))
if mood_index >= 60:
    print("恭喜")
else:
    print("还是别打了")

#not优先级最高