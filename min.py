from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

YOUTUBE_TRENDING_URL = "https://www.youtube.com/feed/trending"

def get_driver():
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--disable-dev-shm-useage')
  driver = webdriver.Chrome(options=chrome_options)
  return driver

def get_videos():
  VIDEO_DIV_TAG = 'ytd-video-renderer'
  driver.get(YOUTUBE_TRENDING_URL)
  videos = driver.find_elements(By.TAG_NAME, VIDEO_DIV_TAG)
  return videos

def parse_video(video):
  title_tag = video.find_element(By.ID, 'video-title')
  title = title_tag.text
  url = title_tag.get_attribute('href')
  
  thumbnail_tag = video.find_element(By.TAG_NAME, 'img')
  thumbnail_url = thumbnail_tag.get_attribute('src')

  channel_div = video.find_element(By.CLASS_NAME, 'ytd-channel-name')
  channel_name = channel_div.text
  
  description = video.find_element(By.ID, 'description-text').text

  return {
    'title': title,
    'url': url,
    'thumbnail_url': thumbnail_url,
    'channel': channel_name,
    'description': description
  }







if __name__ == "__main__":
  print("Creating driver")
  driver = get_driver()

  print('Fetching the page')
  driver.get(YOUTUBE_TRENDING_URL)

  print( 'Get the video divs')
  

  driver.find_elements(By.TAG_NAME,VIDEO_DIV_TAG)

  print(f'Found {len(VIDEO_DIV_TAG)} videos')

  print('Parsing the first video')

  # title, url, thumbnail_url, channel, views, uploaded, description

  video =videos [0]

  title_tag = video.find_element(By.ID, 'video-title')
  title = title.tag.text
  url = title_tag.get_attribute('href')

  thumbnail_tag = video.find_element(By.Tag_name,'img')
  thumbnail_url = thumbnail_tag.get_attribute('src')

  channel_div = video.find_element(By.CLASS_NAME,'ytd-channel-name')
  channel_name
  description = video.find_element(By.ID, '')

  


