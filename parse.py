#!/usr/bin/env python3

from selectolax.parser import HTMLParser
import locale
import requests
import re

locale.setlocale(locale.LC_ALL, 'en_US.UTF8')
html = requests.get("https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population").text
html_data = HTMLParser(html)
objs = html_data.css("table.wikitable")
table = objs[1] # Use Second Table
rows = table.css("tr")

for row in rows:
    columns = row.css("td")
    if len(columns) == 11:
        position = columns[0].text().rstrip("\n")
        city = columns[1].text().strip()
        city = re.findall('(.*?)(?:\[|$)', city)[0]
        state = columns[2].text().strip()
        state = re.findall('(.*?)(?:\[|$)', state)[0]
        est_pop_2018 = locale.atoi(columns[3].text().strip())
        pop_2010 = locale.atoi(columns[4].text().strip())
        land_area = columns[6].text().rstrip()
        land_area = re.findall('([0-9\.\,]*)', land_area)[0]
        pop_density = columns[8].text().strip()
        pop_density = re.findall('([0-9\.\,]*)', pop_density)[0]
        location = columns[10].text().split('/')[1].strip()
        print(position, city, state, est_pop_2018, pop_2010, land_area, pop_density, location)
