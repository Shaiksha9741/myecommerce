#!/bin/bash

ssh -i "Key_pair36.pem" ubuntu@ec2-15-207-100-225.ap-south-1.compute.amazonaws.com <<EOF
  cd myecommerce
  git pull 
  source env/bin/activate
  ./manage.py migrate
  sudo systemctl restart nginx
  sudo service gunicorn restart
  sudo service nginx restart
  exit
EOF
