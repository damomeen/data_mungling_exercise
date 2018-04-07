import unittest
import os, sys
import numpy as np

# import the modules which will be tested
sys.path.append(os.path.dirname("../src/"))
from football import FootballData, DATA_URL, FILE
from download import download_data                       
sys.path.pop()

# NOTE: In general TestCases should be very simple and explicit as much as possible

class WeatherTest(unittest.TestCase):
	
	def setUp(self):
		download_data(DATA_URL, FILE)
		self.football = FootballData(FILE)
		
	def test_number_of_entries(self):
		number_of_entries = self.football.df.shape[0]
		self.assertEqual(number_of_entries, 20)
	
	def test_A_are_int(self):
		self.assertEqual(self.football.df['A'].dtype, np.int32)
		
	def test_F_are_float(self):
		self.assertEqual(self.football.df['F'].dtype, np.int32)
	
	def test_no_missing_values(self):
		self.assertFalse(self.football.df.isnull().values.any())
	
	def test_D_column_not_present(self):
		self.assertNotIn('D', self.football.df.columns.values)
		
	def test_D_column_present(self):
		self.football._add_goals_difference('D')
		self.assertIn('D', self.football.df.columns.values)
		
	def test_team_with_min_goals_difference(self):
		team = self.football.find_team_with_min_goals_difference()
		self.assertEqual(team, ('8.', 'Aston_Villa'))
		
if __name__ == '__main__':
    unittest.main()