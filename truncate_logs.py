import glob
path = "/home/pi/"
ext = glob.glob('*.log')
for file in ext:
	filename = path + str(file)
	with open(filename, 'w'):
		pass
	print filename + " has been truncated"
