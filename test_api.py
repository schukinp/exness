from api_helper import get_employee_data, post_employee_data
from faker import Faker


class TestAPI:
    def test_get_employee_data_is_successful(self):
        request = get_employee_data('1')
        assert request.status_code == 200
        assert request.json()['status'] == "success"
        assert request.json()['data']['employee_name'] == 'Tiger Nixon'
        assert request.json()['data']['employee_salary'] == 320800
        assert request.json()['data']['employee_age'] == 61
        assert request.json()['message'] == "Successfully! Record has been fetched."

    def test_get_employee_data_employee_doesnt_exist(self):
        request = get_employee_data('100')
        assert request.status_code == 200
        assert request.json()['status'] == "success"
        assert request.json()['data'] is None
        assert request.json()['message'] == "Successfully! Record has been fetched."

    def test_post_employee_is_successfully_created(self):
        name = Faker().first_name()
        salary = '100'
        age = '20'
        data = {'name': name,
                'salary': salary,
                'age': age}
        request = post_employee_data(data)
        assert request.status_code == 200
        assert request.json()['status'] == "success"
        assert request.json()['data']['name'] == name
        assert request.json()['data']['salary'] == salary
        assert request.json()['data']['age'] == age
        assert request.json()['data']['id'] is not None
        assert request.json()['message'] == "Successfully! Record has been added."
