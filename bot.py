from os 	  				import getenv as env
from classes.client	import app

app("randbot",	env('API_ID'), env('API_HASH'), bot_token=env('TG_TOKEN')).run_custom()