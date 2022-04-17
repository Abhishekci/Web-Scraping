from bs4 import BeautifulSoup
import requests

url = 'https://www.naukri.com/data-scientist-jobs-in-india'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all('article', class_="jobTuple bgWhite br4 mb-8")
for list in lists:
    title = lists.find('a', class_="title fw500 ellipsis")
    comp = lists.find('a', class_="subTitle ellipsis fleft")
    location = lists.find('a', class_="ellipsis fleft fs12 lh16 ")
    info = [title, comp, location]
    print(info)
