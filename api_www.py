'''from urllib.request import urlopen

def getsource(url):
    response = urlopen (url)
    html = response.read()
    return html.decode()

html = getsource('http://www.uol.com.br')
#print(html)


from html.parser import HTMLParser
class myParser (HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr in attrs:
                if attr [0] == 'href':
                    print(attr[1])


parser = HTMLParser()
parser.feed(html)

parser = myParser()
parser.feed(html)'''