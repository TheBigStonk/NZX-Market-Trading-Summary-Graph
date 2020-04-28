### Basic Python Script for taking NZX Data Scraped off of the NZX and saving into a CSV Spreadsheet.
### Best to run at 4:57 before market close or directly after
 
from bs4 import BeautifulSoup
import requests
import json
import csv
import os.path
 
## To change name of file outputed or header row column names, change the following variable names 
csv_filename = "nzx_trading_data.csv"
csv_header_row_creation = [["Market", "Daily Trade Volume", "Daily Trade Value"]]
 
csv_buffer = []
 
# The purpose of this Python function is to create a JSON object of top five gainers & decliners, daily traded volumes, and announcements
def webscrape(link):
    page_response = requests.get(link)
    content = page_response.content
    soupsoupsoup = BeautifulSoup(content, "html.parser")
    reduced_soup = soupsoupsoup.find(class_="js-div").findAll("script", type="text/javascript")
    # NZX is tricky with grabbing their data so a trim is the only reasonable workaround
    nearlyjson = str(reduced_soup[1])[139:-403]
    return json.loads(nearlyjson)
 
# The purpose of this Python function is to open/create the csv file for daily trade volumes and values for writing. Heavy lifter
def csv_connect(filename, collected_data):
    # Check if file for achival purpose exists and if not create it
    if os.path.exists(filename) != True :
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(csv_header_row_creation[0])
    # Read in historical data and send to buffer
    with open(filename, newline="") as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=",")
        for row in csv_reader:
            csv_buffer.append(row)
    # Read in data collected in pull to buffer
    for code in collected_data:
        csv_buffer.append([code["code"], code["trade_value"], code["trade_volume"]])
    # Write all the yummy buffer data that was once soup into archival folder
    with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            for row in csv_buffer:
                writer.writerow(row)
 
nzx_json = webscrape("https://www.nzx.com")
csv_connect(csv_filename, nzx_json)
 
### To move CSV Elements to seperate functions###

 
print("As of the time this code has been run, the stats are...")
print("------------------------------------------------")
for code in nzx_json:
    print("Market: "+str(code["code"]))
    print("Daily Trade Value: "+str(code["trade_value"]))
    print("Daily Trade Volume: "+str(code["trade_volume"]))
    print("------------------------------------------------")
 
print("-----------------------------------------------------")
print("-- CVS Sheet ["+csv_filename+"] has been updated ---")
print("-----------------------------------------------------")
# Something to keep the program hanging while not being used in automation mode
input("Press any key to continue...")