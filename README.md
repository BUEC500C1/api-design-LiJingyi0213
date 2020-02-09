# api-design-LiJingyi0213
## Introduction
Using OpenWeatherAPI to created an API. The function of this API is that enter the airport name to get the current weather conditions at the airport.

## Target Users
- Traveler
- City dweller
- Airport staff

## User Stories
- I, a traveler, want to know the current weather conditions at the airport to predict if I need change my flight.
- I, a city dweller, want to know the current weather conditions in the city where I live.
- I, an airport staff, want to know the current weather of the airport to deal with emergency that might happen.

## Steps
- First, we need sign up in OpenWeather to find the website address in the API documents of current weather data and get the key of API.
- Download the information of US airports to terminal from http://ourairports.com/data/airports.csv, it includes temperature, weather, latitude and longitude, humidity and other information.
- Run airport_api.py
- Test this python file.
- Enter an airport name, then we can get the information of this airport.

## Project Demo
Enter airport name(for example:Lindu Airport)

Results:

![](https://github.com/BUEC500C1/api-design-LiJingyi0213/blob/master/270e2421a98ebf794a4c14151fff11b.png)

Test Results:

![](https://github.com/BUEC500C1/api-design-LiJingyi0213/blob/master/7a0d44b32495696cc14a660cfc7ce8c.png)

## Pros and Cons
- pros: This code can recognize all the letters of the airports' names no matter if it is lowercase of uppercase.
- cons: This code just can get current weather conditions.
