from .mocked_requests_list import mocked_requests_json
from json import dumps

def mock_requests_get(*args, **kwargs):
    return mock_requests(args, kwargs, "get")

def mock_requests_post(*args, **kwargs):
    return mock_requests(args, kwargs, "post")

def mock_requests_request(*args, **kwargs):
    return mock_requests(args, kwargs, "request")

# ----------

# Ya que no se si los parametros me vienen desde args o kwargs tengo que usar este diccionario para buscarlos por indice
PARAMS_PLACEMENTS = {
    "get": {
        "url": 0,
        "params": 1,
        "data": 2
    },
    "post": {
        "url": 0,
        "data": 1,
        "json": 2,
        "params": 3
    },
    "put": {
        "url": 0,
        "data": 1,
        "params": 2
    },
    "delete": {
        "url": 0,
        "params": 1,
        "data": 2
    },
    "patch": {
        "url": 0,
        "data": 1,
        "params": 2
    },
    "request": {
        "url": 1,
        "data": 2,
        "params": 3,
        "json": 14
    }
}

def get_mock_requests_params(args, kwargs, mock_type):
    url = kwargs.get("url")
    if not url:
        url_index = PARAMS_PLACEMENTS[mock_type].get("url")
        if url_index and (len(args) - 1 >= url_index):
            url = args[url_index]

    params = kwargs.get("params")
    if not params:
        params_index = PARAMS_PLACEMENTS[mock_type].get("params")
        if params_index and (len(args) - 1 >= params_index):
            params = args[params_index]

    data = kwargs.get("data")
    if not data:
        data_index = PARAMS_PLACEMENTS[mock_type].get("data")
        if data_index and (len(args) - 1 >= data_index):
            data = args[data_index]
            
    json = kwargs.get("json")
    if not json:
        json_index = PARAMS_PLACEMENTS[mock_type].get("json")
        if json_index and (len(args) - 1 >= json_index):
            json = args[json_index]

    return url, params, data, json

def mock_requests(args, kwargs, mock_type):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    url, params, data, json = get_mock_requests_params(args, kwargs, mock_type)

    mocked_request = mocked_requests_json.get(url)
    if mocked_request:
        mock_data = dumps(mocked_request.get("data"))
        if is_valid_mock_data(mock_data, params, data, json):
            return MockResponse(mocked_request.get("response"), mocked_request.get("status"))

    return MockResponse(None, 404)

def is_valid_mock_data(mock_data, params, data, json):
    if not params and not data and not json:
        return True
    return (params and dumps(params) == mock_data) or (data and dumps(data) == mock_data) or (json and dumps(json) == mock_data)
