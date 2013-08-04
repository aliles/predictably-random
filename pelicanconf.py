#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Aaron Iles'
SITENAME = 'Predictably Random'
SITEURL = 'http://www.aaroniles.net'

TIMEZONE = 'Australia/Canberra'

DEFAULT_LANG = 'en'
DEFAULT_PAGINATION = 10

ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

# Feed generation is usually not desired when developing
FEED_DOMAIN = SITEURL
FEED_ATOM = 'feeds/atom.xml'
FEED_ALL_ATOM = FEED_ATOM
FEED_RSS = 'feeds/rss.xml'
FEED_ALL_RSS = FEED_RSS
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.rss.xml'
TRANSLATION_FEED_ATOM = None
TRANSLATION_FEED_RSS = None

# Blogroll
LINKS =  (('Python', 'http://python.org/'),
          ('Pelican', 'http://getpelican.com/'),
          ('Travis', 'https://travis-ci.org'),
          ('Heroku', 'https://www.heroku.com'))

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/aliles'),
          ('github', 'https://github.com/aliles'),
          ('linkedin', 'https://www.linkedin.com/in/aliles'))

# Theme
THEME = 'theme'
DISQUS_SITENAME = None
GOOGLE_ANALYTICS = None
GITHUB_URL = 'https://github.com/aliles'

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
