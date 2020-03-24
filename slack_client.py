import requests
import json
import logging

HEADERS = {
    'Content-type': 'application/json'
}

def slacker(webhook_url='https://hooks.slack.com/services/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'):
    def slackit(msg):
        logging.info('Sending {msg} to slack'.format(msg=msg))
        payload = {'text': msg + '<https://www.mohfw.gov.in|Click Here> for Details'}
        return requests.post(webhook_url, headers=HEADERS, data=json.dumps(payload))

    return slackit
