a = [[1,2,3], [4,5,6]]
dic = {}
dic[0] = a[0]
a[0] = []
print(a)
print(dic)
a[0] = dic.get(0)
print(a)