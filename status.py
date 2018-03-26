#imports

import http.client as httplib
import requests
import socket
import sys
import os
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

def send_mail(): 
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login("servicestatus01public@gmail.com", "ServiceStatus01")
 
	msg = "Attention! Host is down!\ntest"
	server.sendmail("servicestatus01public@gmail.com", "victor.puiu01@gmail.com", msg)
	server.quit()

if have_internet():
	internet = "OK"
public_ip_address = requests.get('http://ip.42.pl/raw').text

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
monitoring_ip = "93.116.134.243"
print("=======================")
print("Monitoring IP set to {}".format(monitoring_ip))
print("Monitoring PORT(s) set to: 80 [future versions multiple ports]")
server_ip = monitoring_ip


host_up = True if os.system("ping -c 1 " + monitoring_ip) is 0 else False



###### LOOOP
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