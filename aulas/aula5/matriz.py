m1 = [1, 2, 3, 4, 5]
m2 = ['a', 'b', 'c']
m3 = []

for i in range(len(m1)):
  if (len(m1) >= 1+i):
    m3.append(m1[i])
  if (len(m2) >= 1+i):
    m3.append(m2[i])

print(m3)