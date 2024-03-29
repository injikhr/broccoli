import requests
import json
from django.conf import settings
from ..errors import DIDReqError

def did_get_req(path, req_param=None):
    res = requests.get(f"http://{settings.DID_HOST}:{settings.DID_PORT}{path}", params=req_param)
    body = json.loads(res.text)
    if res.status_code >= 400 or body['error'] is not None:
        raise DIDReqError(res.status_code, body['error'])
    return body['content']

def did_post_req(path, req_body):
    res = requests.post(f"http://{settings.DID_HOST}:{settings.DID_PORT}{path}", json=req_body)
    body = json.loads(res.text)
    if res.status_code >= 400 or body['error'] is not None:
        raise DIDReqError(res.status_code, body['error'])
    return body['content']
