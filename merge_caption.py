import sys

'''
dir = '/Users/sliva/Movies/'
fen = "The.Wolf.of.Wall.Street.2013.DVDScr.x264-HaM.eng.srt"
fch = "The.Wolf.of.Wall.Street.2013.DVDScr.x264-HaM.chs.srt"
fout = "The.Wolf.of.Wall.Street.2013.DVDScr.x264-HaM.ench.srt"
fen = open(dir + fen)
fch = open(dir + fch)
fout = open(dir + fout, 'w')
'''

if len(sys.argv) < 4:
    print 'usage: python '+sys.argv[0]+' dir caption1 caption2\n'+\
          'Example: python '+sys.argv[0]+' /Users/sliva/Movies/ The.Wolf.of.Wall.Street.2013.DVDScr.x264-HaM.eng.srt The.Wolf.of.Wall.Street.2013.DVDScr.x264-HaM.chs.srt'
    sys.exit()

d = sys.argv[1]
s = sys.argv[2]
fen = open(d+s)
fch = open(d+sys.argv[3])
fout = open(d+s[:s.rfind('.')]+'_new'+s[s.rfind('.'):], 'w')
s = fen.readline()
fch.readline()
while s:
    print >>fout, s,
    print >>fout, fen.readline(),
    fch.readline()
    s = fen.readline()
    while s and not s.strip().isdigit():
        if s != '\r\n':
            print >>fout, s,
        s = fen.readline()

    s = fch.readline()
    while s and not s.strip().isdigit():
        print >>fout, s,
        s = fch.readline()



