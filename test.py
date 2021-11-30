import requests
from bs4 import BeautifulSoup

YOUTUBE_TRENDING_URL = "https://www.youtube.com/feed/trending"

response = requests.get(YOUTUBE_TRENDING_URL)

print('Status Code', response.status_code)
#print("Output",response.text[:1000])

with open('trending.html','w') as f:
  f.write(response.text)

doc = BeautifulSoup(response.text,'html.parser')

print('Page Title', doc.title)

# Find all the video divs
video_divs = doc.find_all('div',class='ytd-video-renderer')

print(f'Found{len(video_divs)} video')