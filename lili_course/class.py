 #class创建一个类，__init__可以定义对象拥有哪些属性，前后两个下划线
class CuteCat:
    def __init__(self,cat_name,cat_age,cat_color):
        self.name = cat_name
        self.age = cat_age
        self.color = cat_color
cat1 = CuteCat("Jojo",2,"橙色")

#接下来是一些定义方法的代码
#   def speak(self):
#         print("喵"*self.age)
#   def think(self,content):
#         print(f"小猫{self.name}在思考{content}...")

class Student:
    def __init__(self,name,student_id):
        self.name = name
        self.student_id = student_id
        self.grades = {"语文":0,"数学":0,"英语":0}

    def set_grade(self,course,grade):
        if course in self.grades:
            self.grades[course] = grade
    def print_grades(self):
        print(f"学生{self.name}(学号：{self.student_id})的成绩为：")
        for course in self.grades:
             print(f"{course}:{self.grades[course]}分")
chen = Student("小陈","100618")
chen.set_grade("语文",92)
chen.set_grade("数学",94)
chen.print_grades()
#chen = Student("小陈","100618")
# zeng = Student("小曾","100622")
# print(chen.name)
# zeng.set_grade("数学",95)
# print(zeng.grades)

 