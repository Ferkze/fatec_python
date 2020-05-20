l1 = [1, 2, 3]
l2 = ['a','b','c','d','e']
l3 = []

for i in range(max(len(l1), len(l2))):
  if (len(l1) >= 1+i):
    l3.append(l1[i])
  if (len(l2) >= 1+i):
    l3.append(l2[i])

print(l3)
