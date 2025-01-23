select avg(time_in_hospital), admission_type_id, count(*) from encounter
group by admission_type_id
order by count desc;

select readmitted, admission_type_id, count(*) from encounter
group by admission_type_id, readmitted
order by count desc;
