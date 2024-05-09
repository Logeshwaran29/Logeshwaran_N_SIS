use SISDB;
select * from Students;
select * from Enrollments;
select * from Courses;
select * from Payments;
select * from Teacher;

update Enrollments set course_id = 7 where enrollment_id = 10;

--1
select s.student_id, first_name, last_name,sum(amount) as 'Total Payment' from Students s join Payments p on s.student_id = p.student_id
where s.student_id = 5
group by s.student_id, first_name, last_name;

--2
select c.course_id , c.course_name, count(student_id) as 'No.of.students' from Enrollments e join Courses c on c.course_id = e.course_id
group by c.course_id ,c.course_name;

--3
select s.student_id, concat(first_name,' ',last_name) as 'Student Name' 
from Students s left join Enrollments e on s.student_id = e.student_id
where e.student_id is null;

--4
select first_name, last_name, course_name from Students s join Enrollments e on s.student_id = e.student_id
join Courses c on e.course_id = c.course_id;

--5
select concat(first_name,' ',last_name) as 'Teacher Name', course_name from Teacher t join Courses c on t.teacher_id = c.teacher_id;

--6
select first_name, last_name, enrollment_date from Students s join Enrollments e on s.student_id = e.student_id
join Courses c on e.course_id = c.course_id
where c.course_name = 'Network Security';

--7
select s.student_id, CONCAT(first_name,' ',last_name) as 'Student Name' 
from Students s left join Payments p on s.student_id = p.student_id
where p.payment_id is null;

--8
select c.course_id, c.course_name from Courses c left join Enrollments e on c.course_id = e.course_id
where e.enrollment_id is null;

--9
select e.student_id from Enrollments e join Enrollments e1 on e.student_id = e1.student_id
group by e.student_id
having COUNT(e.student_id) > 1;

--10
insert into Teacher values('Adam','Cole','adam.cole@example.com')

select * from Teacher t left join Courses c on t.teacher_id = c.teacher_id
where c.teacher_id is null;
