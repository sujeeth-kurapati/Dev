import boto3
from pprint import pprint


client = boto3.client('events')


def event_publish():
    response = client.put_events(
    Entries=[
        {
            'Source': 'sample',
            'Resources': [
                'string',
            ],
            'DetailType': 'sample notification from local',
            'Detail': '{"message": "Hello World!"}',
            'EventBusName': 'Sample_Event_Bus',
        },
    ],
    )
    pprint(response)


if __name__ == "__main__":
    event_publish()