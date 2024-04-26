from commons.log_helper import get_logger
from commons.abstract_lambda import AbstractLambda

_LOG = get_logger('Second-handler')


class Second(AbstractLambda):

    def validate_request(self, event) -> dict:
        pass
        
    def handle_request(self, event, context):
        path = event.get('rawPath')
        if path == '/hello':
            return {
             "statusCode": 200,
             "message": "Hello from Lambda"
            }
        return {'statusCode': 404}
    

HANDLER = Second()


def lambda_handler(event, context):
    return HANDLER.lambda_handler(event=event, context=context)
