# Special Offers TinyDeal Scrapy

Scrap Special Offer Products from https://www.tinydeal.com/specials.html using Scrapy

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install some packages needed.

```bash
git clone git@github.com:sustiono/tinydeal-scrapy.git
cd tinydeal-scrapy
pip3 install virtualenv
virtualenv .env
source .env/bin/activate
cd tinydeal/tinydeal
pip install -r requirements.txt
```

## Usage
Choose one of the commands below to get the results in the desired format

```bash
scrapy crawl special_offers -o special_offers.csv
scrapy crawl special_offers -o special_offers.json
scrapy crawl special_offers -o special_offers.xml
```
