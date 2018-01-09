import urllib, re, requests

url = "http://daily.zhihu.com/"
def getHtml(url: str):
    header = {"User_Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36 "}
    request = urllib.request.Request(url, headers = header)
    response = urllib.request.urlopen(request)
    text = response.read()
    return text

def getUrls(html: str):
    pattern = re.compile('<a href="/story/(.*?)".*?>')
    items = re.findall(pattern, html)
    urls = ["http://daily.zhihu.com/story/"+item for item in items]
    return urls

def getContent(url: str):
    new_html = getHtml(url).decode(encoding = "utf-8")
    title_pattern = re.compile('<h1 class="headline-title">(.*?)</h1>')
    titles = re.findall(title_pattern, new_html)
    for title in titles: print(title)
    content_pattern = re.compile('<div class="content">([\d\D]*?)</div>')
    search_result = re.findall(content_pattern, new_html)
    content = re.sub("<.*?>", "", search_result[0])
    content = re.sub("&.*?;", "", content)
    print(content)

if __name__ == "__main__":
    html = getHtml(url).decode(encoding = "utf-8")
    urls = getUrls(html)
    for string in urls:
        getContent(string)
