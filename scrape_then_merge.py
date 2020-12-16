from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta
import usgs_scraper import scrape

# implement argparser for next iteration

begin_date = datetime.strptime('2017-10-03', '%Y-%m-%d')
end_date = datetime.strptime('2018-07-06', '%Y-%m-%d')

increment = timedelta(days=7)
first_date = begin_date-increment
second_date = first_date + increment

while second_date <= end_date:
    first_date += increment
    second_date = first_date + increment - timedelta(days=1) #prevent overlap
    first_str = str(first_date)[:10]
    second_str = str(second_date)[:10]
    scrape(first_str,second_str)
    #print(f'the first date is {str(first_date)} and the second date is {str(second_date)}')