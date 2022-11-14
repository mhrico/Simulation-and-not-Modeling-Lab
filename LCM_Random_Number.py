seed = 0
a = 1
c = 3
m = 10

x = [seed]
r = [] # Sir only asked for X in his doc, so R may not be necessary

for i in range(0, 13):
    x.append((a * x[i] + c) % m)
    r.append(x[i] / m)

print('\t x\t r')
for i in range(1, 13):
    print(i, '\t', x[i], '\t', r[i])