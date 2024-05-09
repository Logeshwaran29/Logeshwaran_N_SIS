create database SISDB;
use SISDB;

create table Students (
student_id int primary key identity(1,1),
first_name varchar(50),
last_name varchar(50),
date_of_birth date,
email varchar(50) constraint ck check(email like '%@example.com'),
phone_number varchar(10)
);

create table Teacher (
teacher_id int primary key identity(1,1),
first_name varchar(50),
last_name varchar(50),
email varchar(50) constraint ck1 check(email like '%@example.com')
);

create table Courses (
course_id int primary key identity(1,1),
course_name varchar(100),
credits int,
teacher_id int references Teacher(teacher_id) on delete cascade
);

create table Enrollments (
enrollment_id int primary key identity(1,1),
student_id int references Students(student_id) on delete cascade,
course_id int references Courses(course_id) on delete cascade,
enrollment_date date
);

create table Payments (
payment_id int primary key identity(1,1),
student_id int references Students(student_id) on delete cascade,
amount decimal(10,2),
payment_date date
);

insert into Students values('James','Anderson','2000-01-20','james.anderson@example.com',9988776655),
('Ethan','Hunt','1999-02-02','ethan.hunt@example.com',9876543210),
('Corey','Graves','2000-03-23','corey.graves@example.com',9988776644),
('John','Cena','2001-04-27','john.cena@example.com',9988772255),
('Paul','Anderson','1998-05-25','paul.anderson@example.com',9988336655),
('Madison','Thomas','2000-06-11','madison.thomas@example.com',9911776655),
('Mia', 'Wilson','1999-07-14','mia.wilson@example.com',9483726150),
('Benjamin', 'Taylor','2000-08-18','benjamin.taylor@example.com',9984636251),
('Emma','Watson','2001-09-19','emma.watspn@example.com',9984576004),
('Jackson','Storm','1998-11-03','jackson.strom@example.com',9988740550);

select * from Students;

insert into Teacher values
('Liam', 'Lewis', 'liam.lewis@example.com'),
('Avery', 'Roberts', 'avery.roberts@example.com'),
('Evelyn', 'Turner', 'evelyn.turner@example.com'),
('Lucas', 'Phillips', 'lucas.phillips@example.com'),
('Harper', 'Campbell', 'harper.campbell@example.com'),
('Aiden', 'Parker', 'aiden.parker@example.com'),
('Sofia', 'Evans', 'sofia.evans@example.com'),
('Jackson', 'Edwards', 'jackson.edwards@example.com'),
('Charlotte', 'Collins', 'charlotte.collins@example.com'),
('Mason', 'Bennett', 'mason.bennett@example.com');

select * from Teacher;

insert into Courses values
('Introduction to SQL', 3, 1),
('Software Testing', 3, 2),
('Data Analysis', 3, 3),
('Web Development', 4, 4),
('Software Engineering', 4, 5),
('Computer Science Fundamentals', 3, 6),
('Network Security', 4, 7),
('Artificial Intelligence', 3, 8),
('Problem Solving Techniques', 4, 9),
('Data Structures and Algorithms', 4, 9);

select * from Courses;

insert into Enrollments values
(1, 1, '2024-01-01'),
(1, 2, '2024-01-11'),
(2, 3, '2024-02-21'),
(3, 4, '2024-04-25'),
(5, 5, '2024-02-10'),
(5, 6, '2024-02-09'),
(6, 7, '2024-03-11'),
(9, 8, '2024-01-15'),
(8, 9, '2024-03-29'),
(4, 10, '2024-04-05');

select * from Enrollments;

insert into Payments values
(1, 77000.00, '2024-01-11'),
(1, 75000.00, '2024-01-16'),
(2, 87000.00, '2024-03-10'),
(3, 65000.00, '2024-05-05'),
(5, 90000.00, '2024-02-22'),
(5, 80000.00, '2024-02-28'),
(6, 70000.00, '2024-04-02'),
(9, 71000.00, '2024-01-25'),
(8, 95000.00, '2024-04-09'),
(4, 60000.00, '2024-04-30');

select * from Payments;