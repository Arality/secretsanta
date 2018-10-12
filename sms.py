import smtplib
import json
from time import sleep


Carriers = {
	'att':    	'@txt.att.net',
	'tmobile':	'@tmomail.net',
	'verizon':  '@vtext.com',
	'sprint':   '@messaging.sprintpcs.com',
	'fi':		'@msg.fi.google.com',
	'gvoice':	'@txt.voice.google.com',
	'gmail':	'@gmail.com'	#Fallback incase you want to use email
}

def send(message, to_number, provider):
	Credentials = json.load(open('credentials.json', 'r'))
	# Replace the number with your own, or consider using an argument\dict for multiple people.
	# to_number = Credentials["phonenumber"]
	auth = (Credentials["email"], Credentials["password"])

	# Establish a secure session with gmail's outgoing SMTP server using your gmail account
	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.starttls()
	server.login(auth[0], auth[1])

	# Send text message through SMS gateway of destination number
	server.sendmail( auth[0], to_number+Carriers[provider], message)
	sleep(15)
	return