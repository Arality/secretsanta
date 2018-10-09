from random import shuffle
import json

Names = json.loads(open("names.json").read())

def notify(name,name2):		# Function to text list
	pass
	print(name,name2)
	return

def nameshuffle(array):		# Makes a copy of arrary and shuffles sending different names to notify()
	array2 = array[::-1].copy()
	shuffle(array)
	while len(array) != 0:
		if len(array) == 2 and array[0] == array2[0] and array[1] == array2[1]:
			shuffle(array)
		if array[0] != array2[0]:
			notify(array[0], array2[0])
			array.pop(0)
			array2.pop(0)
		else:
			shuffle(array)
	return



			
nameshuffle(Names)