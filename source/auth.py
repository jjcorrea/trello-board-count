import urlparse
import oauth2 as oauth
from config import *

def authenticate():
	consumer = oauth.Consumer(CONSUMER_KEY, CONSUMER_SECRET)
	client = oauth.Client(consumer)

	resp, content = client.request(request_token_url, "GET")
	if resp['status'] != '200':
		raise Exception("Invalid response %s." % resp['status'])

	request_token = dict(urlparse.parse_qsl(content))

	print "Go to the following link in your browser:"
	print "%s?oauth_token=%s&scope=read&name=Trello+List+Counter" % (authorize_url, request_token['oauth_token'])

	accepted = 'n'
	while accepted.lower() == 'n':
		accepted = raw_input('Have you authorized me? (y/n) ')
	oauth_verifier = raw_input('What is the PIN? ')

	token = oauth.Token(request_token['oauth_token'],
		request_token['oauth_token_secret'])
	token.set_verifier(oauth_verifier)
	client = oauth.Client(consumer, token)

	resp, content = client.request(access_token_url, "POST")
	return dict(urlparse.parse_qsl(content))