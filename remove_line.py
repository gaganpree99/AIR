import os
from mmap import mmap
def line(filename, lineno):
    f=os.open(filename, os.O_RDWR)
    m=mmap(f,0)
    p=0
    for i in range(lineno-1):
        p=m.find('\n',p)+1
    q=m.find('\n',p)
    m[p:q] = ' '*(q-p)
    os.close(f)