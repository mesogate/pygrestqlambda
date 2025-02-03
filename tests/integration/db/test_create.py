"""
Test record creation
"""

from psycopg.rows import dict_row

def test_create(db):
    """
    Verify that records can be created
    """
    db.row_factory = dict_row
    result = db.execute('SELECT 5 + 3 AS result;').fetchone()
    assert result['result'] == 8
