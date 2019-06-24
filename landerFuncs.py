def showWelcome():
   print()
   print("Welcome aboard the Lunar Module Flight Simulator")
   print()
   print("   To begin you must specify the LM's initial altitude")
   print("   and fuel level.  To simulate the actual LM use")
   print("   values of 1300 meters and 500 liters, respectively.")
   print()
   print("   Good luck and may the force be with you!\n")

def getFuel():
   userFuel = int(input('Enter the initial amount of fuel on board the LM (in liters): '))
   while userFuel <= 0:
      print("ERROR: Amount of fuel must be positive, please try again")
      userFuel = int(input('Enter the initial amount of fuel on board the LM (in liters): '))
   return userFuel

def getAltitude():
   userAltitude = int(input("Enter the initial altitude of the LM (in meters): "))
   while userAltitude < 1 or userAltitude > 9999:
      print("ERROR: Altitude must be between 1 and 9999, inclusive, please try again")
      userAltitude = int(input("Enter the initial altitude of the LM (in meters): "))
   return userAltitude

def displayLMState(elapsedTime, altitude, velocity, fuelAmount, fuelRate):
   print("Elapsed Time: %4d s" % (elapsedTime))
   print("        Fuel: %4d l" % (fuelAmount))
   print("        Rate: %4d l/s" % (fuelRate))
   print("    Altitude: %7.2f m" % (altitude))
   print("    Velocity: %7.2f m/s\n" % (velocity))

def getFuelRate(currentFuel):
   userFuelRate = int(input("Enter fuel rate (0-9, 0=freefall, 5=constant velocity, 9=max thrust): "))
   while userFuelRate < 0 or userFuelRate > 9:
      print("ERROR: Fuel rate must be between 0 and 9, inclusive\n")
      userFuelRate = int(input("Enter fuel rate (0-9, 0=freefall, 5=constant velocity, 9=max thrust): "))
   if userFuelRate > currentFuel:
      return currentFuel
   return userFuelRate

def updateAcceleration(gravity, fuelRate):
   acceleration = gravity * ((fuelRate / 5) - 1)
   return acceleration

def updateAltitude(altitude, velocity, acceleration):
   altitude = altitude + velocity + (acceleration / 2)
   if altitude <= 0:
      return 0
   return altitude

def updateVelocity(velocity, acceleration):
   velocity = velocity + acceleration #updated acceleration
   return velocity

def updateFuel(fuel, fuelRate):
   fuel = fuel - fuelRate
   return fuel

def displayLMLandingStatus(velocity):
   if -1 <= velocity <= 0:
      print("Status at landing - The eagle has landed!")
   elif -10 < velocity < -1:
      print("Status at landing - Enjoy your oxygen while it lasts!")
   elif velocity <= -10:
      print("Status at landing - Ouch - that hurt!")
