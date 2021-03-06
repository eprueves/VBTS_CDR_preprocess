import ccnvars
import pandas as pd
from _datetime import datetime, timedelta


def sort_event_type(row):
    event_type = row['Type of Event']
    event_type_frm_description = row['Type of Event FD']
    to_num = row['To Number']
    from_num = row['From Number']
    
    if event_type in ccnvars.EXTERNAL_CALL_EVENTS:
        if event_type == 'incoming_call':
            num = '63' + from_num  # they don't have the 63 prefix
        else:
            if to_num[:2] == '09':
                num = '63' + to_num[1:]
            elif to_num[:1] == '+':
                num = to_num[1:]
            else:
                num = to_num
            if event_type == "globe_call":
                event_type = 'outside_call'  
                
    elif event_type in ccnvars.EXTERNAL_SMS_EVENTS:
        if event_type == 'incoming_sms':
            num = '63' + from_num  # they don't have the 63 prefix
        else:
            num = to_num
    elif event_type == 'unknown':
        if event_type_frm_description == 'D_globe_sms':
            event_type = 'outside_sms'
            num = to_num
        elif "Promo" in row['Description']:       
            return "promo_event"
    else:
        return event_type
             
    if num[:5] in ccnvars.GLOBE:
        return "%s_%s" % (event_type, 'globe')
    else:
        return "%s_%s" % (event_type, 'others')


def open_promo_status(fname):
    # Open promo status file
    promostatus = pd.read_csv('Promo_status_tracking_MASTER_201905.csv')

    # convert dates to datetime object
    promostatus['Promo1 Start'] = pd.to_datetime(promostatus['Promo1 Start'], format='%m+AC0-%d+AC0-%y')
    promostatus['Promo2 Start'] = pd.to_datetime(promostatus['Promo2 Start'], format='%m+AC0-%d+AC0-%y')
    promostatus['Freeload transfered on'] = pd.to_datetime(promostatus['Freeload transfered on'],
                                                           format='%m+AC0-%d+AC0-%y')

    promostatus['has GL'] = promostatus['Promo1 (GL/GLD)'] == 'GL'
    promostatus['has GLD'] = promostatus['Promo1 (GL/GLD)'] == 'GLD'

    return promostatus


def check_status_today(promostatus, today):

    promostatus['Promo1 Start diff'] = today - promostatus['Promo1 Start']
    promostatus['GL active'] = (promostatus['Promo1 Start diff'] <= timedelta(days=30)) & (promostatus['has GL'])
    promostatus['GLD active'] = (promostatus['Promo1 Start diff'] <= timedelta(days=30)) & (promostatus['has GLD'])
    promostatus['FL sent'] = promostatus['Freeload transfered on'] == today

    return promostatus[['IMSI', 'GLD active', 'GL active', 'FL sent']].groupby('IMSI').any()


def munge(fname):
    df = pd.read_csv(fname)

    # Extract event_type indicated in description field
    temp = df['Description'].str.split(r'[(\/)]', n=3, expand=True)
    df['Type of Event FD'] = temp[1]
    df['Hangup Cause'] = temp[2]

    # sort OB/IB event types by network
    # also determine correct event types for events tagged as 'unknown'
    df['Type of Event'] = df.apply(sort_event_type, axis=1)

    # Get event_type counts and per event_type usage
    # Also do some cleaning
    counts = df.groupby(['Subscriber IMSI', 'Type of Event']).size()
    cols = ['Total Call Duration (sec)', 'Billable Call Duration (sec)', 'Cost (PHP)']
    sums = df.groupby(['Subscriber IMSI', 'Type of Event'])[cols].aggregate(sum)
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

    return pd.concat([counts, sums], axis=1)


def fname_to_datetime(fname):
    year = fname[6:10]
    mon = fname[11:13]
    day = fname[14:16]
    today = '%s-%s-%s' % (mon, day, year[2:4])
    return datetime.strptime(today, "%m-%d-%y")
