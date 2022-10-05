# imports
import json

# internal imports
import logger

# loading config
with open('config.json') as json_file:
    config = json.load(json_file)
if config['dev_mode']: # warning if dev mode is enabled
    logger.warn("StarHunter", "Running in dev mode")

CONFIG = config

DEV = config['dev_mode']
