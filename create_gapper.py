import numpy as np
import pandas as pd
import re


def get_lap_time_seconds(lap_time_string):
	# String in format of m:ss.mmm. Need to convert minutes to seconds so split at ":"
	lap_time_split_string = lap_time_string.split(":")


	minutes = int(lap_time_split_string[0])
	minutes_to_seconds = minutes*60
	seconds = float(lap_time_split_string[1])
	totalseconds = minutes_to_seconds + seconds
	return round(totalseconds, 3)


def get_first_lap_gaps(lap_history_file_name):
	lap1_gaps = {}

	with open(lap_history_file_name) as file:
		for line_nr, line in enumerate(file):
			if line_nr > 0:
				if "LAP" in line:
					return lap1_gaps
				else:
					split_line = line.split()
					drivernumber = int(split_line[0])
					lap_time_string = split_line[-1]

					lap_time_seconds = get_lap_time_seconds(lap_time_string)
					lap1_gaps[drivernumber] = [lap_time_seconds]


lap1_gaps = get_first_lap_gaps("SIL Race History.txt")
print(lap1_gaps)