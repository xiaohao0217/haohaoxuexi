#定义函数
def calculate_BMI(weight,height):
    BMI = weight/height ** 2
    if BMI <= 18.5:
        category = "偏瘦"
    elif BMI <= 25:
        category = "正常"
    elif BMI <= 30:
        category = "偏胖"
    else:
        category = "肥胖"
    print(f"BMI为分类:{category}")
    #利用f字符串，可以直接把字符串和变量一起打印，不用手动加上str
    return BMI
result = calculate_BMI(70,1.8 )
print(result)