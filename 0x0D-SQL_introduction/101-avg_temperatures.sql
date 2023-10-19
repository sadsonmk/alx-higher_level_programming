-- displays the average temperature (Fahrenheit) by city ordered by temperature (descending)
mysql -hlocalhost -uroot -p hbtn_0c_0 < temperatures.sql
SELECT AVG(temperature) as 'avg_temp'
