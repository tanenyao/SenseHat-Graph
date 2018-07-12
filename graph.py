#!/usr/bin/python3

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from matplotlib.widgets import Button

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(2,3,1)
ax2 = fig.add_subplot(2,3,2)
ax3 = fig.add_subplot(2,3,3)
ax4 = fig.add_subplot(2,3,4)
ax5 = fig.add_subplot(2,3,5)
ax6 = fig.add_subplot(2,3,6)


def animate(i):
	data = open('data.txt', 'r').read()
	lines = data.split('\n')

	xs,ts,hs,ps,s1s,s2s,s3s,m1s,m2s,m3s,g1s,g2s,g3s = [],[],[],[],[],[],[],[],[],[],[],[],[]
	j = 1

	if sum(1 for line in open('data.txt')) == 200:
		for line in lines:
			if len(line.split(',')) == 12:
				t,h,p,s1,s2,s3,m1,m2,m3,g1,g2,g3 = line.split(',')
				xs.append(j)
				ts.append(float(t))
				hs.append(float(h))
				ps.append(float(p))
				s1s.append(float(s1))
				s2s.append(float(s2))
				s3s.append(float(s3))
				m1s.append(float(m1))
				m2s.append(float(m2))
				m3s.append(float(m3))
				g1s.append(float(g1))
				g2s.append(float(g2))
				g3s.append(float(g3))
				j+=1

		ax1.clear()
		ax2.clear()
		ax3.clear()
		ax4.clear()
		ax5.clear()
		ax6.clear()
		ax1.plot(xs,ts)
		ax2.plot(xs, hs)
		ax3.plot(xs, ps)
		ax4.plot(xs, s1s, label = 'x-axis')
		ax4.plot(xs, s2s, label = 'y-axis')
		ax4.plot(xs, s3s, label = 'z-axis')
		ax5.plot(xs, m1s, label = 'x-axis')
		ax5.plot(xs, m2s, label = 'y-axis')
		ax5.plot(xs, m3s, label = 'z-axis')
		ax6.plot(xs, g1s, label = 'x-axis')
		ax6.plot(xs, g2s, label = 'y-axis')
		ax6.plot(xs, g3s, label = 'z-axis')
		ax1.set_title("Temperature")
		ax2.set_title("Humidity")
		ax3.set_title("Pressure")
		ax4.set_title("Accelerometer")
		ax5.set_title("Magnetometer")
		ax6.set_title("Gyroscope")
		ax1.set_ylabel("C")
		ax2.set_ylabel("rH")
		ax3.set_ylabel("Millibars")
		ax4.legend()
		leg = ax4.legend(loc=7, ncol = 1, prop = {'size':10})
		leg.get_frame().set_alpha(0.2)
		ax5.legend()
		leg = ax5.legend(loc=7, ncol = 1, prop = {'size':10})
		leg.get_frame().set_alpha(0.2)
		ax6.legend()
		leg = ax6.legend(loc=7, ncol = 1, prop = {'size':10})
		leg.get_frame().set_alpha(0.2)

	else:
		pass

try:
	ani = animation.FuncAnimation(fig, animate, interval = 200)
	plt.show()

except AttributeError:
	print ("No item with that code")

