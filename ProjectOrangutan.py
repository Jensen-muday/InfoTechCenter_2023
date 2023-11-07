

"""
Our welcome screen will start our program letting
drivers know that the InfoTech Center 2023 is loading
"""

# Import Libraries Here
import time
import sys
import random
from time import sleep

time_to_sleep = 2

print("\n\nwelcome to our InfoTech center 2023\n")
time.sleep(time_to_sleep)

# Add code to have the ellipsis add a dot every 0.5 seconds
x = 0
ellipsis = 0

while x != 20:
    x += 1
    message = ("InfoTech Center 2023 is loading" + "." * ellipsis)
    ellipsis = ellipsis + 1
    sys.stdout.write("\r" + message) # \r prints a carriage return first, so, message is printed on top of the previous line
    time.sleep(.5)
    if ellipsis == 4:
        ellipsis = 0
    if x == 20:
        print("\n\nOperating system Loaded - Retina Scanned - Access Granted")

print("\n************************************************************************************************************\n")
print("Checking current gasoline level\n\n")
sleep(1)


# Function that lists Gas Stations, randomly choosing one, and Return its value
def gasLevelGauge():
      gasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
      currentGasLevel = random.choice(gasLevelList)
      return currentGasLevel

# Function with list of GasStations
def listOfGasStations():
      gasStations = ["Shell", "Speedway", "Exxon", "Meijer", "Costco", "Marathon", "BP", "Circle K", "Wesco"]
      gasStationsNearby = random.choice(gasStations)
      return gasStationsNearby

# Function will call the gas level gauge to determine gasLevelGauge, and then find a close gas station if low
def gasLevelAlert():
      milesToGasStationLow = round(random.uniform(1, 25), 1)
      milesToGasStationQuarterTank = round(random.uniform(25.1, 50), 1)
      gasLevelIndicator = gasLevelGauge()
      if gasLevelIndicator  == "Empty":
            print("***WARNING - YOU ARE ON EMPTY***")
            sleep(1.25)
            print("Calling Triple AAA")
      elif gasLevelIndicator == "Low":
            print("Your gas tank is extremely low, checking Google maps for the closest gas station.")
            sleep(1.5)
            print("The closest gas station is", listOfGasStations(), "which is", milesToGasStationLow, "miles away.")
      elif gasLevelIndicator == "Quarter Tank":
            print("You have a Quarter Tank of gasoline, checking Google maps for the closest gas station.")
            sleep(1.5)
            print("The closest gas station is", listOfGasStations(), "which is", milesToGasStationQuarterTank, "miles away.")
      elif gasLevelIndicator == "Half Tank":
            print("You have a Half Tank of gasoline, which is enough for your current destination.")

      elif gasLevelIndicator == "Three Quarter Tank":
            print("You have Three Quarter's of your tank full.")
      else:
            print("Your Gas Tank is full!")



gasLevelAlert()
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
