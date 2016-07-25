
# Name: sneakerCrawler
# Author: Bohan Yao
# Starting Date: 7/24/2016
# Description: I am starting this web crawler project for my own purpose of
# buying limited sneakers online. I am new to python and web related programming
# so this could be slow. To get next NMD!!!!

import requests

website_input = input('Give me a website: ')
url = requests.get(website_input)
print ('The input is %s' %(website_input))
print ('The header is %s' %(url.headers))
print ('some content is %s' %(url.content))
