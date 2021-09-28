create database KrishiNetwork;

use KrishiNetwork;

-- create table and assign column name and data type 

create table app_launches(user_id  int, time_stamp datetime);

desc app_launches;

-- Let take a test case of 5 users 
-- user Id are   101, 102,103,104,105
 -- time frame july 2021 to aug 2021
 
insert into app_launches values(101,'2021-07-01 11-15-56');
insert into app_launches values(101,'2021-07-01 13-30-56');
insert into app_launches values(101,'2021-07-02 18-30-56');
insert into app_launches values(101,'2021-07-02 20-30-56');
insert into app_launches values(101,'2021-07-24 10-30-56');
insert into app_launches values(101,'2021-07-24 15-30-56');
insert into app_launches values(101,'2021-07-24 22-30-56');

insert into app_launches values(102,'2021-07-02 10-30-56');
insert into app_launches values(102,'2021-07-02 21-30-56');
insert into app_launches values(102,'2021-07-01 12-30-56');
insert into app_launches values(102,'2021-07-01 13-20-56');
insert into app_launches values(102,'2021-07-16 11-30-56');
insert into app_launches values(102,'2021-07-18 11-30-56');
insert into app_launches values(102,'2021-07-14 11-30-56');
insert into app_launches values(102,'2021-07-25 11-30-56');

insert into app_launches values(103,'2021-07-01 14-30-56');
insert into app_launches values(103,'2021-07-04 13-30-56');
insert into app_launches values(102,'2021-07-04 18-30-56');
insert into app_launches values(103,'2021-07-15 11-30-56');
insert into app_launches values(103,'2021-07-15 20-30-56');

insert into app_launches values(104,'2021-07-03 11-30-56');
insert into app_launches values(104,'2021-07-03 15-30-56');
insert into app_launches values(104,'2021-07-06 11-30-56');
insert into app_launches values(104,'2021-07-20 15-30-56');
insert into app_launches values(104,'2021-07-24 14-30-56');
insert into app_launches values(104,'2021-07-25  16-30-56');

insert into app_launches values(105,'2021-07-01 11-30-56');
insert into app_launches values(105,'2021-07-01 08-30-56');
insert into app_launches values(105,'2021-07-01 15-30-56');
insert into app_launches values(105,'2021-07-15  11-30-56');
insert into app_launches values(105,'2021-07-24 16-30-56');
insert into app_launches values(105,'2021-07-28 15-30-56');
insert into app_launches values(105,'2021-07-230 11-30-56');

-- aug data 
insert into app_launches values(101,'2021-08-01 11-15-56');
insert into app_launches values(101,'2021-08-01 13-30-56');
insert into app_launches values(101,'2021-08-02 18-30-56');
insert into app_launches values(101,'2021-08-02 20-30-56');
insert into app_launches values(101,'2021-08-24 10-30-56');
insert into app_launches values(101,'2021-10-24 15-30-56');
insert into app_launches values(101,'2021-10-24 22-30-56');

insert into app_launches values(102,'2021-08-02 10-30-56');
insert into app_launches values(102,'2021-08-02 21-30-56');
insert into app_launches values(102,'2021-08-01 12-30-56');
insert into app_launches values(102,'2021-08-01 13-20-56');
insert into app_launches values(102,'2021-10-16 11-30-56');
insert into app_launches values(102,'2021-10-18 11-30-56');
insert into app_launches values(102,'2021-11-14 11-30-56');
insert into app_launches values(102,'2021-11-25 11-30-56');

insert into app_launches values(103,'2021-08-01 14-30-56');
insert into app_launches values(103,'2021-08-04 13-30-56');
insert into app_launches values(102,'2021-08-04 18-30-56');
insert into app_launches values(103,'2021-08-15 11-30-56');
insert into app_launches values(103,'2021-09-15 20-30-56');

insert into app_launches values(104,'2021-08-03 11-30-56');
insert into app_launches values(104,'2021-08-03 15-30-56');
insert into app_launches values(104,'2021-09-06 11-30-56');
insert into app_launches values(104,'2021-09-20 15-30-56');
insert into app_launches values(104,'2021-08-24 14-30-56');
insert into app_launches values(104,'2021-08-25  16-30-56');

insert into app_launches values(105,'2021-08-01 11-30-56');
insert into app_launches values(105,'2021-08-01 08-30-56');
insert into app_launches values(105,'2021-08-01 15-30-56');
insert into app_launches values(105,'2021-08-15  11-30-56');
insert into app_launches values(105,'2021-09-24 16-30-56');
insert into app_launches values(105,'2021-08-28 15-30-56');
insert into app_launches values(105,'2021-08-230 11-30-56');



select * from app_launches;

-- Question 1 - Find out count of daily active users against each data in July, 2021 
-- Output should have two columns - date & count of active users on the date

select   date(time_stamp) as Days,  count(distinct user_id) as Active_Users   from app_launches  Group By date(time_stamp);




-- Question 2 - What percent of total users use the application on their day 2? 
-- Day 2 here means a day after a user installs the application. For example 
-- if you installed the application on 5th September then 5th September is considered day 1 for you. 
-- 6th September is considered day 2 for you. So each user will have his own day 1, day 2 and so on, 
-- based on what date he installed the application. You need to write query(s) for calculating - 
-- What percent of total users use the application on their day 2?

select * from app_launches;

drop table if exists time_tab;

create temporary  table time_tab
SELECT a1.user_id ,a1.time_stamp, (DATEDIFF(a1.time_stamp, a2.time_stamp)) as Difference
from app_launches as a1  
inner join app_launches as a2 
on a2.user_id = a1.user_id+1
-- group by Difference
;

select * from time_tab
where Difference =1 or Difference =-1;





select distinct user_id from app_launches;


-- drop table app_launches;