__author__ = 'bernardo'
import os
import cgi
import Cookie
import sys
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
cookies = []

def ClearCookies(self):
    cookies = []


def WriteCookie(self, key, value):
    form = cgi.FieldStorage()
    c = Cookie.SimpleCookie()
    c[key] = value
    return c.output(header='')


def ReadCookie(self, key):
    if 'cookie' in self.headers:
        c = Cookie.SimpleCookie(self.headers['cookie'])
        return str(c[key].value)


def getCookies(self):
    return cookies

