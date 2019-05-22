# VBTS_CDR_preprocess

This code is for preprocessing CDRs according to Arman's request. 

## Outfile File Schema

### Section A. subscriber info 
* These are taken from ccn_customerlist.csv, May 2019
* Column names:
    - hhuid_key: "Unique Household ID"
    - uuid_key: "Individual Identifier" 
    - member_id: "Household Member ID"
    - IMSI: aka unique ID of the SIM card
    - MSIDN: the mobile phone number
    - vbts_site_str: the location of the subscriber
  
### Section B. Date
* Column Names:
    - Date: date in YYYY-MM-DD format

### Section C. Event_types:
* Each column specifies the count/number of occurrences of each particular event_type/transaction
* Column names:
    - 'error_call': calls made to an bad/incorrectly-formatted/erroneous number
    - 'error_sms': SMS made to an bad/incorrectly-formatted/erroneous number
    - 'free_call': calls that are free of charge, usually these are made to shortcode numbers (i.e. balance inquiry)
    - 'free_sms': SMs that are free of charge, usually these are sent to shortcode numbers (i.e. balance inquiry
    - 'incoming_call_globe',: Inbound calls a VBTS number received a call from a number with a Globe number
    - 'incoming_call_others': Inbound calls a VBTS number received a call from a number with a Smart/other networks number
    - 'incoming_sms_globe': Inbound SMS where origin number is from Globe network
    - 'incoming_sms_others': Inbound SMS where origin number is from Smart and other networks
    - 'local_call': Calls where a VBTS number made a call to another VBTS number
    - 'local_recv_call': Calls where a VBTS number received a call from another VBTS number
    - 'local_recv_sms': SMS where a VBTS number received a text message from another VBTS number
    - 'local_sms': SMS where a VBTS number sent a text message to another VBTS number
    - 'outside_call_globe': Outbound call where a VBTS number called someone with a Globe number
    - 'outside_call_others' Outbound call where a VBTS number called someone with a Smart/other networks number 
    - 'outside_sms_globe': Outbound SMS where a VBTS number sent a text message to someone with a Globe number
    - 'outside_sms_others': Outbound SMS where a VBTS number sent a text message to someone with a Smart/other networks number
    - 'transfer': E-load transfer
    - 'promo_event': A promo auto-enrollment, cancellation or expiry event

### Section D. Call Duration:
* Column name is in a form of a tuple ('%duration_type', '%event_type')
* Valid only for call-type transactions
    - Total Call Duration (sec): value for the total length of a particular call type, in seconds
    - Average Call Duration (sec): value for the average length of a particular call type, in seconds
* Column names:
    -   "('Total Call Duration (sec)', 'error_call')"
    -   "('Total Call Duration (sec)', 'free_call')"
    -   "('Total Call Duration (sec)', 'incoming_call_globe')"
    -   "('Total Call Duration (sec)', 'incoming_call_others')"
    -   "('Total Call Duration (sec)', 'local_call')"
    -   "('Total Call Duration (sec)', 'local_recv_call')"
    -   "('Total Call Duration (sec)', 'outside_call_globe')"
    -   "('Total Call Duration (sec)', 'outside_call_others')"
    -   "('Average Call Duration (sec)', 'error_call')"
    -   "('Average Call Duration (sec)', 'free_call')"
    -   "('Average Call Duration (sec)', 'incoming_call_globe')"
    -   "('Average Call Duration (sec)', 'incoming_call_others')"
    -   "('Average Call Duration (sec)', 'local_call')"
    -   "('Average Call Duration (sec)', 'local_recv_call')"
    -   "('Average Call Duration (sec)', 'outside_call_globe')"
    -   "('Average Call Duration (sec)', 'outside_call_others')"
        
### Section E: Cost
* Column name is in a form of a Tuple ('Cost (PHP)', '%event_type')
* The value refers to e-load spent/gained by a subscriber for a particular event_type
    - negative, if credits were spent by subscriber
    - positive, if credits were gained by subscriber (i.e. from load transfer)
* Column names:
    -   "('Cost (PHP)', 'error_call')"
    -   "('Cost (PHP)', 'error_sms')",
    -   "('Cost (PHP)', 'free_call')"
    -   "('Cost (PHP)', 'free_sms')",
    -   "('Cost (PHP)', 'incoming_call_globe')"
    -   "('Cost (PHP)', 'incoming_call_others')"
    -   "('Cost (PHP)', 'incoming_sms_globe')"
    -   "('Cost (PHP)', 'incoming_sms_others')"
    -   "('Cost (PHP)', 'local_call')"
    -   "('Cost (PHP)', 'local_recv_call')"
    -   "('Cost (PHP)', 'local_recv_sms')
     -  "('Cost (PHP)', 'local_sms')"
    -   "('Cost (PHP)', 'outside_call_globe')"
    -   "('Cost (PHP)', 'outside_call_others')"
    -   "('Cost (PHP)', 'outside_sms_globe')"
    -   "('Cost (PHP)', 'outside_sms_others')"
    -   "('Cost (PHP)', 'transfer')"
    
### Section F: Promo Info
* Indicates if promo is active for a particular subscriber during the date specified
    - 1, if subscriber has valid subscriber during the specified date
    - 0, otherwise
* Column names:
    - 'FL': Freeload promo
    - 'GL': Local discount promo
    - 'GLD': Long distance discount promo
    
    
## Notes
* Blank values in final csv correspond to Nan