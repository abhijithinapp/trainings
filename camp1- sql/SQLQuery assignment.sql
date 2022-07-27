 SELECT name from master.sys.databases ORDER BY name;

 CREATE DATABASE hospital_db

 USE hospital_db

 BACKUP DATABASE hospital_db TO DISK = 'F:\abhijith mssql training\hospital_db.bak'

 USE master

 DROP DATABASE hospital_db

 RESTORE DATABASE hospital_db FROM DISK = 'F:\abhijith mssql training\hospital_db.bak'