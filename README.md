Python wrapper for P2P Content Services
------------------

### Connection configuration

Configuration settings. Set these values in your environment or your Django settings.

    P2P_API_KEY = your_p2p_api_key
    P2P_API_URL = url_of_p2p_endpoint
    P2P_API_DEBUG = plz  # display an http log
    P2P_PRESERVE_EMBEDDED_TAGS = False # set to false to fix encoding issues with special characters

    # Optional
    P2P_IMAGE_SERVICES_URL = url_of_image_services_endpoint

To get a connection object based on these settings:

    from p2p import get_connection
    p2p = get_connection()

Or you can create a connection object manually. You'll want to do this in order to enable caching.

    from p2p import P2P, cache
    p2p = P2P(
        url='url_of_p2p_endpoint',
        auth_token='your_p2p_api_key',
        debug=False or True,
        image_services_url='url_of_image_services_endpoint',
        cache=cache.DictionaryCache(),
        preserve_embedded_tags=False or True
    )

### Encoding

P2P's database only allows ascii and latin-1 characters. By default this
wrapper will convert titles and bodies passed in through create_content_item or
update_content_item. This can be overridden to disable encoding like so:

    p2p.create_content_item({
        "slug": "la-test-hello-world"
        "title": "Hello world",
        "body": "My safe content."
    }, encoded_fields=None)

Or it can be expanded to apply to more fields:

    p2p.create_content_item({
        "slug": "la-test-hello-world"
        "title": "Hello world",
        "body": "My non latin-1 content 🍔 试 ©."
    }, encoded_fields=("title", "body", "seodescription"))

### Encoding

To run tests:

    $ python setup.py test
