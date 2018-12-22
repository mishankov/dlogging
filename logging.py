from .constants import DEFAULT_CONFIG
from . import utils
import datetime
# from time import gmtime, strftime
import os
from inspect import getframeinfo, stack
import json

# load configs
try:
	# try to load configs from file
	file = open(os.getcwd() + '/dlogging.json', 'r')
	config = json.load(file)
	file.close()
except FileNotFoundError as e:
	# if there is no config file => create file with default configs
	config = DEFAULT_CONFIG
	file = open(os.getcwd() + '/dlogging.json', 'w')
	json.dump(config, file, indent=2)
	file.close()
# upgrade configs to work with it
config = utils.upgrade_config(config)

def log(fn):
	def wrapper(message):
		d = fn(message)
		caller = getframeinfo(stack()[1][0])

		if config['level'] <= d['level']:
			print(utils.fill_template(
					config['log_template'], 
					caller, 
					d, 
					message, 
					config[d['mode']]['style']
					))
	return wrapper

@log
def debug(message):
	d = {
		'mode': 'DEBUG',
		'level': 0
	}
	return d

@log
def info(message):
	d = {
		'mode': 'INFO',
		'level': 1
	}
	return d	

@log
def warning(message):
	d = {
		'mode': 'WARNING',
		'level': 2
	}
	return d

@log
def error(message):
	d = {
		'mode': 'ERROR',
		'level': 3
	}
	return d

@log
def critical(message):
	d = {
		'mode': 'CRITICAL',
		'level': 4
	}
	return d

@log
def info_forced(message):
	d = {
		'mode': 'INFO',
		'level': 99
	}
	return d

# FIX ME: use dlogging-light here
# info_forced('Current logging configuration is\n{}'.format(json.dumps(config, indent=2)))
