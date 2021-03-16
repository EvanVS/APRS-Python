# APRS-Python
APRS Beaconing, Weather &amp; Telemetry over TCPIP


# Configuration
At the top of the main.py file there is an outlined Configuration section.

- ServerHost - The APRS server hostname or IP
- ServerPort - The APRS server port
- Callsign  - Your callsign (DO NOT INCLUDE SSID)
- SSID - This is the number after your callsign. Entering 0 or nothing will get rid of the SSID and just use your callsign.
- Password - Generate a password on this website for the callsign your going to use. https://apps.magicbug.co.uk/passcode/
- latitude - Your location latitude (In DDMM.MM Format)
- longitude - Your location longitude (In DDMM.MM Format)
- Comment - Your station comment
- Status - Your station status
- Delay - Delay between beacons (Interval)
