#imports

import http.client as httplib
import requests
import socket
import sys
import os
import random
import string
import smtplib
from time import sleep
from subprocess import Popen, PIPE, STDOUT

#functions
def have_internet():
    conn = httplib.HTTPConnection("www.google.com", timeout=5)
    try:
        conn.request("HEAD", "/")
        conn.close()
        return True
    except:
        conn.close()
        return False

def id_generator(size=8, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

if have_internet():
	internet = "OK"
public_ip_address = requests.get('http://ip.42.pl/raw').text


def send_mail(): 
	server = smtplib.SMTP('SMTP_ADDRESS', SMTP_PORT)
	server.starttls()
	server.login("SMTP_USERNAME", "SMTP_PASSWORD")
 
	msg = ("This message is sent from DNSStatus running on {}\nThe target host ( {} ) has been reported down and not reachable.\nDo not reply to this message!\nHASH:{}".format(public_ip_address, monitoring_ip, id_generator()))
	server.sendmail("SMTP_USERNAME", "SMTP_DESTINATION_ADDRESS", msg)
	server.quit()




monitoring_ip = "REMOTE HOST IP"
#script


print("=======================")
sleep(0.3)
print("====DNSStatus v0.1a====")
sleep(0.3)
print("=======================")
sleep(0.3)

print("DNSStatus initializing...")
sleep(0.3)
print("Setting lang to: EN_US...OK")
sleep(0.3)
print("Enabling SMTP module...OK")
sleep(0.3)
print("Enabling SMTP_TLS...OK")
sleep(0.3)
print("Developed by: vscorpio # http://github.com/vscorpio")
sleep(0.3)
print("Checking connection status...{}".format(internet))
sleep(0.3)
print("Connected to internet via {}".format(public_ip_address))
sleep(0.3)
print("=======================")
#monitoring_ip = input('Please enter the IP you want to monitor: ')
if monitoring_ip is not None:
	print("Skipping user input for monitoring IP because it hard-coded. (View readme)")
print("=======================")
print("Monitoring IP set to {}".format(monitoring_ip))
print("Monitoring PORT(s) set to: 80 [future versions multiple ports]")
server_ip = monitoring_ip


host_up = True if os.system("ping -c 1 " + monitoring_ip) is 0 else False

var = 1
while var==1:
	if host_up is True:
		print('Target host is UP. Sleeping for 2 hours!')
	else:
		print('Target host is DOWN. Warning! Sending MAIL...rechecking in 2 hours...')
		send_mail()
	sleep(1800)
	print('1h30mins left to recheck...')
	sleep(1800)
	print('1h left to recheck...')
	sleep(3600)
	print('rechecking...')

