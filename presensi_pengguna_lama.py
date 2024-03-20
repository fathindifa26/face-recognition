import csv
import os
from datetime import datetime
import directory

dir_path = directory.directory

def write_csv_header(file):
    if not os.path.exists(file):
        with open(file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Nama', 'Waktu'])
            print("Header CSV telah ditulis.")

def add_new_entry(name, file):
    if not os.path.exists(file):
        write_csv_header(file)
    with open(file, mode='a', newline='') as file:
        fieldnames = ['Nama', 'Waktu']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow({'Nama': name, 'Waktu': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})

def execute_database(name):
    file = os.path.join(dir_path, 'data_presensi.csv')
    add_new_entry(name, file)

# Contoh penggunaan
if __name__ == "__main__":
    # Contoh penggunaan fungsi execute_database() dengan variabel name
    name = "Fathin Difa Robbani"  # Atur nama sesuai kebutuhan
    execute_database(name)