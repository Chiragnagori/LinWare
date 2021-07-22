#!/usr/bin/python3
import cgi
import subprocess

print("content-type: text/plain")
print()

mydata = cgi.FieldStorage()
#myos = mydata.getvalue("osname")
#myimage = mydata.getvalue("imagename")
cmd = mydata.getvalue("cmdname")
#print(myx)

#comd="sudo docker run -dit --name {} mycentos:v1".format(myos)
comd="sudo docker start mycentos"
runcmd="sudo docker exec mycentos {} ".format(cmd)

outlaunch = subprocess.getstatusoutput(comd)
output = subprocess.getstatusoutput(runcmd)
status = output[0]
myout = output[1]
print(myout)

