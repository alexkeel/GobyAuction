import json


class ConfigHandler:

    reminder_interval = 0
    keywords = []
    start_price = 0
    end_price = 0
    pages_to_scrape = 0
    path = ""
    
    def print_data(self):
        print("Reminder interval " + str(self.reminder_interval))
        print("Start Price " + str(self.start_price))
        print("End Price " + str(self.end_price))
        print("Keywords")
        for item in self.keywords:
            print(item)
            
    def load_config(self):
        with open(self.path) as data_file:
            data = json.load(data_file)
            
        self.reminder_interval = data["ReminderInterval"]
        self.start_price = data["StartPrice"]
        self.end_price = data["EndPrice"]
        self.keywords = data["Keywords"]
        self.pages_to_scrape = data["PagesToScrape"]

    def update_config(self):
        with open(self.path, "r") as config:
            data = json.load(config)

        # Make changes to json file buffer
        data["ReminderInterval"] = self.reminder_interval
        data["StartPrice"] = self.start_price
        data["EndPrice"] = self.end_price
        data["Keywords"] = self.keywords
        data["PagesToScrape"] = self.pages_to_scrape

        with open(self.path, "w") as config:
            json.dump(data, config)

    def set_pages_to_scrape(self, pages):
        self.pages_to_scrape = pages
            
    def set_config(self, config_path):
        self.path = config_path
            
    def add_keyword(self, keyword):
        if len(keyword) < 50 and len(keyword) > 0:
            self.keywords.append(keyword)
        else:
            return False
        
    def remove_keyword(self, index):
        try:
            self.keywords.remove(index)
        except IndexError:
            return False
        
    def set_start_price(self, value):
        self.start_price = value

    def set_end_price(self, value):
        self.end_price = value

    def set_reminder_interval(self, value):
        self.reminderInterval = value

    def get_keywords(self):
        return self.keywords

    def get_start_price(self):
        return self.start_price

    def get_end_price(self):
        return self.end_price

    def get_reminder_interval(self):
        return self.reminder_interval

    def get_pages_to_scrape(self):
        return self.pages_to_scrape
            
