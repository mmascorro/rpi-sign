# notes

Python script & web app to crontrol videos on Raspberry Pi running Kodi.

Currently works with the OSMC distro

## setup

Make display folder in project root. Place videos and playlists there.

Copy pi-sign.service to /etc/systemd/system/

Make symlink ~/.kodi/userdata/autoexec.py to kodi_autoexec.py


## crontab examples:
30 08 * * * python /home/osmc/pi_sign/remctrl/schedule.py /home/osmc/pi_sign/display/logo
20 09 * * * python /home/osmc/pi_sign/remctrl/schedule.py /home/osmc/pi_sign/display/attractmode.m3u
