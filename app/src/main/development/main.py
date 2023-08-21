import json


def main(event, context):
    body = {
        "message": "Hello World!",
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response


if __name__ == "__main__":
    main()
