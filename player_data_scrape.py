# Scrapper for the actual player data

from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
import tkinter as tk
from tkinter import filedialog

class Scrape:
    # Data needs to be a list of tuples 
    def __init__(self):
        self._data = None

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