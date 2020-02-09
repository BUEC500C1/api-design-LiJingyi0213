import requests
import csv 
from pprint import pprint
airports_dic={}

def airportWeather(Airport_name):
  filename = "airports.csv"
  with open(filename, 'r') as csvfile: 
     csvreader = csv.reader(csvfile) 
     for row in csvreader:
        airports_dic[row[3]]=(row[10],row[8])
        # print(row[3],row[8],row[10])

  i,j=airports_dic[Airport_name]
  r = requests.get('https://openweathermap.org/data/2.5/weather?q={},{}&appid=b6907d289e10d714a6e88b30761fae22'.format(i,j)).json()
  pprint(r)

def main ():
  airportWeather("Lindu Airport")

if __name__ == '__main__':
  main()