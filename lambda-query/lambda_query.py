import boto3
import json

table = boto3.resource(
    'dynamodb'
).Table('CafeSalesData')

def lambda_handler(event, context):

    params = event.get(
        'queryStringParameters'
    )

    # Buscar una venta por ID
    if params and 'id' in params:

        response = table.get_item(
            Key={
                'TransactionID': params['id']
            }
        )

        data = response.get(
            'Item',
            {}
        )

    # Mostrar máximo 50 ventas
    else:

        response = table.scan(
            Limit=50
        )

        data = response.get(
            'Items',
            []
        )

    return {

        'statusCode': 200,

        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Methods': '*'
        },

        'body': json.dumps(data)

    }