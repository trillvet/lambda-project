def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': 'Last time testing this today to see if my function is updated after doing a local git-commit on my computer.'
    }