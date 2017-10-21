import SqlHandler
import ConfigHandler
from WebScraper import Ebay

ebay = Ebay()
config = ConfigHandler.ConfigHandler()

items = []
time_interval = 0


def load_config():
    config.load_config("../data/config.json")


def scrape():
    #DELETING CURRENT DATABASE REMOVE THIS LATER
    SqlHandler.drop_table('../data/web_items.db')
    SqlHandler.create_database('../data/web_items.db')
    
    if config.get_keywords().count is 0:
        print("No keywords set, did you forget to load the config?")

    #Load config
    config.set_config("../data/config.json")
    config.load_config()

    #Scrape sites
    ebay.add_keywords(config.get_keywords())
    ebay.set_pages_to_scrape(config.get_pages_to_scrape())
    ebay.scrape_site()


def get_items():
    items = SqlHandler.get_table('../data/web_items.db')
    return items


def download_thumbnails(item_list = None):
    if item_list is None:
        
        if items.count is not 0:
            ebay.download_thumbnails(items)
        else:
            ebay.download_thumbnails(SqlHandler.getTable('../data/web_items.db'))
    else:
        ebay.download_thumbnails(item_list)
