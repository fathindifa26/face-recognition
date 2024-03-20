import csv
import os
import shutil
from capture_photo_with_photobooth import test_camera_with_third_party_app

# Fungsi untuk mengecek apakah nama sudah ada dalam file CSV
def is_name_registered(name):
    try:
        with open('data_presensi.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Nama'] == name:
                    return True
        return False
    except:
        pass

# Fungsi untuk membuat folder baru berdasarkan nama dan menentukan save path
def create_folder(name):
    base_path = os.environ.get('BASEPATH', '/Users/fathindifarobbani/Documents/Difa/Synapsis/foto')
    folder_path = os.path.join(base_path, name)
    os.makedirs(folder_path, exist_ok=True)
    return folder_path

# Fungsi untuk menjalankan fungsi test_camera_with_third_party_app lima kali
def run_camera_test(save_path):
    for i in range(1, 6):
        print(f"Jalankan tes kamera ke-{i}")
        # Panggil fungsi test_camera_with_third_party_app dengan gaya berbeda
        test_camera_with_third_party_app(save_path)

def pengguna_baru():
    while True:
        name = input("Masukkan nama Anda: ").title()  # Mengkapitalisasi huruf depan nama
        if name.replace(" ","").isalpha():  # Validasi agar hanya huruf alfabet yang diterima
            if not is_name_registered(name):
                break
            else:
                print("Nama sudah terdaftar. Silakan masukkan nama lain.")
        else:
            print("Nama hanya boleh berisi huruf alfabet.")

    folder_path = create_folder(name)
    run_camera_test(folder_path)

if __name__ == "__main__":
    pengguna_baru()