#Author-Harsh Sharma
#codeforces-id:Codula
#codechef-id:Codula1
#Atcoder-id:Codula

#This script will Parse The input and Output
#USE:
#python3 parse.py <Folder-Name> <Problem-Name>
#List 8625 as a port in competitive companion.
#Go to any problem and press the comcompetitive companion icon.



from flask import Flask , request , redirect
import json , subprocess
import datetime
import os
import sys

port1 = 8625

def PARSEIT(data):
	taskData = json.loads(data.decode())
		# print(subprocess.check_output(['subl' , os.path.join(baseContestPath , contestName , taskName + '.cpp')]))
	with open("C:\\Users\\Harsh\\Documents\\contest\\cache.json","wb") as cache:
		cache.write(json.dumps(taskData).encode())
	with open("C:\\Users\\Harsh\\Documents\\contest\\cache.json") as cache:	
		Final=json.load(cache)
	a=1
	for io in Final["tests"]:
		inp=open("C:\\Users\\Harsh\\Documents\\contest\\{}\\{}\\in{}".format(sys.argv[1],sys.argv[2],a),"w")	
		inp.write(io["input"])
		inp.close()
		out=open("C:\\Users\\Harsh\\Documents\\contest\\{}\\{}\\out{}".format(sys.argv[1],sys.argv[2],a),"w")	
		out.write(io["output"])
		out.close()
		a+=1
	

personalparser = Flask(__name__)

@app.route('/' , methods = ['POST'])
def getData():
	PARSEIT(request.data)
	return redirect('/')

personalparser.run(port=port1)
