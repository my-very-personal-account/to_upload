from tests.test_mylambda import MylambdaLambdaTestCase


class TestSuccess(MylambdaLambdaTestCase):

    def test_success(self):
        self.assertEqual(self.HANDLER.handle_request(dict(), dict()), {'statusCode': 200, 'message': 'Hello from Lambda'})

