import json

def lambda_handler(event, context):
    # return "Hello this lambda was deployed from SamTemplate"
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
        }),
    }