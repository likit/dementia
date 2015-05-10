use Provinces;
select AMPHUR_NAME, PROVINCE_NAME from amphur inner join province using (PROVINCE_ID);
