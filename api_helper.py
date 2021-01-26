import requests
from data import base_url, headers


def get_employee_data(employee_id):
    return requests.get(base_url + f'employee/{employee_id}', headers=headers)


def post_employee_data(data):
    return requests.post(base_url + 'create', headers=headers, json=data)
