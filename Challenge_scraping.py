
# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager

# Set the executable path and initialize the chrome browser in splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path)



def hemispheres(browser):
    # 1. Use browser to visit the URL 
    url = 'https://marshemispheres.com/'

    browser.visit(url)
    html = browser.html
    names_soup = soup(html, 'html.parser')

    # 2. Create a list to hold the images and titles.
    hemisphere_image_urls = []

    
    # 3. Write code to retrieve the image urls and titles for each hemisphere.
    for i in range(4):
        #create empty dictionary
        hemispheres = {}
        element=browser.find_by_css('img.thumb')[i]
        print(element)
        img_url = element['src']
        print(img_url)
        title = browser.find_by_css("h3")[i].text
        print(title)
        hemispheres["img_url"] = img_url
        hemispheres["title"] = title
        hemisphere_image_urls.append(hemispheres)
    
       # browser.back()
    return(hemisphere_image_urls)

def new_func(hemisphere_image_urls):
    return hemisphere_image_urls


def scrape_hemisphere(html_text):
    # parse html text
    hemi_soup = soup(html_text, "html.parser")
    # adding try/except for error handling
    try:
        title_elem = hemi_soup.find("h3").get_text()
        img_elem = hemi_soup.find(class_= "thumb").get("src")
    except AttributeError:
        # Image error will return None, for better front-end handling
        title_elem = None
        sample_elem = None
    hemispheres = {
        "title": title_elem,
        "img_url": img_elem
    }
    print (hemispheres)
