from falcon import testing
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from falcon_api.app import api


class MyTestCase(testing.TestCase):
    def setUp(self):
        super(MyTestCase, self).setUp()
        self.app = api


class TestPostAPI(MyTestCase):
    def test_201_post_request(self):

        result = self.simulate_post('/v1/users',
                                    headers={
                                        "metric_value": "777777",
                                        "model_id": "523121"
                                    })
        self.assertEqual(result.status_code, 201)

    def test_400_post_request(self):

        result = self.simulate_post('/v1/users',
                                    headers={
                                        "wrong_key": "777777",
                                        "model_id": "523121"
                                    })
        self.assertEqual(result.status_code, 400)

    def test_404_post_request(self):

        result = self.simulate_post('/v1/wrong_path',
                                    headers={
                                        "metric_value": "777777",
                                        "model_id": "523121"
                                    })
        self.assertEqual(result.status_code, 404)