# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 09:17:36 2016

@author: lms_user
"""

# Maruti WebPages
import urllib2
from config import model_codes

for model_code in model_codes:
    url = "http://www.marutisuzuki.com/Maruti-Price.aspx?ModelCode="+ model_code +"&State=DL&City=08"
    print "URL generated for ", model_code
    print "Attempting to get the HTML"
    try:
        page = urllib2.urlopen(url)
        print "Got the HTML for model", model_code
        print "Now writing to file"
        fo = open("Z:\\New folder\\code\\Python\\Maruti\\HtmlPages\\"+model_code+".html", "w+")
        fo.write(page.read())
    except Exception, e:
        print "Exception:", e
        
######################################################
## Extracting the price table from HTML
from bs4 import BeautifulSoup
car_prices = []

for model in model_codes:
    html_file = "Z:\\New folder\\code\\Python\\Maruti\\HtmlPages\\"+ model + ".html"
    fo = open(html_file)
    #Parse the html in the 'page' variable, and store it in Beautiful Soup format
    soup = BeautifulSoup(fo, "lxml")
    
    ### For vitara brezza
    #table_check_columns = soup.find('table', {'class':'tablepl'})
    #table_check_columns.contents[1].contents[5].contents[0].strip()
    
    table = soup.find('table', {'id' : 'ContentPlaceHolder1_dtDealer'})
    
    model_row_value = 2
    while True:
        try:
            car_model_name = table.contents[model_row_value].contents[3].contents[1].string
            car_model_metallic = table.contents[model_row_value].contents[5].contents[1].string
            car_model_non_metallic = table.contents[model_row_value].contents[7].contents[1].string
        
            car_prices.append([car_model_name, car_model_metallic, car_model_non_metallic])
            
            model_row_value += 3
        except IndexError:
            break
  
#import csv
#with open("Z:\\New folder\\code\\Python\\Maruti\\car_price_data.csv", 'w+') as fo:
#    writer = csv.writer(fo)
#    writer.writerows(car_prices)
#    
from pandas import DataFrame
df = DataFrame(car_prices)
df.to_csv('Z:\\New folder\\code\\Python\\Maruti\\car_price_data.csv', index = False, header = False)

