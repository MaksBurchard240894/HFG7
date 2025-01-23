select discharge_disposition_id, admission_type_id, count(*) from encounter
group by discharge_disposition_id, admission_type_id
order by count desc;

select discharge_disposition_id, readmitted, count(*) from encounter
group by discharge_disposition_id, readmitted
order by count desc;