from landerFuncs import *

def main():
   showWelcome()
   userAltitude = getAltitude()
   userFuel = getFuel()
   elapsedTime = velocity = fuelRate = 0
   gravity = 1.62
   print()
   print("LM state at retrorocket cutoff")
   while userAltitude > 0:
      if userFuel > 0: 
         displayLMState(elapsedTime, userAltitude, velocity, userFuel, fuelRate) 
         fuelRate = getFuelRate(userFuel)
      else:
         print("OUT OF FUEL - Elapsed Time: %3d Altitude: %7.2f Velocity: %7.2f" % (elapsedTime, userAltitude, velocity))
         fuelRate = 0
      userAcceleration = updateAcceleration(gravity, fuelRate)
      userAltitude = updateAltitude(userAltitude, velocity, userAcceleration)
      velocity = updateVelocity(velocity, userAcceleration)
      userFuel = updateFuel(userFuel, fuelRate) 
      elapsedTime += 1
   print()
   print('LM state at landing/impact')
   print("Elapsed Time: %4d s" % (elapsedTime))
   print("        Fuel: %4d l" % (userFuel))
   print("        Rate: %4d l/s" % (fuelRate))
   print("    Altitude:    0.00 m")
   print("    Velocity: %7.2f m/s\n" % (velocity))
   displayLMLandingStatus(velocity)

if __name__ == '__main__':
   main()
