from datetime import date, timedelta
import csv

def getQuarter(month):
	if month in (1,2,3): return '1'
	elif month in (4,5,6): return '2'
	elif month in (7,8,9): return '3'
	elif month in (10,11,12): return '4'
def getWeekNumber(cDate):
	return int(cDate.strftime('%W'))
def getDayAbv(day):
	if day == 'Monday': return 'M'
	elif day == 'Tuesday': return 'Tu'
	elif day == 'Wednesday': return 'W'
	elif day == 'Thursday': return 'Th'
	elif day == 'Friday': return 'F'
	elif day == 'Saturday': return 'Sa'
	elif day == 'Sunday': return 'Su'
def dictToFile(d,file_name):
	headers = [k for k,v in d[0].items()]
	with open(file_name, 'w', encoding='utf-8') as file:
		writer = csv.DictWriter(file, fieldnames=headers,delimiter='|', lineterminator='\n',quotechar='"', quoting=csv.QUOTE_MINIMAL)
		writer.writeheader()
		for row in d:
			writer.writerow(row)

start_year = 2010
end_year = 2030
file_name = 'date_records.csv'

current_date = date(start_year,1,1)
records = []
while current_date <= date(end_year,12,31):
	date_rec = {
		'id': int(current_date.strftime('%Y%m%d')),
		'calendar_date': current_date.strftime('%Y-%m-%d'),
		'calendar_day': int(current_date.strftime('%d')),
		'calendar_month': int(current_date.strftime('%m')),
		'calendar_year': (current_date.strftime('%Y')),
		'calendar_mon_d_y': current_date.strftime('%b. %d, %Y'),
		'calendar_m_d_y': '{0}/{1}/{2}'.format(current_date.month,current_date.day, current_date.year),
		'reporting_y_q_w': '{0}Q{1}W{2}'.format(current_date.year,getQuarter(current_date.month), getWeekNumber(current_date)),
		'reporting_y_w': '{0}W{1}'.format(current_date.year, getWeekNumber(current_date)),
		'reporting_y_w_d': '{0}W{1}D{2}'.format(current_date.year, getWeekNumber(current_date), current_date.weekday() + 1),
		'day_of_week_number': current_date.weekday() + 1,
		'day_of_week_name': current_date.strftime('%A'),
		'day_of_week_short_name': current_date.strftime('%a'),
		'day_of_week_abv_name': getDayAbv(current_date.strftime('%A')),
		'week_number': getWeekNumber(current_date),
		'week_short_name':'W{0}'.format(getWeekNumber(current_date)),
		'month_number':int(current_date.strftime('%m')),
		'month_name': current_date.strftime('%B'),
		'month_short_name': current_date.strftime('%b'),
		'day_of_month_number': int(current_date.strftime('%d')),
		'quarter_number': int(getQuarter(current_date.month)),
		'quarter_name': '{0}Q{1}'.format(current_date.year,getQuarter(current_date.month)),
		'year_number':current_date.year,
		'year_name': 'Year {0}'.format(current_date.year),
		'day_of_year_number':int(current_date.strftime('%j'))
	}
	records.append(date_rec)
	current_date += timedelta(days=1)

dictToFile(records, file_name)