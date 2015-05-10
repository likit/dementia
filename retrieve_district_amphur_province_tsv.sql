use Provinces;
-- select DISTRICT_NAME, AMPHUR_NAME from district inner join amphur using (AMPHUR_ID);
select DISTRICT_NAME, AMPHUR_NAME, PROVINCE_NAME from district
    inner join amphur on district.AMPHUR_ID = amphur.AMPHUR_ID
    join province on district.PROVINCE_ID = province.PROVINCE_ID;
