from tests.test_second import SecondLambdaTestCase


class TestSuccess(SecondLambdaTestCase):

    def test_success(self):
        self.assertEqual(self.HANDLER.handle_request(dict(), dict()), {'statusCode': 404})

