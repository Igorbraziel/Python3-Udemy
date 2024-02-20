from datetime import datetime
from pytz import timezone

#data = datetime.now(timezone('Asia/Tokyo'))
#print(data)

format_ = '%Y-%m-%d %H:%M:%S'
date_ = '2024-02-15 11:44:00'
date_now = datetime.strptime(date_, format_)
print(date_now)