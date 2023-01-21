f = open("/content/27-B_demo.txt", 'r')
n = f.readline()
max_l = []
min_l = []
itog = []
sum = 0
for i in f:
    a, b = i.split()
    a = int(a)
    b = int(b)
    minc = min(a, b)
    maxc = max(a, b)
    max_l.append(maxc)
    min_l.append(minc)

for j in range(int(n)):
    raznica = max_l[j] - min_l[j]
    itog.append(raznica)

itog.sort()

for g in itog:
    if itog[g] % 3 != 0:
        min_must_have_raznica = itog[g]
        break

for i in max_l:
    sum += i
print(sum - min_must_have_raznica)

f.close()