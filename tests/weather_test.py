import unittest
import os, sys
import numpy as np

# import the modules which will be tested
sys.path.append(os.path.dirname("../src/"))
from weather import WeatherData, DATA_URL, FILE
from download import download_data                       
sys.path.pop()

# NOTE: In general TestCases should be very simple and explicit as much as possible

class WeatherTest(unittest.TestCase):
	
	def setUp(self):
		download_data(DATA_URL, FILE)
		self.weather = WeatherData(FILE)
		
	def test_number_of_entries(self):
		number_of_entries = self.weather.df.shape[0]
		self.assertEqual(number_of_entries, 30)

	def test_no_month_entry(self):
		self.assertNotIn('mo', self.weather.df['Dy'])
	
	def test_MxT_are_float(self):
		self.assertEqual(self.weather.df['MxT'].dtype, np.float64)
		
	def test_MxT_are_float(self):
		self.assertEqual(self.weather.df['MxT'].dtype, np.float64)
	
	def test_no_missing_values(self):
		self.assertFalse(self.weather.df.isnull().values.any())
	
	def test_SpT_column_not_present(self):
		self.assertNotIn('SpT', self.weather.df.columns.values)
		
	def test_SpT_column_present(self):
		self.weather._add_temperature_spread('SpT')
		self.assertIn('SpT', self.weather.df.columns.values)
		
	def test_day_with_min_temperature_spread(self):
		day = self.weather.find_day_with_min_temperature_spread()
		self.assertEqual(day, 14)
		
if __name__ == '__main__':
    unittest.main()