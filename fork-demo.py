#coding: utf-8
import os
import time
import random
def testFork():
	testPid = os.fork()
	sleepTime = random.random()
	if testPid == 0:
		for count in range(0, 10):
			print "child %s, father %s" % (os.getpid(), os.getppid())
			time.sleep(sleepTime)
	else:
		for count in range(0, 10):
			print "self %s, big father %s" % (os.getpid(), os.getppid())
			time.sleep(sleepTime)
if __name__ == "__main__":
	testFork()
