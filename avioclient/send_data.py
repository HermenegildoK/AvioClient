# -*- coding: utf-8 -*-
import requests


class SendControls(object):
    _URL = None
    _session = None

    def __init__(self, server_url):
        self._URL = server_url
        self._session = requests.Session()

    def post_data(self, endpoint, data=None):
        resp = self._session.post(
            self._URL + endpoint,
            json=data
        )
        if resp.status_code == requests.codes.ok:
            return resp.json()
        return {}

    def get_data(self, endpoint):
        resp = self._session.get(
            self._URL + endpoint
        )
        if resp.status_code == requests.codes.ok:
            return resp.json()
        return {}







