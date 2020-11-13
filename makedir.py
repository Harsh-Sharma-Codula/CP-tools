#Author-Harsh Sharma

#This File Can be used to make directories during contests
#use:
#python3 ready.py <Contest-name> <problems-name(separated with spaces)>
#example
#python3 ready.py cf656 A B C D

import sys,os
probsnumb=len(sys.argv)
contest=sys.argv[1]
probs=[]
for x in range(2,probsnumb):
	probs.append(sys.argv[x])
for P in probs:
	os.system("mkdir C:\\Users\\Harsh\\Documents\\contest\\{}\\{}".format(contest,P))
