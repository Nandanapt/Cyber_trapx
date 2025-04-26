import socket, threading
from utils.email_alert import send_alert
from utils.geo_lookup import get_geolocation
import sqlite3
from datetime import datetime

def fake_login(client_socket):
    client_socket.send(b"Username: ")
    username = client_socket.recv(1024).decode().strip()
    client_socket.send(b"Password: ")
    password = client_socket.recv(1024).decode().strip()
    return username, password

def log_intrusion(ip, username, password):
    geo = get_geolocation(ip)
    conn = sqlite3.connect("logs/intrusions.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO logs (ip, username, password, city, country, time) VALUES (?, ?, ?, ?, ?, ?)",
                   (ip, username, password, geo['city'], geo['country'], str(datetime.now())))
    conn.commit()
    conn.close()
    send_alert(ip, username, password, geo)

def handle_connection(client_socket, address):
    ip = address[0]
    username, password = fake_login(client_socket)
    log_intrusion(ip, username, password)
    client_socket.send(b"Access Denied.\n")
    client_socket.close()

def start_honeypot(port=2222):
    server = socket.socket()
    server.bind(('0.0.0.0', port))
    server.listen(5)
    print(f"Honeypot active on port {port}")
    while True:
        client_socket, addr = server.accept()
        threading.Thread(target=handle_connection, args=(client_socket, addr)).start()
