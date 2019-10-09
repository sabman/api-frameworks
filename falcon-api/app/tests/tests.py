from falcon import testing
from urllib.parse import urlencode
import json
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main import application


class MyTestCase(testing.TestCase):
    def setUp(self):
        super(MyTestCase, self).setUp()
        self.app = application


class TestPostAPI(MyTestCase):
    # def test_create_user_API(self):

    #     dict_body = {"email": "test14user@gmail.com", "password": "password"}
    #     headers = {"Content-Type": "application/json"}

    #     result = self.simulate_post('/api/v1/users',
    #                                 host="127.0.0.1:5000",
    #                                 headers=headers,
    #                                 body=json.dumps(dict_body))

    #     # API returns 201 status code on success
    #     self.assertEqual(result.status_code, 201)

    # def test_login_user_API(self):

    #     dict_body = {"email": "test14user@gmail.com", "password": "password"}
    #     headers = {"Content-Type": "application/json"}

    #     result = self.simulate_get('/api/v1/user/sign_in',
    #                                host="127.0.0.1:5000",
    #                                headers=headers,
    #                                body=json.dumps(dict_body))
    #     self.assertEqual(result.status_code, 200)

    def test_create_user_API(self):

        dict_body = {"value": 666, "model_ref": 666}
        headers = {
            "Content-Type":
            "application/json",
            "authorization":
            "gAAAAABdncwM0vpHtkp1IW4TeRKZLZVQ9viZeJzPp3DZ75yiw9op43i8ATDYYT7OR2nzJCNrubDCi5UmvlgWF_q5pO3S5ZcrDQ=="
        }

        result = self.simulate_post('/api/v1/metrics',
                                    host="127.0.0.1:5000",
                                    headers=headers,
                                    body=json.dumps(dict_body))

        # API returns 201 status code on success
        self.assertEqual(result.status_code, 201)
