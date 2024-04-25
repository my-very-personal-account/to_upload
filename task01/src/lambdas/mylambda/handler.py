from commons.log_helper import get_logger
from commons.abstract_lambda import AbstractLambda

_LOG = get_logger('Mylambda-handler')


class Mylambda(AbstractLambda):

    def validate_request(self, event) -> dict:
        pass
        
    def handle_request(self, event, context):
        """
        Explain incoming event here
        """
        # todo implement business logic
        return {'statusCode': 200, 'message': 'Hello from Lambda'}
    

HANDLER = Mylambda()


def lambda_handler(event, context):
    return HANDLER.lambda_handler(event=event, context=context)
