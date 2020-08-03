#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 17:16:27 2020

@author: johngillan
"""

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
import pandas as pd
import re
import sys

def get_episodes(show, sleep_time):
    
    driver = webdriver.Chrome('./chromedriver')
    driver.set_window_size(1000, 1000)
    
    url = 'https://www.imdb.com/?ref_=nv_home'
    driver.get(url)
    
    # search for show
    search_box = driver.find_element_by_id('suggestion-search')
    search_box.clear()
    search_box.send_keys(show)
    search_box.send_keys(Keys.RETURN)
    
    time.sleep(sleep_time)
    
    # click on show (first result)
    driver.find_element_by_xpath(".//table[@class='findList']/tbody[1]/tr[1]/td[1]/a[1]").click()
    
    time.sleep(sleep_time)
    
    num_episodes_text = driver.find_element_by_xpath(".//span[@class='bp_sub_heading']").text
    num_episodes = re.findall(r'\d+', num_episodes_text)[0]
    
    # click on link to last season
    driver.find_element_by_xpath(".//div[@class='seasons-and-year-nav']/div[3]/a[1]").click()
    
    time.sleep(sleep_time)
    
    # select menu for first season
    driver.find_element_by_xpath(".//select[@id='bySeason']/option[1]").click()
    
    time.sleep(sleep_time*2) # need extra long sleep time here for select menu to work
    
    # click on link to individual episodes
    driver.find_element_by_xpath(".//div[@class='info']/strong[1]/a[1]").click()
    
    episodes = []    

    while True:
        time.sleep(sleep_time)
        
        season, ep_num = driver.find_element_by_xpath(".//div[@class='bp_heading']").text.split(" | ")
        title = driver.find_element_by_xpath(".//div[@class='title_wrapper']/h1[1]").text
        airdate = pd.to_datetime(driver.find_element_by_xpath(".//div[@class='title_wrapper']/div[@class='subtext']/a[last()]").text.split("aired ")[1])
        rating = driver.find_element_by_xpath(".//div[@class='ratingValue']/strong[1]/span[1]").text
        votes = driver.find_element_by_xpath(".//div[@class='imdbRating']/a[1]/span[1]").text
        description = driver.find_element_by_xpath(".//div[@class='summary_text']").text
        
        episodes.append({
            "season" : re.findall(r'\d+', season)[0],
            "number" : re.findall(r'\d+', ep_num)[0],
            "title" : title,
            "airdate" : airdate,
            "rating" : rating,
            "votes" : votes,
            "description" : description
        })
        
        print("Progress: {}".format("" + str(len(episodes)) + '/' + num_episodes) + " episodes")

        #Clicking on the "next episode" button
        if len(episodes) < int(num_episodes):
            driver.find_element_by_xpath(".//a[@class='bp_item np_next']").click()
        else:
            print("Finished")
            break

    return pd.DataFrame(episodes)

# get name of show from command line argument
show = sys.argv[1]
sleep_time = 2

df = get_episodes(show, sleep_time)

df.to_csv('./' + show + '_episodes.csv', index=False)

