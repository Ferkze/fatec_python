a = [[1,2],
     [3,4]]
b = [[1,2],
     [3,4]]
c = []

for i in range(len(a)):
    c.append([])
    for j in range(len(b)):
        c[i].append(0)
        for k in range(2):
            c[i][j] += a[i][k] * b[k][j]

print(c[0])
print(c[1])
