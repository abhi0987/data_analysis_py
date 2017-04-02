import re
import requests
import os
from urllib import request
from bs4 import BeautifulSoup


url = 'https://alpha.wallhaven.cc/search?q=%22{catagory}%22'

print('WELCOME TO -----> WALLHEAVEN <------\n')

print('category avilable :')
print('1.landscape')
print('2.nature')
print('3.winter')
print('4.games')
print('5.cabin')
print('6.mountain')
print('7.switzerland')
print('8.amsterdam')
print('9.italy')

cat = input('Enter a category from above : ')
page_no = input('Enter page serial no : ')

url_ = url.format(catagory = cat) + '&page='+str(page_no)
wall_r = requests.get(url_)
directory = 'C:\\Users\\abhis\\Desktop\\wallpaper_hd'
if not os.path.exists(directory):
    os.mkdir(directory)

path = 'C:\\Users\\abhis\\Desktop\\wallpaper_hd\\{image_id}.{jpg}'

base_url = 'https://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-{id}.{ext}'

if(wall_r.status_code==200):


    wall_soup = BeautifulSoup(wall_r.text,'html.parser')
    for link in wall_soup.findAll('section',{'class':'thumb-listing-page'}):
         for li in  link.find('ul'):
             img_url = (str(li.find('a')))

             id = int(re.search(r'\d+',img_url).group())

             brk_str = base_url.format(id=id,ext='jpg')

             image_id = 'wallhaven-' + str(id)
             print(image_id)

             try:

                 print('Downloading.....' + image_id)
                 req = request.Request(brk_str)
                 req.add_header("User-Agent",
                                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36")
                 conn = request.urlopen(req)

                 f = open(path.format(image_id=image_id,jpg='jpg'), 'wb')
                 f.write(conn.read())
                 f.close()

                 print('\n\t\t\t' + image_id + ' : download completed')
             except :
                 print(' Error in downloading occoured due to wrong extension format')
                 print(' Proceed to next image ....')














