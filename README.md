# boto3 bugs

https://boto3.readthedocs.io/en/latest/reference/services/sqs.html

send_message(**kwargs) 
Request Syntax
```
response = client.send_message(
    QueueUrl='string',
    MessageBody='string',
    DelaySeconds=123,
    MessageAttributes={
        'string': {
            'StringValue': 'string',
            'BinaryValue': b'bytes',
            'StringListValues': [
                'string',
            ],
            'BinaryListValues': [
                b'bytes',
            ],
            'DataType': 'string'
        }
    },
    MessageDeduplicationId='string',
    MessageGroupId='string'
)
```

Bug 1:
'DataType' sholud be upper case for 'String'

Bug 2:
'StringListValues' is not workable when running code, error message shows the non-related cloumn for this issue.
e.g.:
```
Traceback (most recent call last):
  File "sqs_example.py", line 35, in <module>
    'DataType': 'Number'
  File "/home/ubuntu/.local/lib/python3.5/site-packages/boto3/resources/factory.py", line 520, in do_action
    response = action(self, *args, **kwargs)
  File "/home/ubuntu/.local/lib/python3.5/site-packages/boto3/resources/action.py", line 83, in __call__
    response = getattr(parent.meta.client, operation_name)(**params)
  File "/home/ubuntu/.local/lib/python3.5/site-packages/botocore/client.py", line 314, in _api_call
    return self._make_api_call(operation_name, kwargs)
  File "/home/ubuntu/.local/lib/python3.5/site-packages/botocore/client.py", line 612, in _make_api_call
    raise error_class(parsed_response, operation_name)
botocore.errorfactory.UnsupportedOperation: An error occurred (AWS.SimpleQueueService.UnsupportedOperation) when calling the SendMessage operation: Message attribute list values in SendMessage operation are not supported.
``` 
  
Solution:
Removed unnessasary fields and use string type to send message in messageAttribues.
Transform your list to sting in order to set sting list in message attributes.

e.g.:
```
results = ['abc', '123', '!%#']
response = queue.send_message(
    MessageBody='Test send message',
    DelaySeconds=0,
    MessageAttributes={
        'result_string': {
            'StringValue': ",".join(results),
            'DataType': 'String'
        },
        'id': {
            'StringValue': '9527',
            'DataType': 'Number'
        }
    }
)
```
Update on 2018/08/23
