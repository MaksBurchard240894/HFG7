select count(*) from diabetic_data

select diabetic_data.age, COUNT(*) as count from diabetic_data
group by age
order by count desc;