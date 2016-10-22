a = [1,2,3]

for i in a:
    print(i)

list = [{"name":"가"}, {"name":"나"},{"name":"다"}]
for i in list:
    print(list1[i]["name"])

list2 = [{"name":"가", "score":40},{"name":"황진희", "score":60}]
for i in list2:
    print(list2[i]["name"] + "의 점수는" + str(list2[i]["score"]))


index = 1
list3 = [{"name":"가", "score":40},{"name":황진희", "score":60}]
for i in list3:
    print(str(index) + "번째: " + i["name"] + "의 점수는 " +str(i["score"]))
    index = index + 1


 index = 1
for i in list3:
    if i ["score"] > 50:
        print(str(index) + "번째: " + i ["name"] + "합격")
    else:
        print(str(index) + "번째: " + i ["name"] + "불합격")
        index = index + 1

