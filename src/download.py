from urllib.request import urlretrieve
from urllib.error import URLError, HTTPError
import os.path


def download_data(from_url, to_localfile):
	'''
	Download a data if nessary.
	Args:
		from_url: URL containing data.
		to_localfile: filename and location where data will be downloaded.
	Raises:
		URLError: When cannot connect to remote server with data.
		HTTPError: When data not found on remote server.
		Exception: For any other reason.
	'''
	if os.path.isfile(to_localfile):
		print(f"Data already present in the local directory in file: {to_localfile}.")
		return   # download skipped
	
	print(f"Downloading data...")
	try:
		urlretrieve(from_url, to_localfile)
	except URLError as exc:
		print(f"Cannot connect and download weather data from {from_url}.")
		raise exc
	except HTTPError as exc:
		print(f"Connected to the data server but weather data not found at {from_url}.")
		raise exc
	except:
		import traceback
		traceback.print_ext()
		raise Exception(f"Data download from {from_url} unsuccesfull.")