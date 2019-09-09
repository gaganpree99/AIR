#!/usr/bin/python

i=0

h=open('stt.txt','r')
s= h.read()

for line in s:
	i=i+1
	if(line=="is"):
		print i

print s

d=open("new.txt","a")
d.write(s)



h.close()
