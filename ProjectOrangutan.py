print("***************************")
print("Gasoline Branch\n\n")

# Import Libraries Here
import random
from time import sleep

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