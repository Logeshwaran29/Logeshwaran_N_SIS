use SISDB;
select * from Students;
select * from Courses;
select * from Enrollments;
select * from Payments;
select * from Teacher;

--1
select course_id, avg(count_stu) as 'Avg_stu' from (
select course_id, count(student_id) as 'count_stu' from Enrollments group by course_id) s
group by course_id;

--2
select s.student_id, first_name, last_name, amount from Students s join Payments p on s.student_id = p.student_id
where p.amount = (select max(amount) from Payments);


--3
select course_id, count(student_id) from Enrollments 
group by course_id
having count(student_id) = (
select max(count) from (
select course_id, count(student_id) as 'count' from Enrollments group by course_id) as s)

--4
select t.*, s2.sum as 'Total amt' from Teacher t join (
select teacher_id, s1.sum from Courses c join (
select c.course_id, s.sum from Courses c join (
select sum(amount) as 'sum', e.course_id from Payments p join Enrollments e on p.student_id = e.student_id
group by e.course_id) as s on c.course_id = s.course_id) as s1 on c.course_id = s1.course_id ) as s2 on t.teacher_id = s2.teacher_id;

--5
select * from Students where student_id = any (
select student_id from Enrollments
group by student_id
having count(course_id) = (select count(course_id) from Courses));

--6
select * from Teacher where teacher_id not in(
select teacher_id from Courses)

--7
select avg(age) as 'AVG_AGE' from (
select student_id, DATEDIFF(YEAR, date_of_birth, GETDATE()) as 'age' from Students) as s

--8
select course_id, course_name from Courses where course_id not in (
select course_id from Enrollments)

--9
select student_id, course_id, (select sum(amount) from Payments p where p.student_id = e.student_id) as total_payments
from Enrollments e
group by student_id, course_id;

--10
select * from (
select student_id, count(amount) as 'count_payment' from Payments group by student_id) as s
where count_payment > 1;

--11 
select student_id, sum(amount) from (
select s.student_id, amount from Students s join Payments p on s.student_id = p.student_id ) as t 
group by student_id;

--12
select course_name, count(student_id) as 'Count_of_Students' from Courses c join(
select c.course_id, student_id from Courses c join Enrollments e on c.course_id = e.course_id) as c1
on c.course_id = c1.course_id
group by c.course_id, course_name

--13
select s.student_id,first_name, last_name, avg(amount) from (
select s.*, amount from Students s join Payments p on s.student_id = p.student_id) as s
group by s.student_id, first_name, last_name

