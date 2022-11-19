import matplotlib.pyplot as plt
import numpy as np

vf = None
xb = []
yb = []
inputs = []

with open('./pp_input.txt') as file:
    for line in file.readlines():
        inputs.append(line.rstrip().rsplit(','))

vf = int(inputs[0][0])
xb = [int(x) for x in inputs[1]]
yb = [int(x) for x in inputs[2]]

xf = [0]
yf = [50]

for i in range(len(xb)):
    if i > 10:
        print('Time limit exceed!')
        break

    dist = np.sqrt( (yb[i] - yf[i])**2 + (xb[i] - xf[i])**2 )
    if dist <= 10:
        print('caught at time', i)
        break

    cosx = (xb[i] - xf[i]) / dist
    sinx = (yb[i] - yf[i]) / dist

    xf.append(xf[i] + vf * cosx)
    yf.append(yf[i] + vf * sinx)

plt.plot(xb, yb, 'red')
plt.plot(xf, yf, 'green')
plt.legend(['Bomber', 'Fighter'])
plt.show()