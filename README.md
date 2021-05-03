# generate-date-table
Generates a csv file with all date information between 2 years

Update start_year and end_year with desired years.

Script will output a pipe-delimited csv file in the current directory.

Use table generation SQL file for desired DBMS and load CSV file.

Included columns and value example:
	'id': 20201231 
	'calendar_date': '2020-12-31' 
	'calendar_day': 31 
	'calendar_month': 12 
	'calendar_calendar_year': '2020' 
	'calendar_mon_d_y': 'Dec. 31,  2020' 
	'calendar_m_d_y': '12/31/2020' 
	'reporting_y_q_w': '2020Q4W52' 
	'reporting_y_w': '2020W52' 
	'reporting_y_w_d': '2020W52D4' 
	'day_of_week_number': 4 
	'day_of_week_name': 'Thursday' 
	'day_of_week_short_name': 'Thu' 
	'day_of_week_abv_name': 'Th' 
	'week_number': 52 
	'week_short_name': 'W52' 
	'month_number': 12 
	'month_name': 'December' 
	'month_short_name': 'Dec' 
	'day_of_month_number': 31 
	'quarter_number': 4 
	'quarter_name': '2020Q4' 
	'year_number': 2020 
	'year name': 'Year 2020' 
	'day_of_year_number': 366
