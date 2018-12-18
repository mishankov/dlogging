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
		'style': '\33[1m'
	}
	return d

@log
def info(message):
	d = {
		'mode': 'INFO',
		'style': '\33[1;96m'
	}
	return d	

@log
def warning(message):
	d = {
		'mode': 'WARNING',
		'style': '\33[1;93m'
	}
	return d

@log
def error(message):
	d = {
		'mode': 'ERROR',
		'style': '\33[1;91m'
	}
	return d

@log
def critical(message):
	d = {
		'mode': 'CRITICAL',
		'style': '\33[1;101m'
	}
	return d

@log
def info_forced(message):
	d = {
		'mode': 'INFO',
		'style': '\33[1;96m'
	}
	return d

info_forced('Current logging configuration is\n{}'.format(json.dumps(config, indent=2)))
