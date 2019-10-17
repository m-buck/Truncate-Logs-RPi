import glob
log = glob.glob('*.log')
path = "/home/pi/"
for file in log:
	filename = path + str(file)
	with open(filename, 'w'):
		pass
	print filename + " has been truncated"
