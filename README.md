# robot_raspberrypi

this repo contains all the files required to setup the raspberry pi robot with server page to control it

## Start run.sh on boot

1. Open terminal
2. Type `sudo nano /etc/rc.local`
3. Add the following line before `exit 0`:
```
sudo /home/pi/robot_raspberrypi/run.sh
```
4. Press `Ctrl + X` to exit, then `Y` to save and `Enter` to confirm the file name
5. Reboot the Raspberry Pi

