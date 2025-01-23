select count(*) from encounter

select encounter.admission_source_id, COUNT(*) as count from encounter
group by admission_source_id
order by count desc;

select admission_source_id, admission_type_id, COUNT(*) as count from encounter
group by admission_source_id, admission_type_id
order by count desc;