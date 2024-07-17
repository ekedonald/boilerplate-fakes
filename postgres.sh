#! /bin/bash
sudo sh -c 'echo "deb https://apt.PostgreSQL.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
wget --quiet -O - https://www.PostgreSQL.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo apt update
sudo apt install postgresql-16 -y
sudo systemctl start postgresql
sudo systemctl enable postgresql
#########################################################

# sudo -u postgres psql -c "ALTER USER postgres WITH PASSWORD 'password';"