g = [12,13,43,-12,33,54,12]
n = len(g)
#7
target = 54
visited = 0
for i in range(n):
    if g[i] == target:
        print("found")
        visited = 1
        break
if visited == 0:
     print("not found")
