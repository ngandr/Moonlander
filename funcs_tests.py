import unittest
from landerFuncs import *

class TestCases(unittest.TestCase):
   def test_update_acc1(self):
      self.assertAlmostEqual(updateAcceleration(1.62, 0), -1.62)
   def test_update_acc2(self):
      self.assertAlmostEqual(updateAcceleration(1.62, 1), -1.296)
   def test_update_acc3(self):
      self.assertAlmostEqual(updateAcceleration(9.8, 0), -9.8)
   def test_update_alt1(self):
      self.assertAlmostEqual(updateAltitude(1938, -2.40, 3), 1937.1)
   def test_update_alt2(self):
      self.assertAlmostEqual(updateAltitude(593, -6.83, 2.6), 587.47)
   def test_update_vel1(self):
      self.assertAlmostEqual(updateVelocity(-3, 5.5), 2.5)
   def test_update_vel2(self):
      self.assertAlmostEqual(updateVelocity(-2, 3.14), 1.14)
   def test_update_fuel1(self):
      self.assertEqual(updateFuel(450, 16), 434)
   def test_update_fuel2(self):
      self.assertEqual(updateFuel(369, 22), 347)

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()
