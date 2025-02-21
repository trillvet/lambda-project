def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': 'Second attempt today after updating the build spec yaml. Was it because I was missing the folder in S3?'
    }