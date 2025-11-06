#!/bin/bash
ssh ubuntu@13.233.53.199 <<EOF
  cd myecommerce
  git pull 
  source env/bin/activate
  ./manage.py migrate
  sudo systemctl restart nginx
  sudo service gunicorn restart
  sudo service nginx restart
  exit
EOF
