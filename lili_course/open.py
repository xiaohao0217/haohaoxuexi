#"r"只读，"w"只写模式
#encoding=""
#read方法
# f = open("./data.txt","r",encoding="utf-8")
# print(f.read()) 会读全部的文件内容，并打印
# print(f.read()) 会读空字符串，并打印，因为会自动保存到上一次读的位置
# print(f.read(10))会读第1-10个字节的文件内容
# print(f.readline())读一行
# print(f.readlines())
# f.close()

#以下是示例

# with open("./data.txt") as f:
#     print(f.read())
# f = open("./letter_1 from Hunk.txt","r",encoding = "utf-8")#不写也是默认"r"
# content = f.read()
# print(content)
# f.close()

# #方法2
# with open("./letter_1 from Hunk.txt","r",encoding = "utf-8") as f:
#     content = f.read()
#     print(content)

with open("./letter_1 from Hunk.txt","r",encoding = "utf-8") as f:
    print(f.readline())
    print(f.readlines())#返回的是列表
    lines = f.readlines()
    for line in lines:
        print(line)
         
with open("./poem_1.txt","w",encoding = "utf-8") as f:
    f.write("刘席大笨蛋\n")
    f.write("刘席死夹子\n")
    f.write("刘席跟我分手之后再也找不到对象\n")

with open("./poem_1.txt","a",encoding = "utf-8") as f:
    f.write("刘席再跟我吵架以后就讨不到老婆\n嘿嘿\n")