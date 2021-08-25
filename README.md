# api
api
#! /bin/sh
mysql -u root -ppassword --default-character-set=utf8 sa_bdt  << EOFMYSQL
SELECT * FROM music where singer like '人%';
EOFMYSQL
