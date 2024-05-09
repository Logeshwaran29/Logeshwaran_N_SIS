use SISDB;

--1
insert into Students values('John','Doe','1995-08-15','john.doe@example.com',1234567890);
select * from Students;

--2
insert into Enrollments values(11, 7, '2024-05-01');
select * from Enrollments;

--3
update Teacher set email='evelyn@example.com' where teacher_id=3;
select * from Teacher;

--4
delete from Enrollments where student_id=1 and course_id=2;
select * from Enrollments;

--5
update Courses set teacher_id = 10 where course_id=10;
select * from Courses;

--6
delete from Students where student_id = 11;
select * from Students;

--7
update Payments set amount= 68000 where payment_id=10;
select * from Payments;


