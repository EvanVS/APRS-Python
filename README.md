# APRS-Python
This script makes it easy and simple to start beaconing your location on the APRS network by sending your position directly to the APRS.IS servers via the TCP web socket protocol. This script has been tested using Python 3.8 on Windows. Please note you MUST hold a valid amateur radio call sign to use this script. Using any service that connects/could connect to the amateur radio frequencies without a valid amateur radio call sign is a violation of federal law as outlined by the FCC.


# Configuration
At the top of the main.py file there is an outlined Configuration section. Some of these values such as Call sign, Password, Latitude and Longitude require you to put in your information in order to use this script.

- Server Host - The APRS server host name or IP (Default: fire net.us)
- Server Port - The APRS server port (Default: 10154)
- Call sign - Your call sign (DO NOT INCLUDE SSID)
- SSID - This is the number after your call sign. Entering 0 or nothing will get rid of the SSID and just use your call sign.
- Password - Generate a password on this website for the call sign your going to use. https://apps.magicbug.co.uk/passcode/
- latitude - Your location latitude (In DDMM.MM Format)
- longitude - Your location longitude (In DDMM.MM Format)
- Comment - Your station comment
- Status - Your station status
- Status_Packet - Enable/Disable sending the status packet (Default: False)
- Primary_Symbol_Key - This is a forward or back slash indicating if you are picking the primary set of symbols or the secondary set. (mentioned more in the link below)
- Secondary_Symbol_Key - Sets the station symbol. You can see the available symbols here: https://blog.thelifeofkenneth.com/2017/01/aprs-symbol-look-up-table.html
- Delay - Delay between beacons in seconds (Interval) (Default: 600 (10 mins))

# Future Features
- WX Telemetry - The ability to connect to a JSON API hosted on a ESP8266 with weather sensors connected
- Telemetry - The ability to connect to a JSON API hosted on a ESP8266 with voltage/temperature sensors connected
- Messaging - The ability to send messages through the APRS network when telemetry meets certain criteria
- GPS Support - The ability to use a USB GPS dongle to automatically change your beaconed position.
