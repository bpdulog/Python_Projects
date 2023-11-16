import sys
import subprocess
import os

required_modules = ['csv', 'datetime', 'time']

for m in required_modules:
    if m not in sys.modules:
        print(f"{m} not installed. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", m])

import csv
from datetime import datetime  
import time

# Specify output folder
output_folder = os.path.join('C:\\', 'Users', 'bryan', 'Documents', 'data', 'logs') 

# Specify CSV file path
csv_file_path = os.path.join(output_folder, 'data_log.csv')

# Check if the CSV file exists
if not os.path.exists(csv_file_path):
    # If not, create the file and write headers
    with open(csv_file_path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Timestamp', 'Latitude', 'Longitude', 'Altitude'])

while True:
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

    # Read data from text files
    text_folder = 'C:\\Users\\bryan\\Documents\\SimToolkitPro\\streaming' 
    lat = open(os.path.join(text_folder, 'lat.txt')).read()
    lon = open(os.path.join(text_folder, 'lon.txt')).read() 
    alt = open(os.path.join(text_folder, 'altitude.txt')).read()

    # Open the CSV file in append mode
    with open(csv_file_path, 'a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([timestamp, lat, lon, alt])  

    time.sleep(60)
