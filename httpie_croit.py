"""
croit auth plugin for HTTPie
"""
from httpie.plugins import AuthPlugin
from urllib.parse import urlsplit, urlunsplit
import requests

__version__ = '1.0.0'
__author__ = 'Paul Emmerich'
__licence__ = 'BSD'

"""
Implements croit authentication which is basically just a
OAuth2 Bearer token acquired via client_credentials.
"""
class CroitAuth:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __call__(self, req):
        token = self.get_token(req)
        req.headers['Authorization'] = 'Bearer ' + token
        return req

    def get_token(self, orig_req):
        url = list(urlsplit(orig_req.url))
        url[2] = '/api/auth/login'
        url = urlunsplit(url)
        req = requests.post(
            url,
            data={'grant_type': 'client_credentials'},
            auth=(self.username, self.password)
        )
        return req.json()['access_token']

class CroitAuthPlugin(AuthPlugin):
    name = 'croit auth'
    auth_type = 'croit'
    description = 'croit API authentication'

    def get_auth(self, username, password):
        return CroitAuth(username, password)
