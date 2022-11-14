import matplotlib.pyplot as plt
import numpy as np

vf = 20
xb = [80, 90, 99, 108, 116, 125, 133, 141, 151, 160, 169, 179, 180]
yb = [0, -2, -5, -9, -15, -18, -23, -29, -28, -25, -21, -20, -17]

xf = [0]
yf = [50]
caught = False

for i in range(len(xb)):
    dist = np.sqrt((yb[i]-yf[i])**2 + (xb[i]-xf[i])**2)
    if dist < 10:
        caught = True
        break
    cos = (xb[i]-xf[i])/dist
    sin = (yb[i]-yf[i])/dist
    xf.append(xf[i] + vf * cos)
    yf.append(yf[i] + vf * sin)

if caught:
    print('Caught')
else:
    print('Not Caught')
    
plt.plot(xb, yb)
plt.plot(xf, yf)
plt.show()