#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Aaron Iles'
AUTHOR_EMAIL = 'aaron.iles@gmail.com'
SITENAME = 'Predictably Random'
SITEURL = 'http://www.aaroniles.net'

TIMEZONE = 'Australia/Canberra'

DEFAULT_LANG = 'en'
DEFAULT_PAGINATION = 3

ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

SUMMARY_MAX_LENGTH = None

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

# Powered By
LINKS =  (('python', 'http://python.org'),
          ('pelican', 'http://getpelican.com'),
          ('bootstrap', 'http://getbootstrap.com'),
          ('font awesome', 'http://fortawesome.github.io/Font-Awesome/'),
          ('travis', 'https://travis-ci.org'),
          ('heroku', 'https://www.heroku.com'),
          ('ifttt', 'https://ifttt.com'))

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/aliles'),
          ('github', 'https://github.com/aliles'),
#         ('dropbox', 'http://db.tt/76kN97G'),
#         ('google-plus', 'https://plus.google.com/110197178230796133534'),
          ('linkedin', 'https://www.linkedin.com/in/aliles'))

# Theme
THEME = 'theme'
DISQUS_SITENAME = 'aaronilesnet'
GOOGLE_ANALYTICS = 'UA-43019090-1'
# GITHUB_URL = 'https://github.com/aliles'
# GOOGLE_CUSTOM_SEARCH_SIDEBAR = '011005344798390208422'

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
