#!/usr/bin/env python
# coding: utf-8

# In[147]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd


# In[148]:


# Set the executable path and initialize the chrome browser in splinter
executable_path = {'executable_path': '/Users/jcp/.wdm/drivers/chromedriver/mac64/86.0.4240.22/chromedriver'}
browser = Browser('chrome', **executable_path)


# In[3]:


# Visit the mars nasa news site
url = 'https://mars.nasa.gov/news/'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)


# In[4]:


# Set up html parser
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('ul.item_list li.slide')


# In[5]:


# Scrape title 
slide_elem.find("div", class_='content_title')


# In[6]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find("div", class_='content_title').get_text()
news_title


# In[7]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_="article_teaser_body").get_text()
news_p


# ### Featured Images

# In[8]:


# Visit URL
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)


# In[9]:


# Find and click the full image button
full_image_elem = browser.find_by_id('full_image')
full_image_elem.click()


# In[10]:


# Find the more info button and click that
browser.is_element_present_by_text('more info', wait_time=1)
more_info_elem = browser.links.find_by_partial_text('more info')
more_info_elem.click()


# In[11]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[12]:


# Find the relative image url
img_url_rel = img_soup.select_one('figure.lede a img').get("src")
img_url_rel


# In[13]:


# Use the base URL to create an absolute URL
img_url = f'https://www.jpl.nasa.gov{img_url_rel}'
img_url


# In[14]:


df = pd.read_html('http://space-facts.com/mars/')[0]
df.columns=['description', 'value']
df.set_index('description', inplace=True)
df


# In[15]:


df.to_html()


# In[16]:


# Visit the weather website
url = 'https://mars.nasa.gov/insight/weather/'
browser.visit(url)


# In[17]:


# Parse the data
html = browser.html
weather_soup = soup(html, 'html.parser')


# In[18]:


weather_table = weather_soup.find('table', class_='mb_table')
print(weather_table.prettify())


# In[149]:


# 1. Use browser to visit the URL 
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)


# In[150]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
# set up parser
html = browser.html
mars_soup = soup(html, 'html.parser')


# In[151]:


# loop
for i in range(4):
    # create dictionary
    hemispheres = {}
    # click hemisphere title
    browser.links.find_by_partial_text('Hemisphere')[i].click()
    # redefine soup/html page
    hemi_html = browser.html
    hemi_soup = soup(hemi_html, 'html.parser')
    # scrape title
    img_title = hemi_soup.find('h2', class_="title").get_text()
    # scrape image
    img_url = hemi_soup.find('a', text="Sample").get('href')
    # append to dictionary
    hemispheres['img_url'] = img_url
    hemispheres['img_title'] = img_title
    # append hemispheres to list
    hemisphere_image_urls.append(hemispheres)
    # return to first page
    browser.back()
    


# In[152]:


hemisphere_image_urls


# In[153]:


# 5. Quit the browser
browser.quit()


# In[ ]:




