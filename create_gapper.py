import numpy as np
import pandas as pd
import re


def get_lap_time_seconds(lap_time_string):
	# String in format of m:ss.mmm. Need to convert minutes to seconds so split at ":"
	lap_time_split_string = lap_time_string.split(":")

	# Convert the number of minutes to seconds by multiplying by 60
	minutes = int(lap_time_split_string[0])
	minutes_to_seconds = minutes*60

	# The seconds and milliseconds part can just be converted to a float.
	seconds = float(lap_time_split_string[1])

	totalseconds = minutes_to_seconds + seconds
	return round(totalseconds, 3)


def get_first_lap_gaps(lap_history_file_name):
	lap_times = {}

	with open(lap_history_file_name) as file:
		for line_nr, line in enumerate(file):
			if line_nr > 0:
				if "LAP" in line:
					return lap_times
				else:
					split_line = line.split()
					drivernumber = int(split_line[0])
					lap_time_string = split_line[-1]

					lap_time_seconds = get_lap_time_seconds(lap_time_string)
					lap_times[drivernumber] = [lap_time_seconds]


def get_rest_of_session_lap_times(lap_analysis_file_name, lap_times):
		with open(lap_analysis_file_name) as file:
			for line_nr, line in enumerate(file):
					line_type = get_line_type(line)

def get_line_type(line):
	useless_info = ["The F1 FORMULA 1 logo", "a Formula 1 company", "No part of these results",
					"without prior permission", "the results/data relate", "Formula One World",
					"Page" "FORMULA 1", "Race Lap Analysis", "LAP TIME"]

	driver_numbers_and_names = {44: "HAM", 77: "BOT", 5: "VET", 16: "LEC", 33:"VER", 23: "ALB", 3: "RIC"}

	for part in useless_info:
		if part in line:
			return "Useless"

	new_driver_pattern = re.compile(r"\d{1,2}\s\w{3,100}\s\w{3,50}")
	if new_driver_pattern.match(line):
		print(new_driver_pattern.match(line))
		return "New Driver"

lap_times = get_first_lap_gaps("SIL Race History.txt")
get_rest_of_session_lap_times("Lap Analysis.txt", lap_times)
print(lap_times)
