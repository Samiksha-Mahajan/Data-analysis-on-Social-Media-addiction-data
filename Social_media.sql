select * from social_media;

#select student id which are females 
select Student_ID  as female_Id from social_media  
where Gender = 'Female';

#select student id which are males 
select Student_ID as male_Id  from social_media 
where Gender = 'male';

#select count of undergraduate graduate and high school
SELECT Academic_Level, COUNT(*) AS Count
FROM social_media
GROUP BY Academic_Level;

#sum daily avg hours by gender
select Gender, sum(Avg_Daily_Usage_Hours) as Daily_Hours_use
FROM social_media
GROUP BY Gender;

#sum of avg hours by platform
select Most_Used_Platform, sum(Avg_Daily_Usage_Hours) as Daily_Hours_use
FROM social_media
GROUP BY Most_Used_Platform;

#select platform with is maximum addicted score
select Most_Used_Platform, Max(Addicted_Score)
FROM social_media
GROUP BY Most_Used_Platform;

#avg of mental health by gender
select Gender, avg(Mental_Health_Score)
from social_media
group by Gender;

#sum addicted score by gender
select Gender, sum(Addicted_Score)
from social_media
group by Gender;

#Select Student having addicted score is greater than equal to 5
select Student_ID, Addicted_Score
from social_media
where Addicted_Score >= 5;