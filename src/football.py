import numpy as np
import pandas as pd
from download import download_data
from data_pipeline import DataPipeline

# where to find data online
DATA_URL = 'http://codekata.com/data/04/football.dat'

# filename of downloaded data
FILE = '../data/football.dat' 

class FootballData(DataPipeline):
	'''Football data for data preprocessing and analyse'''

	def _preprocess(self):
		'''
		Prepare and clean football data.
		Returns:
			The method returns itself.
		'''
		# Manually assign correct columns names
		self.df.columns = ['P', 'W', 'L', 'D', 'F', '-', 'A', 'Pts']
		
		# Remove unused features
		self.df = self.df.drop(['P', 'W', 'L', 'D', '-', 'Pts'], axis=1)
		
		# remove entries if goals value missing
		self.df = self.df.dropna() 
		
		# convert all values to integer
		self.df = self.df.astype(np.int)
		
		return self
		
	def _add_goals_difference(self, col_name):
		'''
		Calculate difference between goals scored for and against for each team
		and add it to the dataframe as a new feature.
		Returns:
			The method returns itself.
		'''
		self.df[col_name] = abs(self.df['F'] - self.df['A'])
		return self

	def find_team_with_min_goals_difference(self):
		'''
		Find a team with minimum difference between goals scored for and against the team.
		Returns:
			The method returns team description.
		'''
		min_SpT = self._add_goals_difference(col_name='D')._min('D')
		if min_SpT is not None:
			print("Minimal difference in goals found in dataframe entry:")
			print(min_SpT)
			return min_SpT.name
		else:
			print("Cannot find a team with mimimal goal difference because of empty dataframe.")
			return None

if __name__ == "__main__":
	
	download_data(DATA_URL, FILE)
	
	football = FootballData(FILE)
	
	team = football.find_team_with_min_goals_difference()
	print(f"Minimal goal difference was achieved by team: {' '.join(team)}.")
	
	football.visualize()



