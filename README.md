# worldpop-global2-api
Code snippet to download WorldPop Global2 population density data in 100 m resolution for a user-defined list of countries.

Install "requests" package and you are ready to go.
In the beginning of the script, define the year of interest (2015-2030) and a list of iso3 country codes. 
The code will loop through the countries and download for each country the 100 m resolution population grid of the defined year.
