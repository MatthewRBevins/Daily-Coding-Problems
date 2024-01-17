from random import randint
chars = ['a','b','c','d',1,2,3,4,5,6,7,8,9,0]
codes = dict()
urls = dict()
url = 'https://matthewrbevins.com'
def shorten(url):
    if not url in urls.keys():
        code = ''
        for i in range(6):
            code += str(chars[randint(0,len(chars)-1)])
        urls[url] = code
        codes[code] = url
    return urls[url]
def restore(short):
    return codes[short]

print(shorten(url))
print(restore(shorten(url)))
