from commons.log_helper import get_logger
from commons.abstract_lambda import AbstractLambda

_LOG = get_logger('Lambda3-handler')
import json

class Lambda3(AbstractLambda):

    def validate_request(self, event) -> dict:
        pass
        
    def handle_request(self, event, context):
        """
        Explain incoming event here
        """
        # todo implement business logic
        resp = {
           "statusCode": 200,
           "message": "Hello from Lambda"
       }
        return json.dumps(resp)
    

HANDLER = Lambda3()


def lambda_handler(event, context):
    return HANDLER.lambda_handler(event=event, context=context)
