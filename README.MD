# Headless WiFi Setup for Raspberry Pi : IoT Type Projects
### RaspiWiFi: From Guided WiFi configuration software for the Raspberry Pi, Copyright (C) 2015 Jason Burgett jasbur@gmail.com with modifications from [Makomo](https://github.com/MAKOMO/) and this release mexmarv@gmail.com.

RaspiWiFi is a program to headlessly configure a Raspberry Pi's WiFi connection using any other WiFi-enabled device (much like the way a Chromecast or similar device can be configured). RaspiWiFi has been tested with the Raspberry Pi B+, Raspberry Pi 3, and Raspberry Pi Zero W.

<img src="https://github.com/marvmex/IoT-RaspiWiFi/blob/master/Configuration%20App/app/assets/images/calendar.png" alt="Raspbian Headless WiFi" width="20%"> &nbsp; <img src="https://github.com/marvmex/IoT-RaspiWiFi/blob/master/Configuration%20App/app/assets/images/rstretch.png" alt="Raspbian Stretch" width="43%">

* This version has been updated for use in Raspbian Stretch (as of June 2018 release).
* This version no longer affects `/etc/network/interfaces`.  It now configures via `/etc/dhcpcd.conf` and runs `dnsmasq` for DNS server instead of `isc-dhcp-server`.

### INSTALLATION INSTRUCTIONS:

*To install:*
```
git clone https://github.com/marvmex/IoT-RaspiWiFi.git
cd IoT-RaspiWiFi
sudo sh start.sh
```

_This script will install all necessary prerequisites, copy configuration files, and reboot. When it finishes booting it should present itself in "Configuration Mode" as a WiFi access point with the SSID **pi-IoT**._

### OBSERVATIONS:

* If you run a non-stock **/etc/rc.local**, modify **rc.local.apclient** and **rc.local.apclient.template** in `/usr/share/configure_wifi/Reset_Device/static_files/`
* `/etc/rc.local` will be overwritten **everytime** the system configured to act as a wifi access point for setting up a new network.
* If you happen to need a non-stock `rc.local` during the short time when the system is in the "Configure WiFi" configuration, modify `rc.local.aphost` and `rc.local.aphost.template`.
* `su -c "cd /usr/share/configure_wifi/Configuration_App/ && rails s -b 10.0.0.1 -e production -p 10 -d" &` if you need to start the rails web server on IP and port.

### USAGE:

* Connect to the **pi-IoT** SSID Open Access Point using any other WiFi enabled device.
* Navigate to http://10.0.0.1:10 **(Port:10 IP:10.0.0.1)** using any web browser on the device you connected with. It may take several seconds (or a minute) before the server is ready to accept requests.  
* If you're connected to the RasPi via WiFi, it will give you an IP in its network but the web page is timing out (web server still not loaded), then just wait a couple seconds till it appears (patiently)...
* Select the **WiFi SSID** connection you'd like your Raspberry Pi to connect to from the drop down list and enter its wireless **password** on the page provided. If no encryption is enabled, leave the password box blank.
* Click the **Connect** button.
* At this point your Raspberry Pi will reboot and connect to the access point specified.

The files for this process are stored in **/usr/share/configure_wifi** 

### RESETTING THE DEVICE:

* If **GPIO 4** is pulled **high** for 10 seconds or more, the Raspberry Pi will reset all settings, reboot, and enter "Configuration Mode" again. It's useful to have a simple button wired on GPIO 4 to reset easily if moving to a new location, or if incorrect connection information is ever entered. Just press and hold for 10 seconds or longer.
* You can also reset the device by running: 
`sudo python3 /usr/share/configure_wifi/Reset_Device/manual-reset.py`

_Enjoy!_
