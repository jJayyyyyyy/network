#!/usr/bin/env python3
# -*- coding: utf-8 -*-
months = ['January',
		  'Feburary',
		  'March',
		  'April',
		  'May',
		  'June',
		  'July',
		  'August',
		  'September',
		  'October',
		  'December']

month_abbvs = dict( (m[:3].lower(), m) for m in months )

def valid_month(month):
	if month:
		valid_m = month_abbvs.get( month[:3].lower() )
		if valid_m:
			return valid_m
	# return "Error Month"

def valid_day(day):
	if day and day.isdigit():
		day = int(day)
		if day > 0 and day <= 31:
			return day
	# return "Error Day"

def valid_year(year):
	if year and year.isdigit():
		year = int(year)
		if year > 1900 and year < 2020:
			return year
	# return "Error Year"
