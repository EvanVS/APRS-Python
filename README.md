# APRS-Python
This script makes it easy and simple to start beaconing your location on the APRS netowrk by sending your position directily to the APRS.IS servers via the TCP websocket protocol. This script has been tested using Python 3.8 on Windows. Please note you MUST LEAGALLY have a valid amateur radio callsign to use this script. Operating anything that connect to the amateur radio frequencies without a valid amateur radio callsign is agenst federal law as outlined by the FCC.


# Configuration
At the top of the main.py file there is an outlined Configuration section. Some of thease values such as Callsign, Password, Latitude and Longitude require you to put in your information in ourder to use this script.

- ServerHost - The APRS server hostname or IP (Default: firenet.us)
- ServerPort - The APRS server port (Default: 10154)
- Callsign  - Your callsign (DO NOT INCLUDE SSID)
- SSID - This is the number after your callsign. Entering 0 or nothing will get rid of the SSID and just use your callsign.
- Password - Generate a password on this website for the callsign your going to use. https://apps.magicbug.co.uk/passcode/
- latitude - Your location latitude (In DDMM.MM Format)
- longitude - Your location longitude (In DDMM.MM Format)
- Comment - Your station comment
- Status - Your station status
- Delay - Delay between beacons in seconds (Interval) (Default: 600 (10 mins))
