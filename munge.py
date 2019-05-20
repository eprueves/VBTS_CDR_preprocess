# Use Python 3.6 or greater

import pandas as pd
import numpy as np
import ccnutil
import ccnvars
import sys


try:
    fname = sys.argv[1]
except IndexError:
    print ("Missing args!!!")
    print ("Usage: python3 ./munge.py  {filename}")
    quit()

df = pd.read_csv(fname)
subs = pd.read_csv('sub_list.csv')

# Extract event_type indicated in description field
temp = df['Description'].str.split(r'[(\/)]', n=3, expand=True)
df['Type of Event FD'] = temp[1]
df['Hangup Cause'] = temp[2]

# sort OB/IB event types by network
# also determine correct event types for events tagged as 'unknown' 
df['Type of Event'] = df.apply(ccnutil.sort_network, axis=1)

# Get event_type counts and per event_type usage
# Also do some cleaning
counts = df.groupby(['Subscriber IMSI', 'Type of Event']).size()
sums = df.groupby(['Subscriber IMSI', 'Type of Event']).aggregate(sum).drop(
    ['Bytes Uploaded', 'Bytes Downloaded', 'Billable Call Duration (sec)', 'Tariff (PHP)'], axis=1)
sums.insert(loc=1, column='Average Call Duration (sec)', value=sums['Total Call Duration (sec)'] / counts)

# Unstack and then concatenate
sums = sums.unstack(fill_value=0)
counts = counts.unstack(fill_value=0)

# Remove uneeded columns as it doesn't make any sense (i.e. call duration for SMS events)
for_dropping = []
for item in list(sums.columns.values):
    if "Cost" in item[0]:
        continue
    elif "call" not in item[1]:
        for_dropping.append(item)
sums = sums.drop(for_dropping, axis=1)

summary = pd.concat([counts, sums], axis=1)

# Left join merge 'summary' df to 'subs' df
final = subs.merge(summary, how='left', left_on='IMSI', right_on='Subscriber IMSI')
final.insert(loc=2, column='Date', value=fname[18:28])
final.to_csv('final.csv', sep=',')
