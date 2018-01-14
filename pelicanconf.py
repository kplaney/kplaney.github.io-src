#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Katie Planey'
SITENAME = 'From the Ground Up'
SITEURL = 'http://kplaney.github.io'

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('LinkedIn', 'https://www.linkedin.com/in/katieplaney/'),
          ('GitHub', 'https://github.com/kplaney/'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


#katie edited
#plugins
PLUGIN_PATHS = ['/code/pelican-plugins']
#nbconvert error for 'liquid_tags.notebook',
PLUGINS = ['i18n_subsites', 'liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.youtube', 'liquid_tags.vimeo',
           'liquid_tags.include_code', 'related_posts', 'series']
#NOTEBOOK_DIR = 'notebooks'



THEME = '/code/pelican-themes/pelican-bootstrap3'
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
I18N_TEMPLATES_LANG = 'en'
BOOTSTRAP_THEME='flatly'
#SHOW_ARTICLE_CATEGORY=True
#SHOW_DATE_MODIFIED=True
#SHOW_ARTICLE_AUTHOR=False
#DISPLAY_ARTICLE_INFO_ON_INDEX=True
#BOOTSTRAP_NAVBAR_INVERSE=True

#SITELOGO = 'images/my_site_logo.png'
#SITELOGO_SIZE
#BANNER = '/code/kplaney.github.io-src/bridge.jpg'
#BANNER_SUBTITLE = 'Building a data-centric biotech company'
#BANNER_ALL_PAGES = False
GITHUB_USER = 'kplaney'
PYGMENTS_STYLE = 'monokai'


