import tkFileDialog
import sys


f = tkFileDialog.askopenfiles(mode='r')
if len(f) != 2:
    print 'Please choose 2 files.\n'
    sys.exit()

fa = f[0]
fb = f[1]
s = fa.name

fvlc = open(s[:s.rfind('.')]+'_vlc'+s[s.rfind('.'):], 'w')
fsp = open(s[:s.rfind('.')]+'_splayer'+s[s.rfind('.'):], 'w')

fsp.write(fa.read())
fsp.write(fb.read())
fa.seek(0)
fb.seek(0)

line = fa.readline()
fb.readline()
while line:
    print >>fvlc, line,
    print >>fvlc, fa.readline(),
    fb.readline()
    line = fa.readline()
    while line and not line.strip().isdigit():
        if line != '\r\n':
            print >>fvlc, line,
        line = fa.readline()

    line = fb.readline()
    while line and not line.strip().isdigit():
        print >>fvlc, line,
        line = fb.readline()