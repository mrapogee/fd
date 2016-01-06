
import requests

apiKey = "AIzaSyAUNC1ZouF1YestfrHC_A-WF2aqUBM3vrY"
location = "http://test.test/"

def auth (url):
    return url + "&apiKey=" + apiKey

def toQuery(options):
    return "&".join(map(lambda e: e + '=' + str(options[e]), options.keys()))

def make (path, options):
    return auth(location + path + '?' + toQuery(options))


print make('test/test', {'sup': 'dog'})
