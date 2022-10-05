# imports
import json

# internal imports
import logger

# loading config
with open('config.json') as json_file:
    config = json.load(json_file)

CONFIG = config
DEV = config['dev_mode']
