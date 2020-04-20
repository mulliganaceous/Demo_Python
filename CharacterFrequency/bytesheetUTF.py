from time import time
OMG = "Tracelog.\U0001F602"
f = open(OMG, "rb")
b = f.read(2)
k = 0

utf16 = [0]*0x10000
utf8 = [0]*0x100

ms = time()
while len(b) == 2:
    upper = b[0]
    lower = b[1]
    if k > 0 and k % (1024*1024) == 0:
        print("{0:12d} B: {1:6d}".format(k, int(1000*(time()-ms))))
        ms = time()
        
    utf8[upper] = utf8[upper] + 1
    utf8[lower] = utf8[lower] + 1
    utf16[256*upper + lower] = utf16[256*upper + lower] + 1

    k = k + 2
    b = f.read(2)
    
if b:
    utf8[b[0]] = utf8[b[0]] + 1
    utf8[0] = utf8[0] + 1
    utf16[256*b[0]] = utf16[256*b[0]] + 1
    
    k = k + 1

print("Characters = " + str(k))
for e in range(0, len(utf16)):
    print("{0:6X};\t{1:d}".format(e, utf16[e]))
for e in range(0, len(utf8)):
    print("{0:2X};\t{1:d}".format(e, utf8[e]))
