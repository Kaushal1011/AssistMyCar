import mmap
import os

filename = 'mapfile'

## create and initialize file with code like this
#fd = os.open(filename, os.O_CREAT | os.O_TRUNC | os.O_RDWR)
#os.write(fd, '\x00' * mmap.PAGESIZE)

fd = os.open(filename, os.O_RDWR)
buf = mmap.mmap(fd, 0, mmap.MAP_SHARED, mmap.PROT_WRITE)

i = 0
try:
    while 1:
        print i
        buf.seek(0)
        ## use pickle to store complicated data
        buf.write((str(i)+"\n").encode())
        #buf.flush()
        raw_input('ENTER')
except:
    buf.seek(0)
        ## use pickle to store complicated data
    buf.write(("1"+"\n").encode())
    #buf.flush()
    raw_input('ENTER')
    buf.close()
    os.close(fd)
