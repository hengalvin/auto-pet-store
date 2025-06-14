from enum import IntEnum

class StatusCode(IntEnum):
    SUCCESS = 200
    CREATED = 201
    NO_CONTENT = 204
    BAD_REQUEST = 400
    NOT_FOUND = 404
    INTERNAL_ERROR = 500