--To create a new database
CREATE DATABASE hospital_database

--List all databases
SELECT name from master.sys.databases ORDER BY name;

--Selecting a particulat database
USE db_name;

--backing up a database 
BACKUP DATABASE hospital_database TO DISK = 'F:\abhijith mssql training\hospital.bak';

--backup the differences only
BACKUP DATABASE hospital_database TO DISK = 'F:\abhijith mssql training\hospital.bak' WITH DIFFERENTIAL;

--Restore the database from backup
RESTORE DATABASE employee_db FROM DISK = 'F:\abhijith mssql training\hospital.bak' WITH REPLACE;

--Delete a database 
DROP DATABASE employee_db;

--viewing current schema 
SELECT SCHEMA_NAME()

--creating new schemas 
CREATE SCHEMA myschema1

--creating a schema explicitly by specifying owner
CREATE SCHEMA  myschema2 AUTHORIZATION dbo

--To create objects under the schema 
CREATE TABLE myschema1.mytable1(
ID INT,
FirstName NVARCHAR(50) NOT NULL,
LastName NVARCHAR(50) NOT NULL
);

--TO transfer database objects from one scheme to another schema in the same database
ALTER SCHEMA myschema1 TRANSFER OBJECT::dbo.employeemaster

-- To change the owner of the schema 
ALTER AUTHORIZATION ON SCHEMA ::myschema1 TO dbo

--to drop schema
DROP SCHEMA IF EXISTS myschema1

-----------------------------------------------------------
------------------SQL CONSTRAINTS--------------------------
-----------------------------------------------------------

--create a dummy table
CREATE TABLE  employee(
id INT IDENTITY PRIMARY KEY,
name varchar(50),
age SMALLINT,
location varchar(50)
);

--adding a column after creating the table 
ALTER TABLE employee
ADD DOB date;

--inserting values into a table
INSERT INTO employee(name, age, location, dob)
VALUES ('Tom', 2, 'USA', '2018-10-20'),
('Jerry',1,'USA', '2018-10-20'),
('Mickey', 3, 'USA', '2018-10-20');

--view all data in the table
SELECT *  FROM employee;


