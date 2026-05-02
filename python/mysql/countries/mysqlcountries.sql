# To get this loaded, we created new database. Imported SQL file world, and then ran the file to allow it
# to be populated with the values per the provided SQL file. Tested to make sure information was available.
# Then started querying below as necessary.
# SELECT * FROM cities;
# SELECT * FROM countries;
# SELECT * FROM languages;

#1 Query to get all countries that speak Slovene - return name, language, lang% in desc
SELECT countries.name, languages.language, languages.percentage FROM countries
JOIN languages ON countries.code = languages.country_code WHERE languages.language="Slovene" 
ORDER BY languages.percentage DESC;

#2 (3) Query to display total cities per country - return name, total cities, desc
# Likely have to look at outside documentation (will help w/ 8)
SELECT countries.name, COUNT(cities.country_id) AS city_count FROM countries
JOIN CITIES ON countries.id = cities.country_id GROUP BY countries.name 
ORDER BY COUNT(cities.country_id) DESC;

#3 Query to get all cities in Mexico w/ pop > 500K, return in desc by population
SELECT cities.name, cities.population, cities.country_id FROM countries
JOIN cities ON countries.id = cities.country_id WHERE countries.name = "Mexico"
ORDER BY cities.population DESC;

#4 Query to get all langs in country w/ %>89 - return by % in desc (similar to 1)
SELECT countries.name, languages.language, languages.percentage FROM countries
JOIN languages ON countries.id = languages.country_id WHERE languages.percentage > 89
ORDER BY languages.percentage DESC;

#5 (2) Query to get all countries w/ SA<501 and pop>100K
SELECT * FROM countries WHERE countries.surface_area < 501 AND countries.population > 100000;

#6 Query to get countries w/ constmonarchy w/ cap>200 LE>75
SELECT * FROM countries WHERE countries.government_form = "Constitutional Monarchy"
AND countries.capital > 200 AND countries.life_expectancy > 75;

#7 (2) Query to get all Argentina cities inside BA dist w/ pop>500K - return count/cit name, dist, population
SELECT countries.name AS country_name, cities.name AS city_name, cities.district, cities.population FROM countries
JOIN cities ON countries.id = cities.country_id WHERE countries.name = "Argentina"
AND cities.district = "Buenos Aires" AND cities.population > 500000;

#8 (2) Query to summarize # countries per region - return region name and # of countries in desc
SELECT region, COUNT(id) FROM countries GROUP BY region ORDER BY COUNT(id) DESC;