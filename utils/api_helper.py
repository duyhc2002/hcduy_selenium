import logging
from typing import Any, Dict, Optional
import requests
from utils.config_reader import ConfigReader
#logger = logging.getLogger(__name__)

class APIHelper:
    def __init__(
        self,
        base_url:None,
        timeout: float = 10,
        headers: Optional[Dict[str, str]]= None,):

        self.base_url = base_url
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update(headers or {"Accept": "application/json"})

    def request(self, method, endpoint, params=None, json_data=None, headers=None, timeout=None):
        endpoint = endpoint.lstrip("/")
        url = self.base_url + "/" + endpoint

        response = self.session.request(
            method = method,
            url = url,
            params = params,
            json = json_data,
            headers = headers,
            timeout = timeout
        )

        print("Response status: %s", response.status_code)

        return response
    
    def get(self, endpoint, params=None):
        response = self.request(
            method="GET",
            endpoint=endpoint,
            params=params
        )
        return response
    
    def post(self, endpoint, json_data=None):
        response = self.request(
            method="POST",
            endpoint=endpoint,
            json_data=json_data
        )
        return response
    
    def put(
        self, 
        endpoint: str, 
        json_data:Optional[Dict[str, Any]] = None
    ) -> requests.Response:
        return self.request("PUT", endpoint, json_data=json_data)
    
    def patch(
        self, 
        endpoint: str, 
        json_data:Optional[Dict[str, Any]] = None,
    ) -> requests.Response:
        return self.request("PATCH", endpoint, json_data=json_data)
    
    def delete(self, endpoint: str) -> requests.Response:
        return self.request("DELETE", endpoint)
    
    def set_auth_token(self, token: str) -> None:
        self.session.headers["Authorization"] = f"Bearer {token}" 
    
    def close(self) -> None:
        self.session.close()

    close_session = close
