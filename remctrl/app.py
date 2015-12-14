from flask import Flask, render_template, request, jsonify
import os
import schedule

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    
    return render_template('index.html')


@app.route('/logo', methods=['GET', 'POST'])
def logo():
    schedule.play(schedule.xbmcUrl, '/home/osmc/pi_sign/display/logo')
    return "logo"


@app.route('/attractmode', methods=['GET', 'POST'])
def attractmode():

    schedule.play(schedule.xbmcUrl, '/home/osmc/pi_sign/display/attractmode.m3u')
    return "attractmode"

@app.route('/reboot')
def rebootsys():
    os.system('systemctrl restart kodi')

if __name__ == '__main__':
        app.run(debug=True,host='0.0.0.0')

