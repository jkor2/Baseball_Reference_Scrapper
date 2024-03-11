# Scrapper for the actual player data

from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
import tkinter as tk
from tkinter import filedialog

class Scrape:
    # Data needs to be a list of tuples 
    def __init__(self, data):
        self._data = data



class Convert_Excel:
    def __init__(self):
        self.data = None
    
    def open_file(self):
        root = tk.Tk()
        root.withdraw()  
        # Ask the user to select an Excel file from their desktop
        file_path = filedialog.askopenfilename(initialdir="/Desktop", title="Select An Excel File", filetypes=(("Excel files", "*.xlsx;*.xls"), ("All files", "*.*")))
        df = pd.read_excel(file_path)
        temp_list = []

        tracker = 0
        while tracker <= len(df) - 1:
            # Reformat of excel structure
            temp_list.append((df["player_ids"][tracker], df['player_name'][tracker]))
            tracker += 1
        self.data = temp_list



xls = Convert_Excel()
xls.open_file()