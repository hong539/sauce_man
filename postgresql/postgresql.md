# postgresql

## db_init

```shell
#Create user and db
sudo -iu postgres
createuser --interactive
createdb sauce_man -O sauce_man

#Add passwd
sudo -u postgres psql
ALTER USER username WITH PASSWORD 'new_password';

#Client authentication
sudo vim /var/lib/postgres/data/pg_hba.conf
sudo systemctl restart postgresql.service
```