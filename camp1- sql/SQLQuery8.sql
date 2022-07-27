-----------------SQL Time functions------------------

--to get the current timestamp
SELECT CURRENT_TIMESTAMP as DATE

--to get the current date time ( both these commands are same)
SELECT GETDATE() AS DATE

--time with more precision
SELECT SYSDATETIME() AS Date

-- to extract the part of the date day, month , or year
SELECT DATENAME(day, '2021/12/10') as Result1, DATENAME(month, '2021/12/10') AS  Result2,
DATENAME(year, '2021/12/10') AS Result3;

--To extract the part of the date as an integer value
SELECT DATEPART(day, '2021/12/10') AS result1,
DATEPART (month,'2021/12/10') AS Result2,
DATEPART (year, '2021/12/10') AS Result3;

-- To extract the part of the date day, month, or year as integers (alternate method)
SELECT YEAR('2021/12/10') AS Result1,
MONTH('2021/12/10') AS result2,
DAY('2021/12/10') AS result3;

-- to extract the difference of days, months, or years.
SELECT DATEDIFF(dd, '2020/2/3', '2021/3/5') as TotalDays,
DATEDIFF(MM, '2020/2/3', '2021/3/5') AS TotalMonths,
DATEDIFF(WK, '2020/2/3', '2021/3/5') AS TotalWeeks;
--there are more sql date functions to explore

--------------------SQL Mathematical Functions------------------

--returns square root
SELECT SQRT(25) AS Result1;

--returns absolute value
SELECT ABS(-20) AS Result1;

--returns next highest integer value 
SELECT CEILING(22.19) AS RESULT1

--return next lowest integer value
SELECT FLOOR(22.19) AS RESULT1

--to returna random value
SELECT RAND(1501) AS Result1;

--return the powers
SELECT POWER(3,2) AS Result2;

--returns natural logarithm
SELECT LOG(20) AS Result1;

--return sign (as 1 or -1)
SELECT SIGN(22) AS Result;
 
--more functions can be explored at SQL mathematical functions


-----------------------------SQL Conversion Functions-------------------------
----------syntax is CONVERT(data_type, expr, length)

--convert the expression to int
SELECT CONVERT(int,30.55);

--converts string expression to datetime
SELECT CONVERT(datetime, '2022-08-25');

--convert to varchar of length 100
SELECT CONVERT(varchar, '2020-08-25',101);


-----------------------------SQL Server cast Functions---------------------
--------syntax : CAST(expression AS datatype(length))-----------------------
-----------------Convert is sql specific, CAST is ansi-------------------------

-- convert expression to varchar
SELECT CAST(20.65 AS VARCHAR);

--converts a value to a datetime datatype:
SELECT CAST('2020-08-25' AS datetime);

------------------------------------------
-----------------SQL joins----------------
------------------------------------------

--create dummy database and tables for testing
CREATE DATABASE training
USE training

--Create tables trainee, fee, semester
CREATE TABLE trainee (
id int PRIMARY KEY IDENTITY, 
admission_no VARCHAR(45) NOT NULL,
first_name VARCHAR(45) NOT NULL,
last_name VARCHAR(45) NOT NULL,
age int,
city VARCHAR(25) NOT NULL);

CREATE TABLE fee (
admission_no VARCHAR(45) NOT NULL,
sem_no int NOT NULL,
course VARCHAR(45) NOT NULL,
amount int,
);

CREATE TABLE semester (
sem_no int NOT NULL,
sem_name varchar(10),
);
 
INSERT INTO trainee (admission_no, first_name, last_name, 
age,city) 
VALUES (3354,'Spider', 'Man', 13, 'Texas'), 
(2135, 'James', 'Bond', 15, 'Alaska'), 
(4321, 'Jack', 'Sparrow', 14, 'California'), 
(4213,'John', 'McClane', 17, 'New York'), 
(5112, 'Optimus', 'Prime', 16, 'Florida'), 
(6113, 'Captain', 'Kirk', 15, 'Arizona'), 
(7555,'Harry', 'Potter', 14, 'New York'), 
(8345, 'Rose', 'Dawson', 13, 'California'); 

INSERT INTO semester (sem_no, sem_name) 
VALUES 
(1,'First Sem'), 
(2, 'Second Sem'), 
(3, 'Third Sem'), 
(4, 'Fourth Sem');

