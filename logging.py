from .constants import *
import datetime
from time import gmtime, strftime
import os
from inspect import getframeinfo, stack


def log(fn):
	def wrapper(message):
		d = fn(message)

		caller = getframeinfo(stack()[1][0])

		print(LOG_TEMPLATE.format(
			# date=datetime.datetime.now(),
			date=strftime("%Y-%m-%d %H:%M:%S", gmtime()),
			file=FILE_TEMPLATE.format(caller.filename, caller.lineno),
			style=d['style'],
			mode=d['mode'],
			message=message)
		)
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
