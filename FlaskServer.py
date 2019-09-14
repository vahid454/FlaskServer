
from wit import Wit
import json
import sys

import os
from flask import Flask
from flask import request
app = Flask(__name__)
def getResult(args):
	client = Wit("J55QIEQPKJ4PBJOVFDXYKVZNW3PWONEI")
	x=args
	resp=client.message(x)
	#print(resp)
	value=""
	if resp["entities"]=={}:
		return "Wrong text";

	else:
		entities=resp["entities"];
		intents=entities["intent"];
		intent=intents[0];
		#print(intent);
		value=intent["value"];

	#print(value);
	if value=="greeting":
		return "Hello Sir !! May I help you?";
		
	if value=="agree":
		return "Thanks , What Can I do for you? ";
	if value=="helps":
		return "Yes , I can search anything for you. I can open your any apps I can call to any number from your contats any other things similar to that." ;
		
	if value=="exit":
		return "Closing"
		#sys.exit(0);

	if value=="discard":
		return "Okay ! Thanks I'll be working on myself";
	if value=="ok":
		return "Yepp !!";
	if value=="call":
		return "Ok Calling "+x[5:];		








@app.route("/")
def hello():
    return "Hello World!"

@app.route("/chatbot")
def chatbot():
 #os.system("eg2.py 1")
 
 question=request.args.get('question') 
 result=getResult(question)
 return result

if __name__ == "__main__":
 app.run()
