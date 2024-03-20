# Face Recognition Attendance System

## Overview
Face Recognition Attendance System is a Python-based application that utilizes facial recognition technology, specifically the **VGG Face algorithm**, to automate attendance tracking. This system provides a convenient and efficient way to record attendance without the need for manual processes.

## Features
- **Face Detection**: Automatically detects faces in images or live video streams.
- **Face Recognition**: Identifies individuals by matching detected faces with pre-registered faces in the database.
- **Automated Attendance**: Records attendance based on recognized faces.
- **User Registration**: Allows administrators to register new users and associate their faces with their identities.
- **Flexible Configuration**: Easily customizable to adapt to various environments and user requirements.

## Installation
1. Clone this repository to your local machine.
    ```bash
    git clone https://github.com/fathindifa26/face-recognition-attendance.git
    ```
2. Install the required dependencies.
    ```bash
    pip install -r requirements.txt
    ```
3. Configure the application settings such as database connection and face recognition model paths.

## Usage
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
   - Navigate to the `config` directory and open the `config.py` file.
   - Modify the file paths for database connection and face recognition model paths according to your setup.
   - Save the changes and close the file.
5. Run the `main.py` script to start the application.
    ```bash
    python main.py
    ```
6. Follow the on-screen instructions to perform tasks such as taking attendance, registering new users, etc.

## Requirements
- Python 3.11
- OpenCV
- TensorFlow
- Other dependencies listed in `requirements.txt`

## Contributors
- John Doe (@johndoe)
- Jane Smith (@janesmith)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
