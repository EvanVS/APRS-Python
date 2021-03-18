import sys, time, json
from socket import *
import datetime

#            _____  _____   _____   _____       _   _                 
#      /\   |  __ \|  __ \ / ____| |  __ \     | | | |                
#     /  \  | |__) | |__) | (___   | |__) |   _| |_| |__   ___  _ __  
#    / /\ \ |  ___/|  _  / \___ \  |  ___/ | | | __| '_ \ / _ \| '_ \ 
#   / ____ \| |    | | \ \ ____) | | |   | |_| | |_| | | | (_) | | | |
#  /_/    \_\_|    |_|  \_\_____/  |_|    \__, |\__|_| |_|\___/|_| |_|
#                                          __/ |                      
#  https://github.com/EvanVS/APRS-Python  |___/    Version: 0.12 BETA  


# ---------------- INFORMATION ----------------
#
#  APRS Python - V0.12 BETA Release
#  Evan Vander Stoep - March, 2021
#  
#  This script is open source. Please leave author credit.
#  
# ---------------- INFORMATION ----------------


# --------------- CONFIGURATION ---------------

ServerHost = 'firenet.us'
ServerPort = 10154

Callsign = 'N0CALL'
SSID = '-5'
Password = '12345' # Generate here: https://apps.magicbug.co.uk/passcode/

Latitude = '0000.00N'
Longitude = '00000.00W'

Comment = 'https://github.com/EvanVS/APRS-Python'
Status = 'APRS Python'
Status_Packet = False # False = Do not send status message packet

Primary_Symbol_Key = '/'
Secondary_Symbol_Key = '_' # Default is the House symbol. More info here: https://blog.thelifeofkenneth.com/2017/01/aprs-symbol-look-up-table.html

Delay = 600 # 10 Mins (Value is in seconds)

# --------------- CONFIGURATION ---------------



def check_config():
	global ServerHost
	global ServerPort
	global Callsign 
	global SSID
	global Password
	global Latitude
	global Longitude
	global Comment
	global Status
	global Delay
	if ServerHost == '':
		print("CONFIG ERROR: No server host defined! Check configuration and try again!")
		exit()
	if ServerPort == None:
		print("CONFIG ERROR: No server port defined! Check configuration and try again!")
		exit()
	if Callsign == '' or Callsign == 'N0CALL':
		print("CONFIG ERROR: No Callsign defined! Check configuration and try again!")
		exit()
	elif "-" in Callsign:
		print("CONFIG ERROR: SSID Specified in the Callsign field! Please Specify the SSID in the SSID field! Check configuration and try again!")
		exit()
	if Password == '' or Password == '12345':
		print("CONFIG ERROR: No password defined! Check configuration and try again!")
		exit()
	if Latitude == '':
		print("CONFIG ERROR: No Latitude defined! Check configuration and try again!")
		exit()
	if Longitude == '':
		print("CONFIG ERROR: No Longitude defined! Check configuration and try again!")
		exit()
	if len(Comment) > 43:
		print(f"CONFIG ERROR: Comment is over 43 characters ({len(Comment)}/43)! Make it shorter and try again!")
	if len(Status) > 43:
		print(f"CONFIG ERROR: Status is over 43 characters ({len(Status)}/43)! Make it shorter and try again!")
	if Delay == None:
		Delay = 600 # Defaults to 10 Mins
	else:
		print("CONFIGURATION OK")

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = 'Next Packet: {:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t -= 1

def send_packet():
	global ServerHost
	global ServerPort
	global Callsign 
	global SSID
	global Password
	global Latitude
	global Longitude
	global Comment
	global Status
	global Delay

	# create socket & connect to server
	sSock = socket(AF_INET, SOCK_STREAM)
	sSock.connect((ServerHost, ServerPort))
	# logon
	RAWpacket = f'user {Callsign} pass {Password} vers "KJ7BRE APRS Python" \n'
	sSock.send(bytes(RAWpacket, 'utf-8'))
	
	# send BEACON packet
	BEACONpacket = f'{Callsign}{SSID}>APE,TCPIP*:={Latitude}/{Longitude}-{Comment}\n'
	sSock.send(bytes(BEACONpacket, 'utf-8'))
	
	print(BEACONpacket)
	print("[BEACON packet sent]")
	
	if Status_Packet == True and Status != '':
		countdown(5)
		# send STATUS packet
		STATUSpacket = f'{Callsign}{SSID}>APE,TCPIP*:>{Status}\n'
		sSock.send(bytes(STATUSpacket, 'utf-8'))
		
		print(STATUSpacket)
		print("[STATUS packet sent]")
	else:
		pass
	
	# close socket -- must be closed to avoid buffer overflow
	sSock.shutdown(0)
	sSock.close()
	print("\n----------")

check_config()
while True:
	send_packet()
	countdown(Delay)
