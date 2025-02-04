"""
Test record
"""

from pygrestqlambda.db.record import Record

def test_record():
    """
    Verify record class can be initialised correctly
    """
    record = Record()
    assert not record.conn
