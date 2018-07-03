# Freiluftkino

## Run the scraper

You need the Chrome webdriver in your path.

`$ python scripts/get.py`

The script will start a headless Chrome to scrape websites.

You'll find a CSV with today's screeinings in the `data` folder and a `screenings.json` in the project root.

## Deployment

Copy the files to a webserver and set up a cron to rebuild the `screenings.json`.

There is `scrips/cron.sh` that you can use in your crontab.

## Website

There is a little web frontend (only index.html) that takes the json and displays it.

## Why?

This is my first web scraping project and I like open air movie theaters.  
I wanted a single place where I can look at what movies are playing in different places.

