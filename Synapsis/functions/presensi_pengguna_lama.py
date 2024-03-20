import csv
import os
from datetime import datetime

def write_csv_header():
    if not os.path.exists('/Users/fathindifarobbani/Documents/Difa/Synapsis/data_presensi.csv'):
        with open('/Users/fathindifarobbani/Documents/Difa/Synapsis/data_presensi.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Nama', 'Waktu'])
            print("Header CSV telah ditulis.")

def add_new_entry(name):
    if not os.path.exists('/Users/fathindifarobbani/Documents/Difa/Synapsis/data_presensi.csv'):
        write_csv_header()
    with open('/Users/fathindifarobbani/Documents/Difa/Synapsis/data_presensi.csv', mode='a', newline='') as file:
        fieldnames = ['Nama', 'Waktu']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow({'Nama': name, 'Waktu': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})

def execute_database(name):
    add_new_entry(name)

# Contoh penggunaan
if __name__ == "__main__":
    # Contoh penggunaan fungsi execute_database() dengan variabel name
    name = "Fathin Difa Robbani"  # Atur nama sesuai kebutuhan
    execute_database(name)