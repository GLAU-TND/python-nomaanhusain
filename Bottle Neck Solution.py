a=int(input("Enter number of bottles"))
radius = list(map(int,input().split(" ")))
filled = []
for i in radius:
    filled.append(radius.count(i))

print(max(filled))
