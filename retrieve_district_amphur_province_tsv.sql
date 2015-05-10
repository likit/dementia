use Provinces;
select DISTRICT_NAME, AMPHUR_NAME from district inner join amphur using (AMPHUR_ID);
