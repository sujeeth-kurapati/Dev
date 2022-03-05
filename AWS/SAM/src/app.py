import json
import pprint
import os
import boto3

table_name = os.environ['TABLE_NAME']
rgn = os.environ['REGION_NAME']
dynam = boto3.client('dynamodb',region_name = rgn)

def lambda_handler(event, context):
    # return "Hello this lambda was deployed from SamTemplate"
    pprint.pprint(event)
    scan_results = dynam.scan(TableName=table_name)
    pprint.pprint(scan_results)
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Hello, I am Sujeeth :)",
        }),
    }