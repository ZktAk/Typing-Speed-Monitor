
import pickle
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline, BSpline
import os

wpm_file = open("seasions/" + os.environ['filename'], "rb")
wpm = pickle.load(wpm_file)
wpm_file.close()

#create data
x = []
y = []

for n in range(len(wpm)):
    x.append(n+1)
    y.append(wpm[n])
x = np.array(x)
y = np.array(y)


#define x as 200 equally spaced values between the min and max of original x
xnew = np.linspace(x.min(), x.max(), 20*len(x))

#define spline
spl = make_interp_spline(x, y, k=5)
y_smooth = spl(xnew)

#create smooth line chart
fig = plt.figure(figsize=(50,6))
ax = plt.gca()
ax.set_facecolor('#363737')
fig.canvas.manager.set_window_title(os.environ['filename'])

max_index = y.argmax()

plt.plot(xnew, y_smooth, color='#ff9900')

plt.axhline(y[max_index])  #horizontal line
plt.annotate("Best: {}".format(round(y[max_index])), [1, y[max_index]-6], color='#ff9900')

plt.show()
