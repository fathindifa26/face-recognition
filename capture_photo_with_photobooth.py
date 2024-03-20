import cv2
import subprocess
import shutil
import os
from datetime import datetime
import time
import directory



def move_latest_photo(source_folder, destination_folder):
    try:
        # Mendapatkan daftar semua file di folder sumber (urutkan berdasarkan waktu modifikasi)
        files = sorted(os.listdir(source_folder), key=lambda x: os.path.getmtime(os.path.join(source_folder, x)), reverse=True)

        # Temukan file foto terbaru
        latest_photo = None
        for file in files:
            if file.endswith('.jpg') or file.endswith('.jpeg'):
                latest_photo = file
                break

        # Jika ada file foto, deteksi wajah dan potong gambar
        if latest_photo:
            source_file_path = os.path.join(source_folder, latest_photo)
            
            # Baca gambar
            image = cv2.imread(source_file_path)
            
            # Konversi gambar ke grayscale
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            # Load pre-trained Haar Cascade face detector
            face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

            # Deteksi wajah pada gambar
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            # Jika wajah terdeteksi, potong dan simpan gambar
            if len(faces) > 0:
                (x, y, w, h) = faces[0]  # Ambil koordinat wajah pertama
                face_crop = image[y:y+h, x:x+w]  # Potong wajah dari gambar
                
                # Ubah nama file sesuai dengan waktu saat ini
                timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
                new_file_name = f"face_{timestamp}.jpg"

                # Simpan wajah yang dipotong dengan nama baru ke folder tujuan
                cv2.imwrite(os.path.join(destination_folder, new_file_name), face_crop)
                print("Foto terbaru berhasil dipindahkan dan dipotong.")
            else:
                print("Tidak ada wajah yang terdeteksi dalam foto terbaru.")

        else:
            print("Tidak ada file foto yang ditemukan.")

    except Exception as e:
        print("Terjadi kesalahan:", e)

def test_camera_with_third_party_app(save_path):
    try:
        input('Siapkan diri anda untuk foto! (tekan enter)')
        # Jalankan aplikasi pihak ketiga untuk mengakses webcam
        subprocess.run(["open", "-a", "Photo Booth"])
        
        # Setelah selesai menguji, tunggu 3 detik dan kemudian pindahkan dan potong file foto terbaru ke lokasi yang ditentukan
        time.sleep(5)

        source_folder = directory.photo_booth
        move_latest_photo(source_folder, save_path)
        input("Tunggu sebentar.. tekan ENTER")

        input("Setelah selesai foto, tekan ENTER")

    except Exception as e:
        print("Terjadi kesalahan:", e)
