import json

def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))

    operations = {
        'DELETE': lambda dynamo, x: dynamo.delete_item(**x),
        'GET': lambda dynamo, x: dynamo.scan(**x),
        'POST': lambda dynamo, x: dynamo.put_item(**x),
        'PUT': lambda dynamo, x: dynamo.update_item(**x),
    }

    operation = event['httpMethod']
    response = {
        'statusCode': '200',
        'body':  'Pferd',
        'headers': {
            'Content-Type': 'application/json'
            }
        }
    return response
    
