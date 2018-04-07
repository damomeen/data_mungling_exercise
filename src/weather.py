import pandas as pd
import matplotlib.pyplot as plt
from download import download_data
from data_pipeline import DataPipeline

# where to find data online
DATA_URL = 'http://codekata.com/data/04/weather.dat'

# filename of downloaded data
FILE = '../data/weather.dat'  

class WeatherData(DataPipeline):
	'''Weather data for data preprocessing and analyse'''
	def _preprocess(self):
		'''
		Prepare and clean weather data.
		Returns:
			The method returns itself.
		'''
		# Remove unused features
		self.df = self.df[['Dy', 'MxT', 'MnT']]
		
		# remove entries if temperature value missing
		self.df.dropna() 
		
		# remove `*` from temperature and convert to float 
		for feature in ['MxT', 'MnT']:
			self.df[feature] = self.df[feature].apply(lambda temp: float(temp.replace("*", "")))
			
		# remove weather data entries if unlogic temperature values found
		self.df = self.df[self.df['MxT'] - self.df['MnT'] >= 0]

		# remove weather data summarizing the whole month
		self.df = self.df[self.df['Dy'] != 'mo']
		
		return self
		
	def _add_temperature_spread(self, col_name):
		'''
		Calculate difference between maximum and minimum temperature for each day
		and add it to the dataframe as new `DiffT` feature.
		Returns:
			The method returns itself.
		'''
		self.df[col_name] = self.df['MxT'] - self.df['MnT']
		return self
		
	def find_day_with_min_temperature_spread(self):
		'''
		Find a day with minimum spread of temperature.
		Returns:
			The method returns a day number.
		'''
		min_SpT = self._add_temperature_spread(col_name='SpT')._min('SpT')
		if min_SpT is not None:
			print("Minimal temperature spread found in dataframe entry:")
			print(min_SpT)
			return int(min_SpT['Dy'])
		else:
			print("Cannot find a day with mimimal spread temperature because of empty dataframe.")
			return None

if __name__ == "__main__":
	
	download_data(DATA_URL, FILE)
	
	weather = WeatherData(FILE)
	
	day = weather.find_day_with_min_temperature_spread()
	print(f"Minimal temperature spread was observed at day #{day}.")
	
	weather.visualize()



