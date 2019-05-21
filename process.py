# Use Python 3.6 or greater

import pandas as pd
import ccnutil
import sys

try:
    fname = sys.argv[1]
except IndexError:
    print("Missing args!!!")
    print("Usage: python3 ./process.py  {filename}")
    quit()

summary = ccnutil.munge(fname)

# Open ccn subscriber list
cols = ['hhuid_key', 'uuid_key', 'memberid', 'IMSI', 'MSISDN', 'vbts_site_str']
subs = pd.read_csv('ccn_customerlist.csv')[cols]

# Left join merge 'summary' df to 'subs' df
final = subs.merge(summary, how='left', left_on='IMSI', right_on='Subscriber IMSI')
final.insert(loc=6, column='Date', value=fname[18:28])
final.to_csv('final.csv', sep=',')
