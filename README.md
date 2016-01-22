Python wrapper for P2P Content Services
------------------

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

To run tests:

    $ python setup.py test
    
### Example API call

This is an example call to create a content item. It is using all of the known custom parameters.

    p2p = get_connection()
    
    htmlstory_data = {
        'slug': "la-test-htmlstory-20160121",
        'body': "Lorem ipsum dolor...",
        'title': "Test HTML Story",
        'content_item_state_code': "working",
        'content_item_type_code': 'htmlstory',
        'custom_param_data': {
            'htmlstory-rhs-column-ad-enable': 'true', # Default `true` enables the right ad rail on html stories.
            'htmlstory-top-leaderboard-enable': 'true', # Default `true` enables the top ad leaderboard to display on html stories.`
            'htmlstory-headline-enable': 'true', # Default `true` enables the headline to display on html stories.
            'htmlstory-byline-enable': 'true', # Default `true` enables the byline to display on html stories. 
            'disable-publication-date': 'false', # Default `false` enables the display time to display on html stories. 
            'disable-dateline': 'false', # Default `false` keeps the dateline visible on content items
            'comments-panel-title': 'Comment on this article', # A string that modifies the title of the comments panel
        }
    }

    p2p.update_content_item(htmlstory_data)

Some documentation for the P2P API can be found [here](http://content-api.p2p.tribuneinteractive.com/docs/content_items).
