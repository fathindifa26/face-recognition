# Face Recognition Attendance System (Only Compatible with Macbook)

## Overview
Face Recognition Attendance System is a Python-based application that utilizes facial recognition technology, specifically the **VGG Face algorithm**, to automate attendance tracking. This system provides a convenient and efficient way to record attendance without the need for manual processes. Please note that this application is exclusively compatible with Macbook due to its reliance on the Photo Booth application for capturing photos.

## Features
- **Face Detection**: Automatically detects faces in images or live video streams.
- **Face Recognition**: Identifies individuals by matching detected faces with pre-registered faces in the database.
- **Automated Attendance**: Records attendance based on recognized faces.
- **User Registration**: Allows administrators to register new users and associate their faces with their identities.
- **Flexible Configuration**: Easily customizable to adapt to various environments and user requirements.

## Installation
1. Download the repository from GitHub to your local machine.
   - Visit the [GitHub repository](https://github.com/fathindifa26/face-recognition-attendance).
   - Click on the green "Code" button and select "Download ZIP".
   - Extract the downloaded ZIP file to a location on your computer.
2. Navigate to the extracted directory in your terminal or command prompt.
3. Ensure you have installed all the required dependencies listed in `requirements.txt`.
    ```bash
    pip install -r requirements.txt
    ```
4. **Update File Paths**:
   - Navigate to the `config` directory and open the `directory.py` file.
   - Modify the file paths for database connection and face recognition model paths according to your setup.
   - Update the `directory` variable to specify the directory where your project resides. You can use an environment variable or a specific path. For example:
     ```python
     import os
     directory = os.environ.get('DIRECTORY', '/Users/your_project')
     photo_booth = "/Users/your_username/Pictures/Photo Booth Library/Pictures"
     ```
   - Save the changes and close the file.
5. Download the VGG Face weights file from [Kaggle](https://www.kaggle.com/datasets/evertwydoodt/vgg-face-weights).
6. Place the downloaded `vgg_face_weights.h5` file in the same directory as the project files.
7. **Note**: As this application is designed specifically for Macbook, ensure you have the Photo Booth application installed and accessible.
8. Run the `main.py` script to start the application.
    ```bash
    python main.py
    ```
9. Follow the on-screen instructions to perform tasks such as taking attendance, registering new users, etc.

## Requirements
- Macbook
- Python 3.11
- OpenCV
- TensorFlow
- Other dependencies listed in `requirements.txt`

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
