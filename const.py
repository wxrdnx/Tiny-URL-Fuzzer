#!/usr/bin/python3

PARSERS = {
    'Python.urlparse'      :'self.urlparse', 
    'PHP.parseurl'         :'url.php', 
    'Ruby.uri'             :'url.rb', 
    'Ruby.addressable/uri' :'url.addressable.rb', 
    'Perl.URI'             :'url.pl', 
    'NodeJS.url'           :'url.js', 
    'Java.net.URL'         :'url.class', 
    'Go.net/url'           :'url.go'
}

REQUESTERS = {
    'Python.httpclient'     :'self.httpclient', 
    'Python.urllib'         :'self.urllib', 
    'Python.requests'       :'self.requests', 
    'PHP.open'              :'get.php', 
    'PHP.curl'              :'get.curl.php', 
    'Ruby.Net/HTTP'         :'get.rb', 
    'Ruby.open_uri'         :'get.open.rb', 
    'Perl.LWP'              :'get.pl', 
    'NodeJS.http'           :'get.js', 
    'Java.URL'              :'get.class', 
    'Go.net/http'           :'get.go'
}
