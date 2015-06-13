import urllib2


def getVirtualNumbers():
	response = urllib2.urlopen("https://api4.apidaze.io/e14c0591/numbers?api_secret=***REMOVED***").read()
	return response

def dial(phoneNumber):
	f = open('dial.xml', 'r')
	template = f.read()
	f.close()
	res = template.replace('phone_number', str(phoneNumber))
	return res

def hangup():
	f = open('hangup.xml', 'r')
	template = f.read()
	f.close()
	return template

def voicemail(textToRead):
	f = open('speak.xml', 'r')
	template = f.read()
	f.close()
	res = template.replace('text', str(textToRead))
	return res
