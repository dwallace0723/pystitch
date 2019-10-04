from datetime import datetime
from typing import Dict, List

import pytz
import requests

from .version import __version__


class PyStitch:
    BASE_URL = 'https://api.stitchdata.com/v4'

    def __init__(self, token):
        self.token = token

    def _construct_headers(self) -> Dict:
        headers = requests.utils.default_headers()
        headers['User-Agent'] = f'python-pystitch/{__version__}'
        headers['Authorization'] = f'Bearer {self.token}'
        headers['Content-Type'] = 'application/json'
        headers["Date"] = datetime.strftime(datetime.utcnow().replace(tzinfo=pytz.UTC), '%a, %d %b %Y %H:%M:%S %Z')
        return headers

    def _get(self, url_suffix: str, params: Dict = None) -> Dict:
        url = self.BASE_URL + url_suffix
        headers = self._construct_headers()
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()

    def _post(self, url_suffix: str, params: Dict = None, data: Dict = None) -> Dict:
        url = self.BASE_URL + url_suffix
        headers = self._construct_headers()
        response = requests.post(url, headers=headers, params=params, data=data)
        response.raise_for_status()
        return response.json()

    def list_destinations(self):
        resp = self._get(url_suffix="/destinations")
        return resp

    def get_source(self, source_id: int) -> Dict:
        resp = self._get(url_suffix=f"/sources/{source_id}")
        return resp

    def list_sources(self) -> List:
        resp = self._get(url_suffix="/sources")
        return resp

    def get_stream_schema(self, source_id: int, stream_id: int) -> Dict:
        resp = self._get(url_suffix=f"/sources/{source_id}/streams/{stream_id}")
        return resp

    def list_streams(self, source_id: int) -> List:
        url_suffix = f"/sources/{source_id}/streams"
        resp = self._get(url_suffix=url_suffix)
        return resp

    def start_replication_job(self, source_id: int) -> Dict:
        url_suffix = f"/sources/{source_id}/sync"
        resp = self._post(url_suffix=url_suffix)
        return resp
