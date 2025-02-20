def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': 'Hello from Lambda! Updated via GitHub pipeline. Trying this again. And Again. And Again.'
    }