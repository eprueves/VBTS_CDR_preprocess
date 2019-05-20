import ccnvars

def sort_network(row):
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
        

