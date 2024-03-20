import csv
import os
from datetime import datetime


def write_csv_header(file_path):
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Nama', 'Waktu'])

def add_entry_to_csv(file_path, name):
    with open(file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, datetime.now().strftime('%Y-%m-%d %H:%M:%S')])

def check_existing_name(name):
    with open('data_presensi.csv', mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Nama'] == name:
                return True
        return False

def add_new_entry(name):
    with open('data_presensi.csv', mode='a', newline='') as file:
        fieldnames = ['Nama', 'Waktu']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow({'Nama': name, 'Waktu': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})

def register_new_user():
    name = input("Masukkan nama lengkap Anda: ")
    if check_existing_name(name):
        print(f"Halo {name}!")
        new_user = False
    else:
        new_user = True
        register = input("Anda adalah orang baru. Apakah ingin mendaftar? (ya/tidak): ")
        if register.lower() == 'ya':
            add_new_entry(name)
            print(f"Selamat datang, {name}!")
        else:
            print("Terima kasih. Sampai jumpa!")

if __name__ == "__main__":
    file_path = 'data_presensi.csv'

    if not os.path.exists(file_path):
        write_csv_header(file_path)

    register_new_user()