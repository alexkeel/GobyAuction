import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt
import ConfigHandler
from WebScraper import Ebay
import Functional


class GUI(QtWidgets.QMainWindow):

    item_list = []
    
    def __init__(self):
        super().__init__()
        
    def start(self):
        Functional.scrape()
        self.items = Functional.get_items()
        Functional.download_thumbnails(self.items)
        self.create_gui()

    def create_gui(self):

        self.create_menu_bar()
        
        # Set item info area properties
        self.item_info_area = QtWidgets.QVBoxLayout()
        text_box = QtWidgets.QTextEdit("THIS WILL BE THE AREA WHERE INFORMATION ABOUT THE SELECTED ITEM WILL BE DISPLAYED")
        self.item_info_area.addWidget(text_box)
        # Put items into "Lot" objects
        for item in self.items:
            self.item_list.append(Lot('../data/images/' + str(item[0]) + ".jpg",
                                      str(item[1]),
                                      str(item[2]),
                                      str(item[5]),
                                      str(item[6])))
        # Set main area properties
        self.main_area = QtWidgets.QGridLayout()
        self.main_area.setColumnMinimumWidth(0, self.frameGeometry().width() / 2)
        self.main_area.setColumnMinimumWidth(1, self.frameGeometry().width() / 2)
 
        self.main_area.addWidget(self.create_item_area(self.item_list), 0, 0)
        self.main_area.addLayout(self.item_info_area, 0, 1)
        
        # Set main window properties
        self.setWindowTitle("GobyAuction")
        self.setGeometry(100, 100, 800, 500)
        self.central_widget = QtWidgets.QWidget()
        # Create a central widget to be used as the main window
        self.setCentralWidget(self.central_widget)
        self.central_widget.setLayout(self.main_area)
        
        self.show()

    def create_item_area(self, item_list):
        # Set main item area properties
        self.item_area = QtWidgets.QVBoxLayout()
        # Set scrollbar properties
        self.scroll_area = QtWidgets.QScrollArea()
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setWidgetResizable(True)
        # Set central widget
        self.scrollbar_central = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout()
        self.scrollbar_central.setLayout(layout)
        # Add buttons to button container
        button_container = QtWidgets.QButtonGroup(self.scrollbar_central)
        button_container.setExclusive(True)
        # Add item list to container
        for item in reversed(item_list):
            button_container.addButton(item)
            self.scrollbar_central.layout().addWidget(item)

        self.scroll_area.setWidget(self.scrollbar_central) 
        
        return self.scroll_area

    def create_menu_bar(self):
        bar = self.menuBar()
        file = bar.addMenu("File")

        # Create actions
        preferences_action = QtWidgets.QAction('Preferences...', self)
        exit_action = QtWidgets.QAction('Exit', self)

        # Add actions
        file.addAction(preferences_action)
        file.addAction(exit_action)

        # Events
        exit_action.triggered.connect(lambda: QtWidgets.qApp.quit())
        
    def create_item_list(self):
        pass

    def scrape(self):
        config = ConfigHandler.ConfigHandler()
        ebayScraper = Ebay()
        config.setConfig('../data/config.json')
        config.loadConfig() 
        ebayScraper.addKeywords(config.getKeywords())
        ebayScraper.setPagesToScrape(1)
        ebayScraper.scrapeSite()

    def create_preferences(self):
        pass

    
class Lot(QtWidgets.QPushButton):

    def __init__(self, image_path, title, price, purchase_type, website):
        super(Lot, self).__init__()
        #self.setStyleSheet("background-color: rgb(255,255,255); margin:5px; border:1px solid rgb(0, 0, 0); ")
        #self.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.setMinimumWidth(430)
        self.setMinimumHeight(150)
        self.setCheckable(True)
        #self.setStyleSheet('background-color: white;')

        self.website = "From " + website
        self.purchase_type = "Purchase Type: " + purchase_type
        self.image_path = image_path
        self.title = title
        self.price = price

        self.create_gui()

    def create_gui(self):
        # Create image
        image = QtGui.QImage(self.image_path)
        image_resized = image.scaled(140, 140)
        image_label = QtWidgets.QLabel()
        image_label.setPixmap(QtGui.QPixmap.fromImage(image_resized))

        # Create elements
        title_label = QtWidgets.QLabel(self.title)
        price_label = QtWidgets.QLabel(self.price)
        purchase_type_label = QtWidgets.QLabel(self.purchase_type)
        website_label = QtWidgets.QLabel(self.website)
        
        element_box1 = QtWidgets.QVBoxLayout()
        element_box1.addWidget(title_label)
        element_box1.addWidget(price_label)
        element_box1.addWidget(purchase_type_label)
        element_box1.addWidget(website_label)
        
        # Create layout
        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(image_label)
        layout.addLayout(element_box1)
        layout.stretch(600)

        self.setLayout(layout)

        self.show()

