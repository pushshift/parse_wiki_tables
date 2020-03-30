#!/usr/bin/env python3

from selectolax.parser import HTMLParser
import locale
import requests
import re

locale.setlocale(locale.LC_ALL, 'en_US.UTF8')
html = requests.get("https://en.wikipedia.org/wiki/List_of_largest_cities").text
html_data = HTMLParser(html)
objs = html_data.css("table.wikitable")
table = objs[0]
rows = table.css("tr")

for row in rows:
    columns = row.css("td")
    if len(columns) == 10:
        city = re.findall('(.*?)(?:\[|$)', columns[0].text().strip())[0]
        state = re.findall('(.*?)(?:\[|$)', columns[1].text().strip())[0]
        definition = re.findall('(.*?)(?:\[|$)', columns[3].text().rstrip())[0]

        # City Stats
        city_population = re.findall('(.*?)(?:\[|$)', columns[4].text())[0]
        if city_population != "N/A":
            city_population = locale.atoi(city_population)
        city_area = re.findall('(.*?)(?:\[|$)', columns[5].text())[0]
        if city_area != "N/A":
            city_area = locale.atoi(city_area)

        # Metro Stats
        metro_population = re.findall('(.*?)(?:\[|$)', columns[4].text())[0]
        if metro_population != "N/A":
            metro_population = locale.atoi(metro_population)
        metro_area = re.findall('(.*?)(?:\[|$)', columns[5].text())[0]
        if metro_area != "N/A":
            metro_area = locale.atoi(metro_area)

        # Urban Stats
        urban_population = re.findall('(.*?)(?:\[|$)', columns[4].text())[0]
        if urban_population != "N/A":
            urban_population = locale.atoi(urban_population)
        urban_area = re.findall('(.*?)(?:\[|$)', columns[5].text())[0]
        if urban_area != "N/A":
            urban_area = locale.atoi(urban_area)

        print(city, state, definition, city_population, city_area, metro_population, metro_area, urban_population, urban_area)
