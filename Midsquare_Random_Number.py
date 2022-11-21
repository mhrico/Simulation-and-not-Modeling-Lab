seed = 675248
s = str(seed * seed)
while len(s) != 12:
    s = '0' + s
seed = int(s[3:9])
print(seed)