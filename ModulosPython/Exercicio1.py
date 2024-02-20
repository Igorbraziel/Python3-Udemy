from datetime import datetime, timedelta
from dateutil import relativedelta

loan_date = datetime(2022, 12, 20)
print(loan_date)

loan_years = 5
loan_months = 5 * 12
loan_delta = relativedelta.relativedelta(years=loan_years)
one_month = relativedelta.relativedelta(months=1)
loan_end_date = loan_date + loan_delta
portion_value = 1_000_000 / loan_months 

print(loan_end_date, '\n')

while loan_end_date != loan_date:
    loan_date = one_month + loan_date
    print(f'U${portion_value:,.2f}', loan_date.strftime('%d/%m/%Y'))
