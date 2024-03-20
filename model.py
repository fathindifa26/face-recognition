import os
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
# used to supress display of warnings
import warnings
from sklearn.metrics import precision_recall_curve, accuracy_score, f1_score, precision_score, recall_score
import directory

directory = directory.directory



# suppress display of warnings
def run_model():
    directory = directory.directory
    source_dir = os.path.join(directory, 'foto')
    warnings.filterwarnings('ignore')
    class IdentityMetadata():
        def __init__(self, base, name, file):
            self.base = base
            # identity name
            self.name = name
            # image file name
            self.file = file

        def __repr__(self):
            return self.image_path()

        def image_path(self):
            return os.path.join(self.base, self.name, self.file) 

    def load_metadata(path):
        metadata = []
        presensi_identity = None
        for i in os.listdir(path):
            # Pengecualian untuk file tersembunyi
            if not i.startswith('.'):
                for f in os.listdir(os.path.join(path, i)):
                    # Check file extension. Allow only jpg/jpeg' files.
                    ext = os.path.splitext(f)[1]
                    if ext == '.jpg' or ext == '.jpeg':
                        identity = IdentityMetadata(path, i, f)
                        if i == '0_foto_presensi':
                            presensi_identity = identity
                        else:
                            metadata.append(identity)
        # Pastikan identity untuk "0_foto_presensi" berada di indeks pertama
        if presensi_identity is not None:
            metadata.insert(0, presensi_identity)
        return np.array(metadata)

    # Load metadata dengan path yang sudah diperbarui
    metadata = load_metadata(source_dir)

    import cv2
    def load_image(path):
        img = cv2.imread(path, 1)
        # OpenCV loads images with color channels
        # in BGR order. So we need to reverse them
        return img[...,::-1]

    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import ZeroPadding2D, Convolution2D, MaxPooling2D, Dropout, Flatten, Activation

    def vgg_face():	
        model = Sequential()
        model.add(ZeroPadding2D((1,1),input_shape=(224,224, 3)))
        model.add(Convolution2D(64, (3, 3), activation='relu'))
        model.add(ZeroPadding2D((1,1)))
        model.add(Convolution2D(64, (3, 3), activation='relu'))
        model.add(MaxPooling2D((2,2), strides=(2,2)))
        
        model.add(ZeroPadding2D((1,1)))
        model.add(Convolution2D(128, (3, 3), activation='relu'))
        model.add(ZeroPadding2D((1,1)))
        model.add(Convolution2D(128, (3, 3), activation='relu'))
        model.add(MaxPooling2D((2,2), strides=(2,2)))
        
        model.add(ZeroPadding2D((1,1)))
        model.add(Convolution2D(256, (3, 3), activation='relu'))
        model.add(ZeroPadding2D((1,1)))
        model.add(Convolution2D(256, (3, 3), activation='relu'))
        model.add(ZeroPadding2D((1,1)))
        model.add(Convolution2D(256, (3, 3), activation='relu'))
        model.add(MaxPooling2D((2,2), strides=(2,2)))
        
        model.add(ZeroPadding2D((1,1)))
        model.add(Convolution2D(512, (3, 3), activation='relu'))
        model.add(ZeroPadding2D((1,1)))
        model.add(Convolution2D(512, (3, 3), activation='relu'))
        model.add(ZeroPadding2D((1,1)))
        model.add(Convolution2D(512, (3, 3), activation='relu'))
        model.add(MaxPooling2D((2,2), strides=(2,2)))
        
        model.add(ZeroPadding2D((1,1)))
        model.add(Convolution2D(512, (3, 3), activation='relu'))
        model.add(ZeroPadding2D((1,1)))
        model.add(Convolution2D(512, (3, 3), activation='relu'))
        model.add(ZeroPadding2D((1,1)))
        model.add(Convolution2D(512, (3, 3), activation='relu'))
        model.add(MaxPooling2D((2,2), strides=(2,2)))
        
        model.add(Convolution2D(4096, (7, 7), activation='relu'))
        model.add(Dropout(0.5))
        model.add(Convolution2D(4096, (1, 1), activation='relu'))
        model.add(Dropout(0.5))
        model.add(Convolution2D(2622, (1, 1)))
        model.add(Flatten())
        model.add(Activation('softmax'))
        return model


    model = vgg_face()

    model.load_weights('vgg_face_weights.h5')

    from tensorflow.keras.models import Model
    vgg_face_descriptor = Model(inputs=model.layers[0].input, outputs=model.layers[-2].output)

    embeddings = np.zeros((metadata.shape[0], 2622))
    for i, m in enumerate(metadata):
        img_path = metadata[i].image_path()
        img = load_image(img_path)
        img = (img / 255.).astype(np.float32)
        img = cv2.resize(img, dsize = (224,224))
        embedding_vector = vgg_face_descriptor.predict(np.expand_dims(img, axis=0))[0]
        embeddings[i]=embedding_vector

    def distance(emb1, emb2):
        return np.sum(np.square(emb1 - emb2))

    from collections import defaultdict
    # 1. Hitung semua jarak dari gambar dengan indeks 0 ke semua gambar lainnya
    distances_to_0 = [distance(embeddings[0], embeddings[i]) for i in range(1, len(metadata))]

    # 2. Kelompokkan jarak berdasarkan label dari metadata
    label_distances = defaultdict(list)
    for i, metadata_entry in enumerate(metadata[1:], start=1):  # Mulai dari indeks 1 karena indeks 0 adalah gambar 0
        label = metadata_entry.name
        label_distances[label].append(distances_to_0[i - 1])  # Gunakan i - 1 karena indeks distances_to_0 dimulai dari 0

    # 3. Hitung rata-rata jarak untuk setiap kelompok label
    average_distances = {label: np.mean(distances) for label, distances in label_distances.items()}

    # 4. Tentukan kelompok label dengan rata-rata jarak terkecil
    closest_label = min(average_distances, key=average_distances.get)
    closest_distance = average_distances[closest_label]

    if closest_distance < 0.45:
        return closest_label
    else:
        return False