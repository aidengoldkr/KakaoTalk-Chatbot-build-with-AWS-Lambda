import json

def lambda_handler(event, context):
    body = json.loads(event['body'])
    user_input = event['userRequest']['utterance']

    #여기에 User_input에 대해 반환 할 여러분만의 로직을 구성해서 결론적으로 result 라는 변수에 저장하시면 됩니다

    return {
    "version": "2.0",
    "template": {
        "outputs": [
            {
                "simpleText": {
                    "text": result
                }
            }
        ]
    }
}
