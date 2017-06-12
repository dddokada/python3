import sys
print("aa")
print("bbc")
import numpy as np

# Age testing
#age = int(input("Age?"))
age =1
if age < 3:
    print("free of charge")
elif age<13:
    print("2 dollars please")
else:
    print ("3 dollars please")

#hoge = input ("aaa")
#print (hoge)

for counter in range(1):
    print(counter)

from calendar import TextCalendar

cal= TextCalendar(0)
cal_str= cal.formatmonth(2011, 4)
print(cal_str)


print(id(age))

list = [100,20,31,100,21]
print(list)

print(list[2])
tap =100,32,123,100
print(tap)
print(tap[2])

list2  = ["A","B"]
list3 =["DDD"]*2
list3.append(list2)
print (list2 +list3)
print (sys.argv[1])

# Loop test
words = ["旅行","桜", "テレビ","終了","岸辺","ラジオ"]
for word in words:
    if word == "終了":
        print("*ループを中断しました")
        break
    print(word)
