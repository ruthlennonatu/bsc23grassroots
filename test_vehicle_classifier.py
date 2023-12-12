# test_vehicle_classifier.py

import unittest
from vehicle_classifier import classify_vehicle

class TestVehicleClassifier(unittest.TestCase):
    """ Tests for classify_vehicle function. """

    def test_motorcycle(self):
        """ Checks if 2 wheels is classified as 'Motorcycle'. """
        self.assertEqual(classify_vehicle(2), "Motorcycle")

    def test_trike(self):
        """ Checks if 3 wheels is classified as 'Trike'. """
        self.assertEqual(classify_vehicle(3), "Trike")

    def test_car(self):
        """ Checks if 4 wheels is classified as 'Car'. """
        self.assertEqual(classify_vehicle(4), "Car")

    def test_unknown(self):
        """ Checks if any other wheel count is classified as 'Unknown'. """
        self.assertEqual(classify_vehicle(5), "Unknown")

if __name__ == '__main__':
    unittest.main()
