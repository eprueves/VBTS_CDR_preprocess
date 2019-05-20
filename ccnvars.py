prefix_globe = [
    '63905',
    '63906',
    '63915',
    '63916',
    '63917',
    '63926',
    '63927',
    '63935',
    '63945',
    '63955',
    '63956',
    '63966',
    '63975',
    '63976',
    '63977',
    '63995',
    '63997',
]

prefix_globe_abscbn = ['63937']

prefix_globe_cherry = ['63996']

prefix_smart = [
    '63918',
    '63919',
    '63920',
    '63921',
    '63928',
    '63929',
    '63938',
    '63939',
    '63946',
    '63947',
    '63948',
    '63949',
    '63950',
    '63962',
    '63998',
    '63999',
]

prefix_smart_piltel = [
    '63907',
    '63908',
    '63909',
    '63910',
    '63912',
    '63930',
]

prefix_sun = [
    '63922',
    '63923',
    '63925',
    '63931',
    '63932',
    '63933',
    '63942',
    '63943',
]

prefix_tmbrgy = ['63936']


GLOBE = [
    '63905',
    '63906',
    '63915',
    '63916',
    '63917',
    '63926',
    '63927',
    '63935',
    '63945',
    '63955',
    '63956',
    '63966',
    '63975',
    '63976',
    '63977',
    '63995',
    '63997',
    '63937',    # abs-cbn mobile
    '63996',    # cherry
    '63936'     # TM
]

SMART = [prefix_sun, prefix_smart, prefix_smart_piltel]

EXTERNAL_CALL_EVENTS = ['incoming_call', 'outside_call', 'globe_call']

EXTERNAL_SMS_EVENTS = ['incoming_sms', 'outside_sms', 'globe_sms']

EVENTS = ["local_call", "local_sms", "outside_call", "outside_sms",
          "free_call", "free_sms", "incoming_sms", "error_sms",
          "error_call", "transfer", "add_money", "deduct_money",
          "set_balance", "unknown", "Provisioned", "local_recv_call",
          "local_recv_sms", "incoming_call", "gprs",
          "deactivate_number", "delete_imsi"]
