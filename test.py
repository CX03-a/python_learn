from bs4 import BeautifulSoup
import urllib.request
import csv
urlpage =  'http://www.yzhmyy.com/columns/?id=88'
# 获取网页内容，把 HTML 数据保存在 page 变量中
page = urllib.request.urlopen(urlpage)
# 用 Beautiful Soup 解析 html 数据，
# 并保存在 soup 变量里
soup = BeautifulSoup(page, 'html.parser')
#print(soup)
employment = soup.find('text'=='聘', attrs={'class': 'news_list'})
print(employment)
# 还没写完
