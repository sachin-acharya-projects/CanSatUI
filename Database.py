import time, csv
from colorama import Fore, init; init(autoreset=True)

class Database:
    def __init__(self):
        "Init Database with State as False - Not storing"
        self.state = False
    def guardar(self, data: list):
        "Writing data to CSV file"
        if self.state == True:
            data.append(time.asctime())
            with open("log.csv", "a") as file:
                writer = csv.writer(file, delimiter=",")
                writer.writerow(data)
                
    def start(self):
        "Start Storage of Data in CSV"
        self.state = True
        print(f"{Fore.CYAN}Starting Storage in log.csv file")
    
    def stop(self):
        "Stop Storage of Data in CSV"
        self.state = False
        print(f"{Fore.CYAN}Stopping Storage in log")
