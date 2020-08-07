import datetime
import os

x = datetime.datetime.now()
print "Hello World - Python!!!!"
print "Current date/time: "
print x

if "USERNAME" in os.environ:
    print os.getenv("USERNAME")
else:
    print "no user name"

