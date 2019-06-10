
SMART = [   # mobile prefixes under the SMART network
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
    '63907',    # smart-piltel
    '63908',    # smart-piltel
    '63909',    # smart-piltel
    '63910',    # smart-piltel
    '63912',    # smart-piltel
    '63930',    # smart-piltel
    '63922',    # sun
    '63923',    # sun
    '63925',    # sun
    '63931',    # sun
    '63932',    # sun
    '63933',    # sun
    '63942',    # sun
    '63943',    # sun
]

GLOBE = [   # mobile prefixes under the GLOBE network
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

# Event types defined in original CCN client code
EVENTS = ["local_call", "local_sms", "outside_call", "outside_sms",
          "free_call", "free_sms", "incoming_sms", "error_sms",
          "error_call", "transfer", "add_money", "deduct_money",
          "set_balance", "unknown", "Provisioned", "local_recv_call",
          "local_recv_sms", "incoming_call", "gprs",
          "deactivate_number", "delete_imsi"]

EXTERNAL_CALL_EVENTS = ['incoming_call', 'outside_call', 'globe_call']

EXTERNAL_SMS_EVENTS = ['incoming_sms', 'outside_sms', 'globe_sms']


# Refer to https://freeswitch.org/confluence/display/FREESWITCH/Hangup+Cause+Code+Table
FS_HANGUP_CAUSES = [
    "UNSPECIFIED",
    "UNALLOCATED_NUMBER",
    "NO_ROUTE_TRANSIT_NET",
    "NO_ROUTE_DESTINATION",
    "CHANNEL_UNACCEPTABLE",
    "CALL_AWARDED_DELIVERED",
    "NORMAL_CLEARING",
    "USER_BUSY",
    "NO_USER_RESPONSE",
    "NO_ANSWER",
    "SUBSCRIBER_ABSENT",
    "CALL_REJECTED",
    "NUMBER_CHANGED",
    "REDIRECTION_TO_NEW_DESTINATION",
    "EXCHANGE_ROUTING_ERROR",
    "DESTINATION_OUT_OF_ORDER",
    "INVALID_NUMBER_FORMAT",
    "FACILITY_REJECTED",
    "RESPONSE_TO_STATUS_ENQUIRY",
    "NORMAL_UNSPECIFIED",
    "NORMAL_CIRCUIT_CONGESTION",
    "NETWORK_OUT_OF_ORDER",
    "NORMAL_TEMPORARY_FAILURE",
    "SWITCH_CONGESTION",
    "ACCESS_INFO_DISCARDED",
    "EQUESTED_CHAN_UNAVAIL",
    "PRE_EMPTED",
    "FACILITY_NOT_SUBSCRIBED",
    "OUTGOING_CALL_BARRED",
    "INCOMING_CALL_BARRED",
    "BEARERCAPABILITY_NOTAUTH",
    "BEARERCAPABILITY_NOTAVAIL",
    "SERVICE_UNAVAILABLE",
    "BEARERCAPABILITY_NOTIMPL",
    "CHAN_NOT_IMPLEMENTED",
    "FACILITY_NOT_IMPLEMENTED",
    "SERVICE_NOT_IMPLEMENTED",
    "INVALID_CALL_REFERENCE",
    "INCOMPATIBLE_DESTINATION",
    "INVALID_MSG_UNSPECIFIED",
    "MANDATORY_IE_MISSING",
    "MESSAGE_TYPE_NONEXIST",
    "WRONG_MESSAGE",
    "IE_NONEXIST",
    "INVALID_IE_CONTENTS",
    "WRONG_CALL_STATE",
    "RECOVERY_ON_TIMER_EXPIRE",
    "MANDATORY_IE_LENGTH_ERROR",
    "PROTOCOL_ERROR",
    "INTERWORKING",
    "ORIGINATOR_CANCEL",
    "CRASH",
    "SYSTEM_SHUTDOWN",
    "LOSE_RACE",
    "MANAGER_REQUEST",
    "BLIND_TRANSFER",
    "ATTENDED_TRANSFER",
    "ALLOTTED_TIMEOUT",
    "USER_CHALLENGE",
    "MEDIA_TIMEOUT",
    "PICKED_OFF",
    "USER_NOT_REGISTERED",
    "PROGRESS_TIMEOUT",
    "GATEWAY_DOWN"
]
