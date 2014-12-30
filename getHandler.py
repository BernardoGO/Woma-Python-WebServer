__author__ = 'bernardo'
from BaseHTTPServer import BaseHTTPRequestHandler
import urlparse
from cgi import parse_header, parse_multipart
from urlparse import parse_qs
from BaseHTTPServer import BaseHTTPRequestHandler
import config
import fileHandler
import cookieHandler
import Cookie
import os
import cgi
import sessionManager
import posixpath
import mimetypes
import urllib
import urlparse

def do_GET(self):
    parsed_path = urlparse.urlparse(self.path)
    sessionId = sessionManager.startSession(self)
    par = urlparse.parse_qs(urlparse.urlparse(self.path).query)
    response = fileHandler.read(self, parsed_path.path, [par, None])
    self.send_response(response[0])
    self.send_header('Set-Cookie', cookieHandler.WriteCookie(self, config.__SESSION_COOKIE_NAME__, sessionId))
    self.end_headers()
    self.wfile.write(response[1])
    return


def url_fi2x(s, charset = 'utf-8'):
    if isinstance(s, unicode):
        s = s.encode(charset, 'ignore')
    scheme, netloc, path, qs, anchor = urlparse.urlsplit(s)
    path = urllib.quote(path, '/%')
    qs = urllib.quote_plus(qs, ':&=')
    return urlparse.urlunsplit((scheme,
     netloc,
     path,
     qs,
     anchor))


def guess_typ2e(self, path):
    base, ext = posixpath.splitext(path)
    if self.extensions_map.has_key(ext):
        return self.extensions_map[ext]
    else:
        ext = ext.lower()
        if self.extensions_map.has_key(ext):
            return self.extensions_map[ext]
        return self.extensions_map['']


extensions_map = mimetypes.types_map.copy()
extensions_map.update({'': 'application/octet-stream',
 '.py': 'text/plain',
 '.c': 'text/plain',
 '.h': 'text/plain'})
