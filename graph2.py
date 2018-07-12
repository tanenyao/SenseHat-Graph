#!/usr/bin/python3

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from matplotlib.widgets import Button

style.use('fivethirtyeight')

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
plt.subplots_adjust(bottom=0.2, right=0.8)

titles = {0: "Temperature", 1: "Humidity", 2: "Pressure", 3: "Accelerometer", 4: "Magnetometer", 5: "Gyroscope"}
ylabels = {0: "Celcius", 1: "rH", 2: "Millibars", 3: " ", 4: " ", 5: " "}
th = {0: 30, 1: 59, 2: 1008, 3: 1.1, 4: 1, 5: 0.5}

state = 0
bState = 0
linesOfData = 200

def yList(state):
	list = []
	# line of code to handle special 3-graph cases
	l1, l2, l3 = [],[],[]

	data = open('data.txt', 'r').read()
	lines = data.split('\n')

	if state < 3:
		for line in lines:
			if len(line) > 1:
				line = line.split(',')
				list.append(float(line[state]))

	# block of code to handle 3-graph cases
	elif state == 3:
		for line in lines:
			if len(line) > 1:
				line = line.split(',')
				l1.append(float(line[3]))
				l2.append(float(line[4]))
				l3.append(float(line[5]))
		list.append(l1)
		list.append(l2)
		list.append(l3)

	elif state == 4:
		for line in lines:
			if len(line) > 1:
				line = line.split(',')
				l1.append(float(line[6]))
				l2.append(float(line[7]))
				l3.append(float(line[8]))
		list.append(l1)
		list.append(l2)
		list.append(l3)

	elif state == 5:
		for line in lines:
			if len(line) > 1:
				line = line.split(',')
				l1.append(float(line[9]))
				l2.append(float(line[10]))
				l3.append(float(line[11]))
		list.append(l1)
		list.append(l2)
		list.append(l3)
	# end of code block

	return list

def xList():
	list = []
	for i in range(linesOfData):
		list.append(i)

	return list

def check(xlist, ylist):
	# block of code to handle special 3-graph cases
	if len(ylist) != 0 and isinstance(ylist[0], list):
		count = 0
		for i in range(len(ylist)):
			if len(ylist[i]) != 0 and len(xlist) == len(ylist[i]):
				count += 1

		if count == len(ylist):
			return True
	# end of code block

	elif len(ylist) != 0 and len(xlist) == len(ylist):
		return True

	else:
		return False

def displayAlert(list, state):
	if len(list) == 3:
		for i in list:
			for j in i:
				if float(j) > th[state]:
					ax.text(0.9, 1, 'ALERT: Threshold Exceeded', horizontalalignment='center', verticalalignment='center', transform=ax.transAxes, color='red')

	else:
		for i in list:
			if float(i) > th[state]:
				ax.text(0.9, 1, 'ALERT: Threshold Exceeded', horizontalalignment='center', verticalalignment='center', transform=ax.transAxes, color='red')

def animate(i):
	ylist = yList(state)
	xlist = xList()

	if state < 3:
		if check(xlist, ylist) == True:
			ax.clear()
			ax.plot(xlist, ylist)
			ax.set_title(titles[state])
			ax.set_ylabel(ylabels[state])
		else:
			pass

		# threshold graph
		if bState == 1:
			b6.label.set_text('Threshold On')
			ax.plot(xlist, [[th[state]] for _ in range(len(xlist))], color = "red")
			displayAlert(ylist, state)
		else:
			b6.label.set_text('Threshold Off')

	# code block to handle 3-graph cases
	elif state >= 3:
		if check(xlist, ylist) == True:
			ax.clear()
			ax.plot(xlist, ylist[0], label="x-axis", color = "blue")
			ax.plot(xlist, ylist[1], label="y-axis", color = "orange")
			ax.plot(xlist, ylist[2], label="z-axis", color = "green")
			ax.set_title(titles[state])
			ax.set_ylabel(ylabels[state])
		else:
			pass

		# threshold graph
		if bState == 1:
			b6.label.set_text('Threshold On')
			ax.plot(xlist, [[th[state]] for _ in range(len(xlist))], color = "red")
			displayAlert(ylist, state)
		else:
			b6.label.set_text('Threshold Off')

		ax.legend()
		leg = ax.legend(loc=7, ncol=1, prop = {'size': 15})
		leg.get_frame().set_alpha(0.2)
	# end of code block

class Buttons():
	def zero(self, event):
		global state
		state = 0

	def one(self, event):
		global state
		state = 1

	def two(self, event):
		global state
		state = 2

	def three(self, event):
		global state
		state = 3

	def four(self, event):
		global state
		state = 4

	def five(self, event):
		global state
		state = 5

	def threshold(self, event):
		global bState
		bState += 1

		if bState % 2 != 0:
			bState = 1

		else:
			bState = 0

try:
	b = Buttons()
	axb0 = plt.axes([0.17, 0.05, 0.11, 0.075])
	b0 = Button(axb0, 'Temperature')
	b0.on_clicked(b.zero)

	axb1 = plt.axes([0.28, 0.05, 0.11, 0.075])
	b1 = Button(axb1, 'Humidity')
	b1.on_clicked(b.one)

	axb2 = plt.axes([0.39, 0.05, 0.11, 0.075])
	b2 = Button(axb2, 'Pressure')
	b2.on_clicked(b.two)

	axb3 = plt.axes([0.5, 0.05, 0.11, 0.075])
	b3 = Button(axb3, 'Accelerometer')
	b3.on_clicked(b.three)

	axb4 = plt.axes([0.61, 0.05, 0.11, 0.075])
	b4 = Button(axb4, 'Magnetometer')
	b4.on_clicked(b.four)

	axb5 = plt.axes([0.72, 0.05, 0.11, 0.075])
	b5 = Button(axb5, 'Gyroscope')
	b5.on_clicked(b.five)

	axb6 = plt.axes([0.85, 0.5, 0.11, 0.075])
	b6 = Button(axb6, 'Threshold Off')
	b6.on_clicked(b.threshold)

	ani = animation.FuncAnimation(fig, animate, interval = 100)
	plt.show()

except AttributeError:
	print ("No item with that code")

except IndexError:
	print("List out of range")
