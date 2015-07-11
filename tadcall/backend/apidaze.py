import urllib2

SECRET_KEY="PLEASE_CHANGE_THIS"

def getVirtualNumbers():
	response = urllib2.urlopen("https://api4.apidaze.io/e14c0591/numbers?api_secret=" + SECRET_KEY).read()
	return response

def dial(phoneNumber):
	f = open('backend/resources/dial.xml', 'r')
	template = f.read()
	f.close()
	res = template.replace('phone_number', str(phoneNumber))
	return res

def hangup():
	f = open('backend/resources/hangup.xml', 'r')
	template = f.read()
	f.close()
	return template

def voicemail(textToRead):
	f = open('backend/resources/speak.xml', 'r')
	template = f.read()
	f.close()
	res = template.replace('text', str(textToRead))
	return res
