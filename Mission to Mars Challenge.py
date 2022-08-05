{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "ff9a44fd",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import Splinter, BeautifulSoup, and Pandas\n",
    "from splinter import Browser\n",
    "from bs4 import BeautifulSoup as soup\n",
    "import pandas as pd\n",
    "from webdriver_manager.chrome import ChromeDriverManager"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "a5cbf521",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    }
   ],
   "source": [
    "# Set the executable path and initialize the chrome browser in splinter\n",
    "executable_path = {'executable_path': ChromeDriverManager().install()}\n",
    "browser = Browser('chrome', **executable_path)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "fe8a9042",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 1. Use browser to visit the URL \n",
    "url = 'https://marshemispheres.com/'\n",
    "\n",
    "browser.visit(url)\n",
    "html = browser.html\n",
    "names_soup = soup(html, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "265479b7",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 2. Create a list to hold the images and titles.\n",
    "hemisphere_image_urls = []"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "2c7f32b9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "cerberus.html\n",
      "schiaparelli.html\n",
      "syrtis.html\n",
      "valles.html\n"
     ]
    }
   ],
   "source": [
    "# 3. Write code to retrieve the image urls and titles for each hemisphere.\n",
    "names =names_soup.find_all('h3')\n",
    "names\n",
    "#img_url=names_soup.find('a')\n",
    "#img_url\n",
    "for i in names_soup.find_all('div', attrs={'class' : 'item'}):\n",
    "  print(i.a['href'])\n",
    "\n",
    "img_url = i.text\n",
    "      \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "0f7c54ae",
   "metadata": {},
   "outputs": [],
   "source": [
    "hemispheres = {}\n",
    "#hemispheres['img_url'] = f'https://marshemispheres.com/{img_url}'\n",
    "#hemispheres['names'] = names\n",
    "#hemisphere_image_urls.append(hemispheres)\n",
    "\n",
    "\n",
    "hemispheres = {'img_url': img_url, 'names': names}\n",
    "hemisphere_image_urls.append(hemispheres)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "7327e633",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[{'img_url': '\\n\\n\\n\\nValles Marineris Hemisphere Enhanced\\n\\nimage/tiff 27 MB\\nMosaic of the Valles Marineris hemisphere of Mars projected into point perspective, a view similar to that which one would see from a spacecraft. The distance is 2500 kilometers from the surface of…\\n\\n\\n',\n",
       "  'names': [<h3>Cerberus Hemisphere Enhanced</h3>,\n",
       "   <h3>Schiaparelli Hemisphere Enhanced</h3>,\n",
       "   <h3>Syrtis Major Hemisphere Enhanced</h3>,\n",
       "   <h3>Valles Marineris Hemisphere Enhanced</h3>,\n",
       "   <h3>Back</h3>]}]"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "hemisphere_image_urls"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
