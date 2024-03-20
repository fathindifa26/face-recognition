from capture_photo_with_photobooth import test_camera_with_third_party_app
from register_new_user import register_new_user
from pengguna_baru import pengguna_baru
from presensi_pengguna_lama import execute_database
import directory
import os

if __name__ == "__main__":
    while True:
        directory = directory.directory
        os.system('cls' if os.name == 'nt' else 'clear')

        # Mendapatkan lokasi penyimpanan foto dari variabel lingkungan atau menggunakan nilai default jika tidak ada
        photo_storage_path = os.path.join(directory, 'foto', '0_foto_presensi')

        # Menghapus file yang ada di folder penyimpanan foto
        file_list = os.listdir(photo_storage_path)
        for file_name in file_list:
            file_path = os.path.join(photo_storage_path, file_name)
            os.remove(file_path)

        # Foto User
        test_camera_with_third_party_app(photo_storage_path)
        os.system('cls' if os.name == 'nt' else 'clear')

        input('Proses pengambilan foto selesai. Tekan ENTER untuk melanjutkan...')

        # Face Recognition bekerja
        print('loading....')
        from model import run_model
        hasil = run_model()

        if hasil:
            execute_database(hasil)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f'Halo {hasil}!')
            print('Anda sudah terpresensi')
            input('ENTER untuk keluar')
            break
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Anda belum terdaftar')
            pengguna_baru()
            os.system('cls' if os.name == 'nt' else 'clear')
            input('Anda sudah terdaftar! Bersiap diri untuk melakukan presensi. Tekan ENTER untuk melanjutkan...')