##アンケート
answer = ["イギリス","スペイン","スペイン","スペイン", "日本","ドイツ","イギリス","スペイン","スペイン","スペイン", "ドイツ"]

results = {}


for country in answer:
    if country in results:
        results[country] = results[country]+1
    else:
        results[country] =1

for i, v in results.items():
    print ("{}:{}".format(i,v))

### for xx in bbb:
lst =["日","月","火曜","水","木"]

for a in lst:
    print (a)


##　0-21 を2乗する
lst = []

for num in range(0,21,2):
    lst.append(num **2)

print(lst)

dolls =[1,5,9.5,10]
rate = 101

yens = [doll*rate for doll in dolls]

print(yens)


### 3の倍数と３がつく
num2 = [n for n in range(100) if (n%3)==0 or n//10%3==0]
print(num2)
