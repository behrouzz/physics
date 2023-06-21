import numpy as np
import matplotlib.pyplot as plt
from astropy.time import Time
from datetime import datetime, timedelta



days = 365 * 5
dates = [datetime(2020,1,1,12,0,0) + timedelta(days=i) for i in range(days)]
dates2 = [i+timedelta(seconds=1) for i in dates]

dts = (Time(dates2, scale='utc').tdb - Time(dates, scale='utc').tdb).sec

fig, ax = plt.subplots()
ax.scatter(dates, dts, s=1)
ax.ticklabel_format(axis="y", useOffset=False, style='plain')

plt.grid()
plt.show()
