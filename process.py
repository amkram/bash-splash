import color
import os, sys

pix = open('pixels', 'r')
sys.stdout.write('echo -e ')
pre = '\033[38;5;'
pst = ('m' + u'\u2588').encode('utf-8')
ctr = 0
for line in pix:
	if('ImageMagick' in line):
		cols = int(line.split(': ')[1].split(',')[0])
		# print(cols)
	else:
		p = line.split('#')[1].split(' ')[0]
		sys.stdout.write(pre + color.rgb2short(p)[0] + pst)
		if(ctr == cols - 1):
			sys.stdout.write('\\n')
			ctr = 0
			continue
		ctr += 1
sys.stdout.write(pre + '255' + pst)

