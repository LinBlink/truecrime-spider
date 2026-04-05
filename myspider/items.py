# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyspiderItem(scrapy.Item):

    org_url = scrapy.Field()

    # Jeffrey Dahmer
    main_character_name = scrapy.Field()
    # The Milwaukee Cannibal
    title = scrapy.Field()
    # Jeffrey Dahmer is ...
    content = scrapy.Field()
    # thetruecrimedatabase.com
    source = scrapy.Field()

    header_img_url = scrapy.Field()

    # ["https://xxx.a.jpg","https://..."]
    img_urls_captions = scrapy.Field()

    yt_video_urls = scrapy.Field()

    # Nucleus
    author = scrapy.Field()
    # article created time
    created_at = scrapy.Field()
