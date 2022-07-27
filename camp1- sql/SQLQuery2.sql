USE employee_db

CREATE TABLE employee(
	id INT IDENTITY PRIMARY KEY,
	name VARCHAR(50),
	age SMALLINT ,
	location VARCHAR(50)
	);

ALTER TABLE employee 
ADD DOB date;


EXEC sp_help employee

INSERT INTO employee
VALUES('Tom',4,'USA','5/7/2019'),
('Sam',4,'LA','5/7/2019'),
('Amy',6,'USA','5/7/2020');

SELECT *
FROM employee

UPDATE employee
SET name='Sil'
WHERE name='Tom'

DELETE FROM employee
WHERE NAME='Sil'

DROP table employee

--create db 
USE hospital_db

CREATE TABLE patient(
	rec_no INT IDENTITY PRIMARY KEY,
	pat_name VARCHAR(50),
	pat_num BIGINT,
	pat_gender VARCHAR(6),
	pat_age SMALLINT,
	pat_loc VARCHAR(50)
);

INSERT INTO patient
VALUES('Amy',9874456568,'F',23,'kylm'),
('Abi',894569568,'M',19,'tvm'),
('Sen',785755664,'F',25,'klm');

ALTER TABLE patient 
DROP COLUMN pat_loc;


DELETE FROM patient 
WHERE pat_age=19;

SELECT *
FROM patient

USE northwind

SELECt *
FROM products

--aggregrate functions

SELECT MAX(UnitPrice) AS 'MIN Product Price'
FROM products 

SELECT MAX(UnitPrice) AS 'Max price'
FROM products

SELECT AVG(UnitPrice) AS 'Average Price'
FROM products
  
Select ProductID,ProductName,UnitPrice FROM Products
WHERE UnitPrice<(SELECT AVG(UnitPrice) FROM Products)

SELECT SUM(UnitsInStock) AS 'TOTAL STOCK'
FROM Products
WHERE Discontinued=1

--COUNT AGGEREGRATE FUN
SELECT COUNT(ProductID) AS 'TOTAL'
FROM Products
WHERE Discontinued=1

USE employee_db
CREATE DATABASE ques

USE ques

CREATE TABLE customers(
	customer_id INT PRIMARY KEY,
	cust_name VARCHAR(50),
	city VARCHAR(50),
	grade INT,
	sales_amount INT);

INSERT INTO customers
VALUES (3002,'Anna Anthony','New York',100,5001),
(3007,'Samantha Carl','New York',200,4001),
(3005,'Jacob James','California',200,2002),
(3008,'Sophie Green','London',300,6002),
(3004,'Joe William','Paris',300,9000);

SELECT * FROM customers

--TOTAL CUSTOMERS

SELECT COUNT(customer_id) AS 'TOTAL NO. OF CUSTOMERS'
FROM customers

SELECT * FROM customers
WHERE grade=(SELECT MAX(grade) FROM customers)

SELECT * FROM customers
WHERE grade=(SELECT MIN(grade) FROM customers);

SELECT AVG(sales_amount) AS 'AVG_SALES_AMOUNT'
FROM customers

SELECT SUM(sales_amount) AS 'total_sales_amount'
FROM customers


--cause in sql
USE Northwind
SELECT * FROM customers
SELECT DISTINCT city , Region FROM customers
WHERE country='UK'
SELECT COUNT(CustomerId) AS 'TOTAL CUSTOMER' ,Country
FROM customers


ORDER BY COUNTRY DESC

--where clause ,"=" and "with"
SELECT * FROM Suppliers


SELECT CompanyName,City
FROM suppliers
WHERE country='USA'
ORDER BY CompanyName

SELECT * FROM Employees
WHERE EmployeeID BETWEEN 1 AND 5


--in and like operator
SELECT * FROM Employees
WHERE EmployeeID IN (1,2,3)

SELECT * FROM Employees
WHERE FirstName LIKE 'Steven'

--orderby clause
--DESCENDING ORDER
SELECT * FROM Employees
WHERE EmployeeID >1
ORDER BY HireDate DESC;
--ASCENDING OREDR
SELECT FirstName,BirthDate FROM Employees
ORDER BY BirthDate DESC,FirstName ASC;
--Having clause same as where clause to be used with aggregrate fun
SELECT  ProductName,UnitPrice FROM Products
	GROUP BY ProductName,UnitPrice
    HAVING (UnitPrice)>25
--concatination
SELECT * FROM Employees

SELECT CONCAT(FirstName,' ',LastName)AS FullName FROM Employees

--grouping set clause
USE employee_db

CREATE TABLE EmployeeMaster
(
	id INT IDENTITY PRIMARY  KEY,
	EmployeeCode VARCHAR(10),
	EmployeeName VARCHAR(20),
	DepartmentCode VARCHAR(10),
	LocationCode VARCHAR(10),
	Salary INT
	);

