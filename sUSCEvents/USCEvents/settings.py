# -*- coding: utf-8 -*-

# Scrapy settings for USCMaps project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'USCEvents'

SPIDER_MODULES = ['USCEvents.spiders']
NEWSPIDER_MODULE = 'USCEvents.spiders'

# Needed to avoid 403 error
DOWNLOADER_MIDDLEWARES = {'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'USCMaps (+http://www.yourdomain.com)'
