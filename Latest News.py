import requests
from bs4 import BeautifulSoup as bs

url="https://www.news18.com/news/"
urlpage=requests.get(url)

web_content=urlpage.text

soup=bs(web_content,"html.parser")

div_tag=soup.find_all("div",{"class":"jsx-3961882050 blog_list_row"})

for news in div_tag:
    print(news.text)
    print("URL:-",str(news).split('href="')[1].split('"')[0])
    print("\n")