"""
Test Lambda Function proxy integration responses
"""

import json
from base64 import b64decode
from pygrestqlambda.aws.lambda_function.proxy_integration_response import (
    LambdaFunctionProxyIntegrationResponse
)

def test_plain_text():
    """
    Test non-base64 plain text payload
    """
    response = LambdaFunctionProxyIntegrationResponse(
        body='plain text'
    )
    payload = response.get_payload()
    assert not payload['isBase64Encoded']
    assert payload['headers']['Content-Type'] == 'text/plain'
    assert payload['body'] == 'plain text'


def test_json():
    """
    Test non-base64 JSON payload
    """
    response = LambdaFunctionProxyIntegrationResponse(
        body={'item':'example'}
    )
    payload = response.get_payload()
    assert not payload['isBase64Encoded']
    assert payload['headers']['Content-Type'] == 'application/json'
    assert json.loads(payload['body'])['item'] == 'example'


def test_base64():
    """
    Test base64 payload
    """
    response = LambdaFunctionProxyIntegrationResponse(
        body=b'plain text to be base64 encoded',
        headers={'Content-Type': 'application/pdf'},
        is_base64_encoded=True,
    )
    payload = response.get_payload()
    assert payload['isBase64Encoded']
    assert payload['headers']['Content-Type'] == 'application/pdf'
    assert b64decode(payload['body']) == b'plain text to be base64 encoded'
