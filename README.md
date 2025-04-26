# Cyber_trapx
A honeypot is a security system designed to trap malicious actors or attackers by presenting a fake system.
1. Login Page Simulation
You have a login page (the one where a user enters a username and password).

When someone (a hacker or user) tries to enter a username and password, the system does not verify it like a real login system. Instead, it logs the input details as if it was a real login attempt.This simulates a real-world attack attempt where an attacker might try to break into a system by guessing passwords.

2. Fake IP Address and Geolocation
After the user submits their login credentials, you use a fake IP address (192.168.1.100), which is commonly used in local networks, and it's meant to simulate the IP address of an attacker.You also simulate getting a geolocation based on the IP address, using a mock function. This simulates what would happen in a real-world attack detection system that tries to identify the location of an attacker based on their IP.The actual IP is irrelevant here, but in a more realistic scenario, you could integrate a real IP geolocation API to gather more accurate attacker details.

3. Email Alerts for Intrusion Attempts
When a user (or attacker) attempts to log in, the system logs their username, password, and fake IP address and then sends an email alert.The email alert contains information such as:

Fake IP address (192.168.1.100)
The username and password they entered.The fake geolocation data of the attacker (even though it’s simulated in this case).This alert goes to an email address of your choice (you could have your email set up), which notifies you every time a login attempt is made.This feature simulates the kind of alert system you'd have in real-time if you were monitoring a production system for suspicious logins.

4. User Feedback on Login Attempt
After the login attempt is made (whether it's successful or not), the system provides feedback to the user by showing the message "Login attempt logged!" on the page.This simulates the idea that the system is recording and reacting to the intrusion attempt, even though it's entirely fake.This message could potentially be enhanced to look more convincing, like showing a countdown or fake error message to simulate a real hacking attempt.
