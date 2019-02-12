import re
import urllib.request

url = "http://goo.gl/U7mSQl"
html = urllib.request.urlopen(url)
html_contents = str(html.read())
id_results = re.findall(r"([A-Za-z0-9]+\*\*\*)", html_contents)

for result in id_results:
    print (result)


import urllib.request
import re

url = "https://www.google.com/googlebooks/uspto-patents-grants-text.html"
html = urllib.request.urlopen(url)
html_contents = str(html.read().decode("utf8"))

url_list = re.findall(r"(http)(.+)(zip)", html_contents)
for url in url_list:
    print("".join(url)) #출력된 Tuple 형태 데이터 str으로 join


import urllib.request
import re

url = "https://finance.naver.com/item/main.nhn?code=005930"
html = urllib.request.urlopen(url)
html_contents = str(html.read().decode("ms949"))

url_list = re.findall("(\<dl class=\"blind\"\>)([\s\S]+?)(\<\/dl\>)", html_contents)

samsung_index =  url_list[0][1]
print(samsung_index)
index_list = re.findall("(\<dd\>)([\s\S]+?)(\<\/dd\>)", samsung_index)

print(index_list)

for index in index_list:
    print (index[1])
