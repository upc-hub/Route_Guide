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
<img width="686" alt="Screenshot 2023-08-19 at 20 53 51" src="https://github.com/upc-hub/Route_Guide/assets/79504426/fda8d128-07d6-4039-8c15-1d48800c10da">

## Login as a Walker

## Login as a Helper

## Route Guiding
