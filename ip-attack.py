#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# 	<=== IP ATTACK ===>
#
#  Name 	:  IP Attack
#  Platform	:  Android Termux
#  Code		:  Python
#  Sec.Code	:  8h4i
#  Coded by	:  Sutariya Parixit
#  Site 		:  bhai4you.blogspot.com
#  Github	:  https://github.com/Bhai4You
#
#
#
# 	<=== WARNING ===>
#
# Do Not Copy Or Modify Without Permission..!!!
#
#	<=== WARNING ===>
#
#
#
#

import sys
import time
import os
from urllib2 import *
from platform import system
print
print
print
os.system("clear")
os.system("bash logo.sh")
print
print
print
print "\033[1m\033[32m\t\t \033[1m\033[31m<==\033[33m[\033[32m Author Info \033[33m]\033[31m==>\033[0m"
time.sleep(3)
print
print
print
print "\033[1m\033[33m\n\tDeveloper : \033[32m \033[33mA\033[32mlfa \033[33mT\033[32mürk\033[0m"
time.sleep(1)
print "\033[1m\033[33m\n\tBlog      :  \033[32mhttp:\033[33m//\033[32mSiber\033[33mE\033[32mkip.net\033[0m"
time.sleep(1)
print "\033[1m\033[33m\n\tGithub    :  \033[32mhttp:\033[33m//\033[32mwww.github.com\033[33m/\033[32mkont0156\033[0m"
time.sleep(1)
print "\033[1m\033[33m\n\tYoutube   : \033[32m \033[33m-\033[32mull \033[33m-\033[32m\033[0m"
time.sleep(2)
print
print

def ping():
	print
	print
	os.system("toilet -f pagga 'Ping Attack       ' | lolcat")
	time.sleep(1)
	print
	
	os.system("curl https://api.hackertarget.com/nping/?q=" + ip)
	print(" ")
	
def http():
	print
	print
	os.system("toilet -f pagga 'Http Bilgileri       ' | lolcat")
	time.sleep(1)
	print
	os.system("curl https://api.hackertarget.com/httpheaders/?q=" + ip)
	print(" ")



def whois():
	print
	print

	os.system("toilet -f pagga 'Whois       ' | lolcat")
	time.sleep(1)
	print
	os.system("curl http://api.hackertarget.com/whois/?q=" + ip)
	print(" ")


def trace():
	print
	print
	os.system("toilet -f pagga 'Traceroute       ' | lolcat")
	time.sleep(1)
	print
	os.system("curl https://api.hackertarget.com/mtr/?q=" + ip)
	print(" ")



def dns():
	print
	print
	os.system("toilet -f pagga 'DNS Araması       ' | lolcat")
	time.sleep(1)
	print
	os.system("curl https://api.hackertarget.com/dnslookup/?q=" + ip)
	print(" ")


def reversedns():
	print
	print
	os.system("toilet -f pagga 'Ters Dns       ' | lolcat")
	time.sleep(1)
	print
	os.system("curl https://api.hackertarget.com/reversedns/?q=" + ip)
	print(" ")


def geoip():
	print
	print
	os.system("toilet -f pagga 'coğrafi Ip Adresi       ' | lolcat")
	time.sleep(1)
	print
	os.system("curl https://api.hackertarget.com/geoip/?q=" + ip)
	print(" ")


def reverseip():
	print
	print
	os.system("toilet -f pagga 'Ters IP       ' | lolcat")
	time.sleep(1)
	print
	os.system("curl https://api.hackertarget.com/reverseiplookup/?q=" + ip)
	print(" ")
	

def nmap():
	print
	print
	os.system("toilet -f pagga 'Port Taraması       ' | lolcat")
	time.sleep(1)
	print
	os.system("curl https://api.hackertarget.com/nmap/?q=" + ip)
	print(" ")



def plink():
	print
	print
	os.system("toilet -f pagga 'Sayfa Bağlantıları       ' | lolcat")
	time.sleep(1)
	print
	os.system("curl https://api.hackertarget.com/pagelinks/?q=" + ip)
	print(" ")


	print
	print
	time.sleep(3)
	print
os.system("clear")
print
os.system( "bash logo.sh" )
print
def mnu():
	print "\033[1m\033[32m[+]\033[36m Whois araması"
	print "\033[32m[+] \033[36mDNS araması"
	print "\033[32m[+]\033[36m ters DNS araması"
	print "\033[32m[+]\033[36m Coğrafi IP araması"
	print "\033[32m[+] \033[36mTers IP aramsı"
	print "\033[32m[+] \033[36mHttp Müdahale"
	print "\033[32m[+] \033[36mPing"
	print "\033[32m[+] \033[36mSayfa Bağlantısı"
	print "\033[32m[+] \033[36mNmap"
	print "\033[32m[+] \033[36mTraceroute"
	
print
print
print
mnu()
print
print
print "\033[1m\033[32mEnter Your IP Or Domain..."
print
ip = raw_input("\033[1m\033[32m IP or Domain : \033[33m\033[1m")
print
time.sleep(3)
whois()
dns()
reversedns()
geoip()
reverseip()
http()
ping()
plink()
nmap()
trace()
sys.exit()
	
