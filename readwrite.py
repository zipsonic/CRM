import os
import csv
from clients import Client

def save_list(clientlist: list[Client]) -> None:

    with open('clientlist.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
    
        writer.writerow(["uuid","lastname","firstname","email","phone"])
    
        for client in clientlist:
            writer.writerow([str(client.client_id),client.last_name,client.first_name,client.email,client.phone])

def read_list() -> list[Client]:

    #Initialize List
    clientlist: list[Client] = []

    listfile: str = "clientlist.csv"

    if os.path.isfile(listfile):
        with open(listfile,'r', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=",")

            #Skip Header
            next(reader, None)

            #Read Rows into clientlist
            for row in reader:
                clientlist.append(Client(first_name=row[2],last_name=row[1],email=row[3],phone=row[4],client_id=row[0]))
    
    return clientlist