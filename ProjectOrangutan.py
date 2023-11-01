print("***************************")
print("Gasoline Branch\n\n")

# Import Libraries Here
import random
from time import sleep

# Function that lists Gas Stations, randomly choosing one, and Return its value
def gasLevelGauge():
      gasLevelList = ["Empty","Low","Quarter Tank","Half Tank","Three Quarter Tank","Full Tank"]
      currentGasLevel = random.choice(gasLevelList)
      return currentGasLevel

# Function with list of GasStations
def listOfGasStations():
      gasStations = ["Shell", "Speedway", "Exxon", "Meijer", "Costco", "Marathon", "BP", "Circle K", "Wesco"]
      gasStationsNearby = random.choice(gasStations)
      return gasStationsNearby


# Function will call the gas level gauge to determine gasLevelGauge, and then find a close gas station if low
def gasLevelAlert():
      milesToGasStationLow = round(random.uniform(1,25),1)
      milesToGasStationQuarterTank = round(random.uniform(25.1, 50), 1)
      print("low =", milesToGasStationLow)
      print("quarter tank =", milesToGasStationQuarterTank)

      
gasLevelAlert()