import requests
from typing import Dict, Optional

def http_request(url: str, method: str = "GET", headers: Optional[Dict[str, str]] = None, params: Optional[Dict[str, str]] = None, json: Optional[Dict[str, str]] = None, data: Optional[Dict[str, str]] = None) -> requests.Response:
    """Makes an HTTP request and returns the response object.

    Args:
        url: The URL to make the request to.
        method: The HTTP method to use (e.g. "GET", "POST").
        headers: Optional dictionary of headers to include in the request.
        params: Optional dictionary of query parameters to include in the request.
        json: Optional JSON data to include in the request body.
        data: Optional form data to include in the request body.

    Returns:
        A requests.Response object containing the server's response to the request.
    """
    response = requests.request(method=method, url=url, headers=headers, params=params, json=json, data=data)
    response.raise_for_status()
    return response
