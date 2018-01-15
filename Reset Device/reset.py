import RPi.GPIO as GPIO
import os
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

counter = 0

while True:
    while GPIO.input(4) == 1:
        time.sleep(1)
        counter = counter + 1

        print(counter)

        if counter == 9:
            os.system('sudo mv /etc/wpa_supplicant/wpa_supplicant.conf /etc/wpa_supplicant/wpa_supplicant.conf.OLD')
            os.system('sudo rm -f /usr/share/configure_wifi/tmp/*')
            os.system('sudo cp /usr/share/configure_wifi/Reset_Device/static_files/dhcpcd.conf /etc/')
            os.system('sudo cp /usr/share/configure_wifi/Reset_Device/static_files/hostapd.conf /etc/hostapd/')
            os.system('sudo cp /usr/share/configure_wifi/Reset_Device/static_files/dnsmasq.conf /etc/dnsmasq.conf')
            os.system('sudo cp /usr/share/configure_wifi/Reset_Device/static_files/default_hostapd /etc/default/hostapd')
            os.system('sudo cp /usr/share/configure_wifi/Reset_Device/static_files/rc.local.aphost /etc/rc.local')
            os.system('sudo reboot')

        if GPIO.input(4) == 0:
            counter = 0
            break

    time.sleep(1)

