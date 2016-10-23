"""Get links to all articles at brainpickings.org"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

DRIVER = webdriver.Chrome()


def get_page(page=1):
    brain_pickings_url = 'http://brainpickings.org'
    DRIVER.get(brain_pickings_url + '/page/%d' % page)


def get_article_links(page=1):
    content = DRIVER.find_elements_by_xpath('//h1[@class="entry-title"]/a')
    # Get all links
    for elem in content:
        print elem.get_attribute('href')


def get_all_article_links():
    for page in xrange(1, 1575):
        get_page(page)
        get_article_links(page)

get_all_article_links()