INSERT INTO EmployeeMaster VALUES 
('E001','Hulk','IT','TVM',4000),
('E002','Spiderman','IT','TVM',4000),
('E003','Ironman','QA','KLM',3000),
('E004','Superman','QA','KLM',3000),
('E005','Batman','HR','TVM',5000),
('E006','Raju','HR','KTM',5000),
('E007','Radha','HR','KTM',5000)

SELECT EmployeeName FROM EmployeeMaster
GROUP BY EmployeeName

SELECT DepartmentCode,LocationCode,SUM(Salary) AS TotalCost FROM EmployeeMaster
	GROUP BY
		GROUPING SETS
		(
			
			(DepartmentCode),
			(LocationCode),()
		)
--comparison operators

SELECT * FROM EmployeeMaster
WHERE Salary <> 4000

SELECT * FROM EmployeeMaster
WHERE Salary = 4000

SELECT *FROM EmployeeMaster
WHERE Salary >4500
--not less than means that value and ABOVE
SELECT * FROM EmployeeMaster
WHERE Salary !<4000
--in means exactly
SELECT * FROM EmployeeMaster
WHERE Salary IN(3000,5000)

SELECT * FROM EmployeeMaster
WHERE Salary NOT IN (3000,4000)

SELECT * FROM EmployeeMaster
Where EmployeeName NOT IN('radha','raju')

SELECT * FROM EmployeeMaster
Where Salary IS NOT NULL

SELECT * FROM EmployeeMaster
WHERE Salary BETWEEN 3000 AND 4000 

SELECT * FROM EmployeeMaster
WHERE EmployeeName LIKE 'Raju'

SELECT * FROM EmployeeMaster
WHERE EmployeeName Like '%man'

SELECT * FROM EmployeeMaster 
WHERE EmployeeName LIKE '%MA%'

SELECT * FROM EmployeeMaster
WHERE EmployeeName  LIKE '%on%n'

--wildcard search
--with like operator
--[abc] would match on a,b orc characters

SELECT * FROM EmployeeMaster
WHERE EmployeeName LIKE 'S[^pi]%erman'

SELECT * FROM EmployeeMaster
WHERE EmployeeName LIKE '[^sibr]%'

--exist operator

SELECT * FROM EmployeeMaster
WHERE EXISTS
(SELECT * FROM EmployeeMaster WHERE EmployeeName LIKE 'Raju')


SELECT * FROM EmployeeMaster
WHERE EXISTS
(SELECT * FROM EmployeeMaster WHERE EmployeeName LIKE 'Ram')


CREATE TABLE EmployeeMaster2
(
	id INT IDENTITY PRIMARY  KEY,
	EmployeeCode VARCHAR(10),
	EmployeeName VARCHAR(20),
	DepartmentCode VARCHAR(10),
	LocationCode VARCHAR(10),
	Salary INT
	);

INSERT INTO EmployeeMaster2 VALUES 
('E001','Arun','IT','TVM',5000),
('E002','Varun','IT','TVM',4000),
('E003','Kiran','QA','KLM',3050),
('E004','Superman','QA','KLM',3000),
('E005','Midhun','HR','TVM',1000),
('E006','Singh','HR','KTM',6000),
('E007','Jyothi','HR','KTM',4000)

--union operator and union all
SELECT * FROM EmployeeMaster
UNION
SELECT * FROM EmployeeMaster2

SELECT * FROM EmployeeMaster
UNION ALL
SELECT * FROM EmployeeMaster2

SELECT * FROM EmployeeMaster
WHERE Salary > 3000
UNION
SELECT *  FROM EmployeeMaster2


SELECT * FROM EmployeeMaster
WHERE Salary >2000
INTERSECT
SELECT * FROM EmployeeMaster2

SELECT EmployeeName FROM EmployeeMaster
WHERE Salary >2000
INTERSECT
SELECT EmployeeName FROM EmployeeMaster2

--sample table to demonstrate popular data types

CREATE TABLE data_types_eg(
	bit_col BIT,
	char_col CHAR(3),
	date_col DATE,
	date_time_col DATETIME2,
	date_time_offset_col DATETIMEOFFSET(2),
	dec_col DECIMAL(4,2),
	num_col NUMERIC(4,2),
	bigint_col BIGINT,
	int_col INT,
	smallint_col SMALLINT,
	tinyint_col TINYINT,
	nchar_col NCHAR(10),
	time_col TIME(0),
	varchar_col VARCHAR(10)
)

INSERT INTO data_types_eg VALUES
	(1,'abc','1999-10-19','1999-10-19 11:23:23','1999-10-19 11:23:23 +5:20',10.23,10.36,944562318745,123554,4554,254,N'你好','12:47:50','helloooo') 

	SELECT * FROM data_types_eg