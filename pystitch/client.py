import requests


class PyStitch:
    BASE_URL = 'https://api.stitchdata.com/v4'

    def __init__(self, token):
        self.token = token

    def _construct_headers(self) -> dict:
        headers = requests.utils.default_headers()
        headers['User-Agent'] = 'python-pystitch'
        headers['Authorization'] = f'Bearer {self.token}'
        headers['Content-Type'] = 'application/json'
        return headers

    def _get(self, url_suffix: str, params: dict = None) -> dict:
        url = self.BASE_URL + url_suffix
        headers = self._construct_headers()
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()

    def _post(self, url_suffix: str, params: dict = None, data: dict = None) -> dict:
        url = self.BASE_URL + url_suffix
        headers = self._construct_headers()
        response = requests.post(url, headers=headers, params=params, data=data)
        response.raise_for_status()
        return response.json()

    def list_sources(self) -> list:
        resp = self._get(url_suffix='/sources')
        return resp

    def start_replication_job(self, source_id: int) -> dict:
        url_suffix = f"/sources/{source_id}/sync"
        resp = self._post(url_suffix=url_suffix)
        return resp
