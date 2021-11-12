import mmap
import os

fd = os.open("sensormapfile", os.O_CREAT | os.O_TRUNC | os.O_RDWR)
os.write(fd, '\x00' * mmap.PAGESIZE)
os.close(fd)

fd = os.open("safemapfile", os.O_CREAT | os.O_TRUNC | os.O_RDWR)
os.write(fd, '\x00' * mmap.PAGESIZE)
os.close(fd)

fd = os.open("gpsmapfile", os.O_CREAT | os.O_TRUNC | os.O_RDWR)
os.write(fd, '\x00' * mmap.PAGESIZE)
os.close(fd)

fd = os.open("distmapfile", os.O_CREAT | os.O_TRUNC | os.O_RDWR)
os.write(fd, '\x00' * mmap.PAGESIZE)
os.close(fd)
