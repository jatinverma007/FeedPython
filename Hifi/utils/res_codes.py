__author__ = 'jatin@gmail.com'

from copy import copy

STATUS_CODE = "code"
MESSAGE = "msg"
DATA = 'data'

INVALID_POST_DATA = "7700"

RESPONSE_LOOKUP = {
     INVALID_POST_DATA: {
        STATUS_CODE: int(INVALID_POST_DATA),
        MESSAGE: "Invalid or no data provided."
    },
}

def get_response_dict(lookup, data=None, substitute=None):
    response_data = copy(RESPONSE_LOOKUP.get(lookup, {
        STATUS_CODE: 0,
        MESSAGE: "Something Went Wrong",
        DATA: ''
    }))
    if data is not None:
        response_data[DATA] = data
    if substitute:
        response_data[MESSAGE] = response_data[MESSAGE] % substitute
    return response_data

