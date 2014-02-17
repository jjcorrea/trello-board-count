#!/usr/bin/python2.7
from trollop import TrelloConnection
from auth import *

trello = TrelloConnection(CONSUMER_KEY, authenticate()['oauth_token'])

for board in filter(lambda b: b.name.lower() in BOARDS, trello.me.boards):
	print '# %s' % board.name
	for l in filter(lambda l: l.name.lower() in LISTS, board.lists):
		print '%s:%i' % (l.name,len(l.cards))

