import requests
import json

backend_server_url = 'http://127.0.0.1:8001/api/words/'

def api_call(url, method  ,**kwargs ):
    if method == 'GET':
        try:
            output = requests.get(url)
            output = json.loads(output.content)
        except:
            output = {'ret':False,' result': False}
        return output

    if method == 'POST':
        try:
            output = requests.post(url,data=kwargs)
            output = json.loads(output.content)
        except:
            output = {'ret':False,' result': False}
        return output

    if method == 'PATCH':
        try:
            output = requests.patch(url,data=kwargs)
            output = json.loads(output.content)
        except:
            output = {'ret':False,' result': False}
        return output

    if method == 'DELETE':
        try:
            output = requests.delete(url)
            output = json.loads(output.content)
        except:
            output = {'ret':False,' result': False}
        return output
