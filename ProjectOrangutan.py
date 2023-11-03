print("\n******************************************************************************\n")

print("Weather Branch\n")

# Import Libraries here
import random
from time import sleep

#Create A Function Randomly Choosing Weather from a list
def weather():
    weatherForecast = ["Snowing", "Blizzard", "Sprinkling", "Raining", "Foggy", "Windy", "Icy", "Sunny", "Cloudy"]
    currentWeather = random.choice(weatherForecast)
    return currentWeather
