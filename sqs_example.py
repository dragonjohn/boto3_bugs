import boto3

# Get the service resource
sqs = boto3.resource('sqs', region_name='us-west-1')

# Get the queue
queue = sqs.get_queue_by_name(QueueName='test-queue')

results = [
  "34e9e",
  "7456b",
  "81293",
  "1a2d2",
  "8ea08"
]
id = '9527'
response = queue.send_message(
    MessageBody='Test send to queue',
    DelaySeconds=0,
    MessageAttributes={
        'list_string': {
            'StringValue': ",".join(results),
            'DataType': 'String'
        },
        'id': {
            'StringValue': id,
            'DataType': 'Number'
        }
    }
)

# The response is NOT a resource, but gives you a message ID and MD5
print(response.get('MessageId'))
print(response.get('MD5OfMessageBody'))
