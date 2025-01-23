select COUNT(*) from encounter

select encounter.admission_type_id, COUNT(*) as count from encounter
group by admission_type_id
order by count desc;

select encounter.discharge_disposition_id, COUNT(*) as count from encounter
group by discharge_disposition_id
order by count desc;