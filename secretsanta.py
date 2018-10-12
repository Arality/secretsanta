from random import shuffle
import json
from sms import send
import smtplib

Names = json.load(open('names.json', 'r'))

# Function to text list
def notify(Sender,Reciever):
	for i in range(len(Sender)):
		Message = f"Hello, {Sender[i]['name']} you are getting a gift for {Reciever[i]['name']}. The spending limit this year is $50.
		send(Message, Sender[i]['cell'], Sender[i]['provider'])
	return

# Makes a copy of arrary and shuffles returning two random arrays from one input
def nameshuffle(array):
	array2 = array[::-1].copy()
	NewArray = array.copy()
	shuffle(NewArray)
	SendersList = []
	RecieversList = []
	while len(NewArray) != 0:
		if len(NewArray) == 2 and NewArray[0]['name'] == array2[0]['name'] and NewArray[1]['name'] == array2[1]['name']:
			shuffle(NewArray)
		if NewArray[0]['name'] != array2[0]['name']:
			SendersList.append(NewArray[0])
			RecieversList.append(array2[0])
			NewArray.pop(0)
			array2.pop(0)
		else:
			shuffle(NewArray)
	return (SendersList, RecieversList)

List1, List2 = nameshuffle(Names)
notify(List1, List2)