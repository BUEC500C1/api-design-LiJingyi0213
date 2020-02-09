import pytest
from airport_api import airportWeather

def test():
  assert "message" not in airportWeather("Total Rf Heliport")
  assert "message" not in airportWeather("total rf heliport")
  assert "message" not in airportWeather("Aero B Ranch Airport") 
  assert "message" not in airportWeather("Newport Hospital & Clinic Heliport")