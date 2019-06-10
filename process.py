# Use Python 3.6 or greater

import pandas as pd
import ccnutil
import sys

try:
    fname = sys.argv[1]
except IndexError:
    print("Missing args!!!")
    print("Usage: python3 ./process.py  {filename}")
    print("Program assumes that the filename is in the following format: etage-YYYY-MM-DD.csv")
    quit()


# Open CCN subscriber master list
cols = ['hhuid_key', 'uuid_key', 'memberid', 'IMSI', 'MSISDN', 'vbts_site_str']
subs = pd.read_csv('ccn_customerlist.csv')[cols]

# Open promo status master list
promostatus = ccnutil.open_promo_status(fname)

# Get datetime today and compare promo status vs today's date
today = ccnutil.fname_to_datetime(fname)
promostatus_today = ccnutil.check_status_today(promostatus, today)

# Munge CDR data
summary = ccnutil.munge(fname)

# Left join merge 'summary' df, 'promostatus_today' df to 'subs' df
final = subs.merge(summary, how='left', left_on='IMSI', right_on='Subscriber IMSI')
final.insert(loc=6, column='Date', value=today)
final = final.merge(promostatus_today, how='left', left_on='IMSI', right_on='IMSI')
final.to_csv('final2.csv', sep=',')
