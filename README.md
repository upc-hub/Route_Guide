# Route_Guide
It is about the system for helping the person, who lost the way by the helpers know the correct route (way).
<img width="766" alt="guide_photo" src="https://github.com/upc-hub/Route_Guide/assets/79504426/00724fdc-ebc8-4849-9d1d-1e77bd03e5c3">
## System Configuration
```
Server
- DigitalOcean
- 8 GB Memory / 4 AMD vCPUs / 160 GB Disk / SFO3 - Ubuntu 18.04 (LTS) x64

Frontend
- HTML, CSS, JavaScript

Backend
- Python

Database
- PostgreSQL

Framework
- Flask Python Web framework
- Nginx HTTP Web server

URL
- https://164.92.104.4
```

## Usage of system
```
- Login to server
- run python3 server.py
- run streamlit run camera_stream.py
```

## Server Configuration
- vi /etc/nginx/sites-available/default
```
server {
  listen 80;
  listen 443 ssl;
  server_name 164.92.104.44;
  ssl_certificate /etc/ssl/certs/nginx-selfsigned.crt;  
  ssl_certificate_key /etc/ssl/private/nginx-selfsigned.key;
  ssl_dhparam /etc/nginx/dhparam.pem;
  location / {
    proxy_pass http://localhost:5000;        
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection "Upgrade";
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_buffering off;
    proxy_cache off;
    proxy_redirect off;
  }
}
```
- nginx -t
- service nginx restart
## User Registration
![register](https://github.com/upc-hub/Route_Guide/assets/79504426/1f70d6ca-9594-46a0-a998-f263120f2ad3)

## Login as a Walker and Helper
![walker](https://github.com/upc-hub/Route_Guide/assets/79504426/8f31d4fb-2ba2-4f93-8335-71a52ec45fc0)

## Route Guiding
<img width="1385" alt="Screenshot 2023-08-19 at 21 07 57" src="https://github.com/upc-hub/Route_Guide/assets/79504426/4239a6a5-d163-415d-a113-114ec3e21ec0">

## Demonstration

## Permission for Location and Audio/Video Access
Google Chrome
- go to chrome://flags/
- search 'unsafely-treat-insecure-origin-as-secure' and enable it
- add these address (http://164.92.104.44, http://164.92.104.44:8501) and relaunch

Firefox
- go to about:config
- set true -> media.devices.insecure.enabled, media.getusermedia.insecure.enabled

Safari
- At computer, go to Developer tab
- search WebRTC and allow Media capture on Insecure Sites
