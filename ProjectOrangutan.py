print("\n******************************************************************************\n")
print("Weather Branch\n")

# Import Libraries here
import random
from time import sleep

# Create A Function Randomly Choosing Weather from a list
def weather():
    weatherForecast = ["Snowing", "Blizzard", "Raining", "Foggy", "Windy", "Icy", "Sunny", "Cloudy"]
    currentWeather = random.choice(weatherForecast)
    return currentWeather

# Variable to call weather() once in our Vehicle Response System - VRS
weatherAlert = weather()

# VRS() will allow my vehicle to respond based on weather conditions
def vehicleResponseSystem():
    if weatherAlert == "Snowing":
        print("\nNational Weather Service has updated your alarm by 30 minutes because of the forecast of", weatherAlert)
        print("Vehicle Response System has been engaged only allowing you to drive 50 MPH.")

    elif weatherAlert == "Blizzard":
        print("\nNational Weather Service has updated your alarm by 45 minutes because of the forecast of", weatherAlert)
        print("Vehicle Response System has been engaged only allowing you to drive 30 MPH.")
    elif weatherAlert == "Raining":
        print("\nNational Weather Service has updated your alarm by 10 minutes because of the forecast of", weatherAlert)
        print("Vehicle Response System has been engaged only allowing you to drive 60 MPH.")
    elif weatherAlert == "Foggy":
        print("\nNational Weather Service has updated your alarm by 25 minutes because of the forecast of", weatherAlert)
        print("Vehicle Response System has been engaged only allowing you to drive 45 MPH.")
    elif weatherAlert == "Windy":
        print("\nNational Weather Service has updated your alarm by 5 minutes because of the forecast of", weatherAlert)
        print("Vehicle Response System has been engaged only allowing you to drive 65 MPH.")
    elif weatherAlert == "Icy":
        print("\nNational Weather Service has updated your alarm by 60 minutes because of the forecast of", weatherAlert)
        print("Vehicle Response System has been engaged only allowing you to drive 25 MPH.")
    elif weatherAlert == "Sunny":
        print("\nThe weather forecast is calling for a", weatherAlert, "day. Enjoy your drive to work!")
    else:
        print("\nThe weather forecast is calling for a", weatherAlert, "day. Enjoy your drive to work!")

vehicleResponseSystem()
