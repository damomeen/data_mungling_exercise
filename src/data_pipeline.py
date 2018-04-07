import pandas as pd
import matplotlib.pyplot as plt

# Note: I'm using Pandas beacause it is the most known library for any data munging, preparation and analyse from a long time.
#             It can deal with pesky datasets like in those two execises.

# Note: In case of big datasets I would replace pandas with Dask (provides pandas compatible interface)
#             https://www.youtube.com/watch?time_continue=2645&v=RA_2qdipVng
#            However, for really short processing delays, I'm ususally writting my own low level and dedicated libraries (as in my last project for Brocade
#            where I had to process online information about traffic in 10G network).

# Note: Normally I'm create logging infrastructure but trying to be KISS here (however prints appear in unitest output)

class DataPipeline:
	'''Tip: Methods returns self allowing for nice data processing pipelining'''
	
	def __init__(self, filename):
		'''
		Read file with data to pandas dataframe and then preprocess the data.
		Args:
			filename: file name and location with a dataset
		'''
		self.df = pd.read_csv(filename, delim_whitespace=True)
		self._preprocess()
		print(f"Number of entries in data is {self.df.shape[0]}.")
		
	def _preprocess(self):
		'''
		Prepare and clean the dataframe.
		Returns:
			The method returns itself.
		'''
		return self
	
	def _min(self, feature):
		'''
		Find dataframe row entry with minimum value for a given feature.
		Args:
			feature: dataframe feature name (a "column").
		Returns:
			The method returns a pandas dataframe row entry or None if dataframe empty.
		'''
		if self.df.shape[0] == 0:
			return None # no rows in dataframe
			
		return self.df.loc[self.df[feature].idxmin()]
		
	def visualize(self):
		'''Plot the dataframe.'''
		self.df.plot()
		plt.show()