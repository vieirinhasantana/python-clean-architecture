from datetime import datetime
from bson import ObjectId


def encoder_object(o):
    if type(o) == ObjectId:
        return str(o)
    elif type(o) == datetime:
        return o.isoformat()
    return o.__str__
