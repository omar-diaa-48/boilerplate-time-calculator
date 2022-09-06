def add_time(start:str, duration:str, day:str=None):

	days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

	start_splitted = start.split(' ')
	start_time = start_splitted[0]
	start_format = start_splitted[1]

	start_time_splitted = start_time.split(':')
	start_time_hour = int(start_time_splitted[0])
	start_time_minute = int(start_time_splitted[1])

	if (start_format == "PM"):
		start_time_hour = start_time_hour + 12

	duration_splitted = duration.split(':')
	duration_hour = int(duration_splitted[0])
	duration_minute = int(duration_splitted[1])

	result_minute = start_time_minute + duration_minute
	result_hour = 0

	if (result_minute >= 60):
		result_minute -= 60
		result_hour += 1

	result_hour += start_time_hour + duration_hour
	number_of_days_added = 0

	if (result_hour >= 24):
		number_of_days_added = result_hour//24
		result_hour = result_hour%24

	result_format = "AM"

	if(result_hour >= 12):
		result_format = "PM"
		result_hour -= 12

	printed_hour = result_hour
	if(printed_hour == 0):
		printed_hour = '12'

	printed_minute = result_minute
	if(printed_minute < 10):
		printed_minute = f'0{printed_minute}'

	result = f'{printed_hour}:{printed_minute} {result_format}'

	if(day is not None):
		day = day.capitalize()

		if(day in days):
			day_index = days.index(day)
			required_day_index = day_index + number_of_days_added
			if(required_day_index > len(days)):
				required_day_index = required_day_index%len(days)  
			day = days[required_day_index]

		result+= f', {day}'

	if(number_of_days_added > 0):
		if(number_of_days_added == 1):
			result += ' (next day)'
		else:
			result+= f' ({number_of_days_added} days later)'

	print(result)
	return result

add_time("3:00 PM", "3:10")
# Returns: 6:10 PM

add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday

add_time("11:43 AM", "00:20")
# Returns: 12:03 PM

add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)

add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)

add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)
