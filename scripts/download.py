import kaggle
from kaggle.api.kaggle_api_extended import KaggleApi
kaggle.api.authenticate()

kaggle.api.dataset_download_files('anandshaw2001/top-spotify-songs-in-countries', path='./input', unzip=True)

