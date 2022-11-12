a = []
b = []
c = []
t = 0.1
k1 = 0.008
k2 = 0.002

a.append(100)
b.append(50)
c.append(0)
print('t = 0.00\t a = {:.2f}\t b = {:.2f}\t c = {:.2f}\t'.format(a[0], b[0], c[0]))

for i in range(1,50):
    a.append(a[i-1] + (k2 * c[i-1] - k1 * a[i-1] * b[i-1]) * t)
    b.append(b[i-1] + (k2 * c[i-1] - k1 * a[i-1] * b[i-1]) * t)
    c.append(c[i-1] + (2 * k1 * a[i-1] * b[i-1] - 2 * k2 * c[i-1]) * t)
    print('t = {:.2f}\t a = {:.2f}\t b = {:.2f}\t c = {:.2f}\t'.format(i*t,a[i], b[i], c[i]))