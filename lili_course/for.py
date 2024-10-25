total = 0
for i in range(1,101):
    total = total + i
print(total)

list1 = ["你","好","吗","兄","弟"]
for char in list1:
    print(char)

for i in range(len(list1)):
    print(list1[i])

i = 1
while i < len(list1):
    print(list1[i])
    i = i+1

print("求平均值")
total = 0
count = 0
user_input = input("请输入数字（完成数字输入后，请输入q终止程序）：")
while user_input != "q":
    num = float(user_input)
    total += num
    count += 1
    user_input = input("请输入数字（完成数字输入后，请输入q终止程序）：")
if count == 0:
    result =0
else:
    result = total / count
print("您输入的数字平均值为" + str(result))
