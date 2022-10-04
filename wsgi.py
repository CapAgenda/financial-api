from webob import Request
from . import jump

def application(environ, start_response):
    request = Request(environ)
    path = request.path
    ua = request.user_agent
    if path == "/test":
        start_response('200 OK', [('Content-Type', 'text/plain')])
        yield bytes(f"in dev: path/user agent:|{path}|{ua}|\n",encoding='utf8')
 
    else:
        start_response('200 OK', [('Content-Type', 'text/html')])
        yield bytes(f"hello world",encoding='utf8') 
