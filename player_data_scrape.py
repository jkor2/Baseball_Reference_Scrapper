# Scrapper for the actual player data

from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
import tkinter as tk
from tkinter import filedialog
import json


class Scrape:
    # Data needs to be a list of tuples 
    def __init__(self):
        self._data = None
        self._player_data = None
        self._JSON_object = {}

    def convert_data(self):
        if self._data is None:
            """
            Convert data for proper usage
            """
            cnvrt = Convert_Excel()
            cnvrt.open_file()
            self._data = cnvrt.return_data()
            print(self._data)
        else:
            """
            Reset and rerun if already populated w data
            """
            self.reset_data()
            self.convert_data()
    
    def reset_data(self):
        """
        Resest data to None
        """
        self._data = None

    def scrape_html(self):
        """
        Where http request will be done 
        1) Reformat excel id and Names
        2) begin loop -- capture each webpage
        3) pass response to format_to_JSON 
        4) pass format_to_JSON result to add_to_temp_JSON
        5) next iteration
        """
        pass

    def format_to_JSON(self):
        """
        Where data will be reformatted to JSON data
        """
        pass

    def add_to_temp_JSON(self):
        """
        Where format_to_JSON result will be sent to be 
        added to JSON object
        """
        pass

    def write_JSON_doc(self):
        """
        Dump reformmated JSON data into a JSON files
        """
        pass



class Convert_Excel:
    """
    Converts the excel data into list of tuples 
    """
    def __init__(self):
        self.data = None
    
    def open_file(self):
        """
        Open excel file generated form player_id_and_name 
        & reformat it 
        """
        root = tk.Tk()
        root.withdraw()  
        # Ask the user to select an Excel file from their desktop
        file_path = filedialog.askopenfilename(initialdir="/Desktop", title="Select An Excel File", filetypes=(("Excel files", "*.xlsx;*.xls"), ("All files", "*.*")))
        df = pd.read_excel(file_path)
        temp_list = []
        try:
            tracker = 0
            while tracker <= len(df) - 1:
                # Reformat of excel structure
                temp_list.append((df["player_ids"][tracker], df['player_name'][tracker]))
                tracker += 1
            self.data = temp_list
        except:
            exit()
    
    def return_data(self):
        """
        Return the data 
        """
        return self.data



scrape = Scrape()
scrape.convert_data()