INSERT INTO fee (admission_no, sem_no, course, amount) 
VALUES (3354, 1, 'Java', 20000), 
(7555, 1, 'Android', 22000), 
(4321, 2, 'Python', 18000), 
(8345, 2, 'SQL', 15000), 
(9345, 2, 'Blockchain', 16000),
(9321, 3, 'Ethical Hacking', 17000), 
(5112, 1, 'Machine Learning', 30000); 

-------------sql inner joins ------------------
----syntax: SELECT colums from table1 INNER JOIN table2 ON condition1 INNER  JOIN table3 ON condition2-------------------

--inner joining with two tables
SELECT trainee.admission_no, trainee.first_name,
trainee.last_name, fee.course, fee.amount FROM trainee
INNER JOIN fee ON trainee.admission_no = fee.admission_no;

--inner joining with three tables
SELECT trainee.admission_no, trainee.first_name, trainee.last_name, 
fee.course, fee.amount, semester.sem_name FROM trainee
INNER JOIN fee ON trainee.admission_no = fee.admission_no
INNER JOIN semester ON semester.sem_no = fee.sem_no;

---------------------------LEFT JOIN--------------------------
--------(returns all records from the left table even if there are no matches in the right table---------------
SELECT trainee.admission_no, trainee.first_name, 
trainee.last_name, fee.course, fee.amount
FROM trainee
LEFT OUTER JOIN fee ON trainee.admission_no = fee.admission_no;

----------------------------RIGHT OUTER JOIN----------------------
----------(returns all records from the right table(fee), even if there are no matches in the left table(trainees)
SELECT trainee.admission_no, trainee.first_name, trainee.last_name, fee.course, fee.amount
FROM trainee
RIGHT OUTER JOIN fee ON trainee.admission_no = fee.admission_no;

------------FULL OUTER JOIN / FULL JOIN (both are the same)--------------------------
SELECT trainee.admission_no, trainee.first_name, trainee.last_name, fee.course, fee.amount FROM trainee
FULL OUTER JOIN fee ON trainee.admission_no = fee.admission_no;

--------------------------------SELF JOIN---------------------------------------
----------------(a copy of the same table is used for joining)-------------------
SELECT t1.first_name, t1.last_name, t2.city FROM trainee t1, trainee t2
WHERE t1.admission_no = t2.admission_no
AND t1.city = t2.city
ORDER BY t2.city ;

-- Give repeating list of cities 
SELECT t1.first_name, t1.last_name, t2.city FROM trainee t1, trainee t2 WHERE t1.admission_no != t2.admission_no
AND t1.city = t2.city ORDER BY t2.city;

--cross join
SELECT * FROM trainee CROSS JOIN fee;

--combining croos join with where clause equivalent to inner join 
SELECT * from trainee CROSS JOIN fee 
WHERE trainee.admission_no = fee.admission_no
USE training

-------------------Stored Procedures-------------------
--Creating a stored procedure 
CREATE PROCEDURE trainingAgewiseList 
AS BEGIN
	SELECT first_name,age,city 
	FROM trainee ORDER BY age;
END;

--Execute Stored procedure
EXEC trainingAgewiseList

--changing stored procedure
ALTER PROCEDURE trainingAgewiseList
AS BEGIN 
SELECT first_name, last_name,age,city FROM trainee ORDER BY age;
END;
EXEC trainingAgewiseList

--deleting a stored procedure
DROP PROCEDURE trainingAgewiseList

--passing parameters into stored procedure
CREATE PROCEDURE getTraineesFromCity(@city VARCHAR(50)) 
AS BEGIN 
	SET NOCOUNT ON; --to hide the rows modified message 
	SELECT first_name, last_name, age, city
	FROM trainee
	WHERE city = @city
END

--Execute the procedure by passing the parameter
EXEC getTraineesFromCity 'texas'

--Return parameter from stored procedure 
CREATE PROCEDURE getTraineeCount (@traineeCount INT OUTPUT)
AS
BEGIN
SELECT @traineeCount = COUNT(id) FROM trainee;
END;

--recieving output from stored procedure 
--step1 declare the variable to hold the output 
DECLARE @TraineeCount INT 
--Step2 is executing the stored procedure
EXEC getTraineeCount @TraineeCount OUTPUT  
--step3 print the output variable 
PRINT @TraineeCount

----------------SUBQUERIES IN SQL--------------------
SELECT * FROM trainee 
WHERE id IN (SELECT id FROM trainee WHERE age<20);

DELETE 
FROM trainee
WHERE admission_no IN 
(SELECT admission_no FROM
trainee WHERE admission_no = 3354);

---------------------VIEWS IN SQL------------------
--Creating the view
CREATE VIEW [ny trainees] AS 
SELECT first_name, last_name, city FROM
trainee WHERE CITY = 'New York';

--Query the view
SELECT * FROM [ny trainees]

--------------------Triggers-------------------------

--creating a DDL trigger ( for events of create, alter, drop )
CREATE TRIGGER dont_play_withmydb
ON DATABASE FOR create_table, alter_table, drop_table --ON db for events
AS --trigger execution statements
PRINT 'NOT ALLOWED !! IN MY DB'
rollback; --roll back to previous state 

--Testing the trigger 
CREATE TABLE testTable(
id int);

--delete the trigger 
DROP TRIGGER dont_play_withmydb ON DATABASE

--Creating a dml trigger( for events of insert, update,delete)
use training;
CREATE TRIGGER msg_afte_insert
 ON trainee 
 AFTER INSERT AS 
 BEGIN PRINT 'insert fine' 
 END

 --Testing the dml trigger 
 INSERT INTO trainee (admission_no, first_name, last_name, 
age,city) 
VALUES (3354,'Spider', 'Man', 13, 'Texas');

--testing the drop trigger 
DROP TRIGGER msg_after_insert

--creating the trainee backup table
CREATE TABLE trainee_backup(
id int PRIMARY KEY IDENTITY,
admission_no VARCHAR(45) NOT NULL,
first_name VARCHAR(45) NOT NULL,
last_name VARCHAR(45) NOT NULL, 
age INT , 
city  VARCHAR (25) NOT NULL
);

--Create an  AFTER Trigger which can backup  data to other table 
CREATE TRIGGER  backup_trainees 
ON trainee 
AFTER INSERT 
AS 
BEGIN 
	SET NOCOUNT ON;	-- To suppress the number of affectd rows message
	--Declaring variables to hold the values temporarily
	DECLARE @id INT 
	DECLARE @admission_no INT
	DECLARE @age INT
	DECLARE @first_name VARCHAR (45) 
	DECLARE @last_name VARCHAR(45)
	DECLARE @city VARCHAR(45)

	SELECT  @id= I.id,
	@first_name = I.first_name,
	@last_name = I.last_name,
	@age = I.age,
	@admission_no = I.admission_no,
	@city = I.city
	FROM INSERTED I
	INSERT INTO trainee_backup VALUES(@id, @admission_no, @first_name, @age, @city)
	PRINT ('Values inserted into both trainee and backup tables'
END

 --Testing the dml trigger 
 INSERT INTO trainee(admission_no, first_name, last_name, 
age,city) 
VALUES (3354,'Spider', 'Man', 13, 'Texas');

SELECT * FROM trainee
SELECT * FROM trainee_backup

--Instead Trigger
CREATE TRIGGER do_insteadof_insert ON trainee
INSTEAD OF INSERT AS 
BEGIN 
PRINT 'Values are not inserted because of a trigger'
END

 --Testing the dml trigger 
 INSERT INTO trainee (admission_no, first_name, last_name, 
age,city) 
VALUES (3354,'Spider', 'Man', 13, 'Texas');

------------SQL TRANSACTIONS--------------------------

--Start a new transaction
BEGIN TRANSACTION 

--SQL Statements to execute one by one 
INSERT INTO semester (sem_no, sem_name) VALUES (5,'sem5')
UPDATE semester SET sem_name = 's5' WHERE sem_no = 5 --query 2
 
--Commit changes and the transaction
COMMIT TRANSACTION

--Manually rollling back the transaction
--Starting a transaction 
BEGIN TRANSACTION
INSERT INTO semester (sem_no, sem_name) VALUES (5,'sem5')
UPDATE semester SET sem_name = 's6' WHERE sem_no = 5 --query 2
ROLLBACK TRANSACTION 

SELECT * FROM semester

BEGIN TRANSACTION 
INSERT INTO semester (sem_no, sem_name) VALUES (6,'sem 6')
SELECT * FROM semester
UPDATE semester SET sem_no = 'six' WHERE sem_no = 6 

--Check for error using system variable @@ERROR
IF (@@ERROR >0)
	BEGIN 
		ROLLBACK TRANSACTION
	END
ELSE
	BEGIN 
		COMMIT TRANSACTION 
	END

BEGIN TRANSACTION 
INSERT INTO semester (sem_no, sem_name) VALUES (6,'sem 6')
SELECT * FROM semester
UPDATE semester SET sem_no = 'six' WHERE sem_no = 6 

--will try to commit the transaction, if fails, will autp,atically rollback 
COMMIT TRANSACTION	
