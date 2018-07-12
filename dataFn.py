import sys
sys.path.insert(0, '/home/pi/model-factory/pubsub')
from sensor import readSensehat
from time import sleep

def createData():
	file = open("data.txt", "w")

def addData():
	file = open("data.txt", "a")

	t,h,p,a,m,g = readSensehat()
	file.write("%.2f, %.2f, %.2f, " % (t,h,p))
	file.write("%.2f, %.2f, %.2f, " % (a['x'], a['y'], a['z']))
	file.write("%.2f, %.2f, %.2f, " % (m['x'], m['y'], m['z']))
	file.write("%.2f, %.2f, %.2f" % (g['x'], g['y'], g['z']))

	file.write("\n")
	file.close()

def deleteData():
	numLines = sum(1 for line in open('data.txt'))
	if numLines > 200:
		lines = open("data.txt").readlines()
		open("data.txt", "w").writelines(lines[1:])
