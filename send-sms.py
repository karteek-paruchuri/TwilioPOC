import sys
import datetime
import time
from twilio import TwilioRestException
from twilio.rest import TwilioRestClient

def send_sms(targetnumber, message):
	account_sid = "AC246bca7d6456941711fa3522508aa028" # Your Account SID from www.twilio.com/console
	auth_token  = "eb2fa125252acd704080c2b598ca1359"  # Your Auth Token from www.twilio.com/console

	t_account_sid = "AC09e2de1cebf27ab75e05e9dbf3dcbdc6"
	t_auth_token = "efe41554b950847da4329f507a1d7998"

	#client = TwilioRestClient(t_account_sid, t_auth_token)
	client = TwilioRestClient(account_sid, auth_token)

	try:
		if targetnumber[:2] != '+1':
			print 'please enter a valid US number in the format +1<10_digit_number>'
			return
		else:
			message = client.messages.create(body = message + '#KapaTwilioBot',
			to = targetnumber,    # Replace with your phone number
			from_ = "+12028997890") # Replace with your Twilio number
	except TwilioRestException as e:
	    print(e)
	return 

if __name__ == '__main__':
	if len(sys.argv) != 3 :
		print 'please enter phone number and message!'
		sys.exit(0)
	if len(sys.argv[1]) != 12:
		print 'please enter a valid US number in the format +1<10_digit_number>'
		sys.exit(0)
	send_sms(sys.argv[1], sys.argv[2])
	print 'success!'
