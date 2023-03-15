import urllib.parse, urllib.request
import http.client
import requests

def my_urlparse(url):
    try:
        parsed = urllib.parse.urlparse(url)
        if parsed.port:
            return 'scheme={0}, host={1}, port={2}'.format(parsed.scheme, parsed.netloc, parsed.port)
        else:
            return 'scheme={0}, host={1}, port='.format(parsed.scheme, parsed.netloc)
    except ValueError:
        return 'err'

def my_httplib(url):
    try:
        conn = http.client.HTTPConnection(urlparse(url).netloc)
        conn.request("GET", urllib.parse.urlparse(url).path)
        data = conn.getresponse().read().strip()
        conn.close()
    except Exception:
        data = 'err'
    return data

def my_urllib(url):
    try:
        return urllib.request.urlopen(url).read().strip()
    except Exception:
        return 'err'

def my_requests(url):
    try:
        return requests.get(url).content.strip()
    except Exception:
        return 'err'
