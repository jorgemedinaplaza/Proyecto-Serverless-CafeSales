import json
import boto3
import csv

# Clientes AWS
s3 = boto3.client('s3')

dynamodb = boto3.resource('dynamodb')

# Tabla DynamoDB
table = dynamodb.Table('CafeSalesData')

def lambda_handler(event, context):

    print("Evento recibido:")
    print(json.dumps(event))

    # Obtener bucket y archivo enviados por S3
    bucket = event['Records'][0]['s3']['bucket']['name']

    key = event['Records'][0]['s3']['object']['key']

    print(f"Bucket: {bucket}")
    print(f"Archivo: {key}")

    # Descargar archivo desde S3
    response = s3.get_object(
        Bucket=bucket,
        Key=key
    )

    # Leer contenido CSV
    contenido = response['Body'].read().decode('utf-8')

    lector = csv.DictReader(
        contenido.splitlines()
    )

    registros = 0

    # Recorrer filas del CSV
    for fila in lector:

        table.put_item(
            Item={

                'TransactionID':
                fila['Transaction ID'],

                'Item':
                fila['Item'],

                'Quantity':
                fila['Quantity'],

                'PricePerUnit':
                fila['Price Per Unit'],

                'TotalSpent':
                fila['Total Spent'],

                'PaymentMethod':
                fila['Payment Method'],

                'Location':
                fila['Location'],

                'TransactionDate':
                fila['Transaction Date']

            }
        )

        registros += 1

    print(f"Registros cargados: {registros}")

    return {

        'statusCode': 200,

        'body': json.dumps({

            'mensaje':
            'Carga completada',

            'registros':
            registros

        })

    }