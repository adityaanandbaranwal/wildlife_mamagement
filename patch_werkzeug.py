# patch_werkzeug.py
import werkzeug.urls
import urllib.parse

if not hasattr(werkzeug.urls, 'url_quote'):
    werkzeug.urls.url_quote = urllib.parse.quote

if not hasattr(werkzeug.urls, 'url_decode'):
    werkzeug.urls.url_decode = urllib.parse.unquote_plus

if not hasattr(werkzeug.urls, 'url_encode'):
    werkzeug.urls.url_encode = urllib.parse.urlencode
