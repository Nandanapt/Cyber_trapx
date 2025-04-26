from flask import Flask, render_template, request
from utils.email_alert import send_alert
from utils.geo_lookup import get_geolocation

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    # Fake intrusion detection
    fake_ip = '192.168.1.100'
    fake_geo = get_geolocation(fake_ip)  # Get fake location data
    
    # Send email alert
    send_alert(fake_ip, username, password, fake_geo)

    return render_template('index.html', message="Login attempt logged!")

if __name__ == '__main__':
    app.run(debug=True)
