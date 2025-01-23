select count(*) from diabetic_data

select diabetic_data.race, COUNT(*) as count from diabetic_data
group by race
order by count desc;

select diabetic_data.weight, COUNT(*) as count from diabetic_data
group by weight
order by count desc;