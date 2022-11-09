COPY vehicles(track_id, vehicle_type, traveled_d, avg_speed, lat, lon, speed, loan_acc, lat_acc, timer)
FROM './20181024_d1_0830_0900.csv'
DELIMITER ','
CSV HEADER;