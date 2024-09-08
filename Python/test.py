a = "epic_W + epic_Winning = c"
print(a.replace("epic_W", "epic_w"))
lst = a.split(" ")
print(lst)
for i in lst:
    if i == "epic_W":
        lst[lst.index(i)] = "epic_w"
print(lst)