#列表list是可变的
num_list = [1,13,-7,2,96]
print(max(num_list))    #打印列表里的最大值
print(min(num_list))    #打印列表里的最小值
print(sorted(num_list)) #打印排列好的列表

shopping_list = []
shopping_list.append("键盘")
shopping_list.append("键帽")
shopping_list.remove("键帽")
shopping_list.append("音响")
shopping_list.append("电竞椅")
shopping_list[1] = "硬盘"

print(shopping_list)
print(len(shopping_list))
print(shopping_list[0])

price = [799,1024,200,800]
max_price = max(price)
min_price = min(price)
sorted_price = sorted(price)
print(max_price)
print(min_price)
print(sorted_price)

#元组tuple()不可变
#字典{}，键值对,用:连接
contacts = {"小明":"110",
            "小花":"112",
            "美女A":"119"}
contacts["美女A"] = "168"
del contacts["小明"]    #删除键值对
print(contacts)

#结合input、词典、if判断，做一个查询流行语句含义的电子词典程序 
slang_ditc = {"book":"hero","YYDS":"guy"}
slang_ditc["rose"] = "flower" 
slang_ditc["job"] = "my dream"
slang_ditc["study"] = "easy"
query = input("请输入您想查询的单词：")
if query in slang_ditc:
    print("您查询的"+query+"含义如下")
    print(slang_ditc[query])
else:
    print("查不到。")
    print("当前的单词数为："+str(len(slang_ditc))+"条。")