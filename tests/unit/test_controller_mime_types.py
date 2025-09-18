"""
Test controller for request/response handling
"""

from pygrestqlambda.controller import Controller

def test_content_type_headers_from_accept_headers():
    """
    Test that requesting a specific MIME type returns content of the same MIME type.
    """

    mime_types = [
        'application/pdf',
        'application/json',
        'text/csv',
    ]

    for mime_type in mime_types:
        controller = Controller(event={
            'httpMethod': 'GET',
            'multiValueHeaders': {
                'Accept': [mime_type]
            }
        })

        response_headers = controller.run().get_payload()['headers']

        assert response_headers['Content-Type'] == mime_type
