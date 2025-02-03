"""
Test JSON transformation for lambda proxy integration response
"""

from uuid import uuid4
from datetime import datetime
from pygrestqlambda.aws.lambda_function.json_transform import to_string


def test_uuid():
    """
    Test UUIDs are transformed correctly
    """

    uid = uuid4()

    assert to_string(uid) == str(uid)


def test_datetime():
    """
    Test UUIDs are transformed correctly
    """

    now = datetime.now()

    assert to_string(now) == now.isoformat()
