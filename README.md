# BioNet SDN Gateway & Face Recognition Security System

## Project Overview

BioNet is a Python-based security gateway prototype that combines facial recognition with network communication for secure user authentication.

The system uses OpenCV's LBPH (Local Binary Pattern Histogram) face recognition algorithm to verify a user's identity. After successful verification, the application sends an authentication message to the controller through a TCP socket connection.

## Features

- Face recognition-based authentication
- LBPH face recognition algorithm
- Camera-based face scanning
- Image upload for face verification
- Streamlit web interface
- TCP socket communication
- Authentication-based gateway access
- Face recognition model training
- Custom face dataset support

## Technologies Used

- Python
- Streamlit
- OpenCV
- OpenCV Contrib
- NumPy
- LBPH Face Recognition
- TCP Socket Programming

## Project Files

- `app.py` - Main Streamlit application for face recognition and authentication.
- `train.py` - Trains the LBPH face recognition model using images from the dataset.
- `controller.py` - Runs the authentication controller and listens for authentication messages.
- `model.yml` - Trained LBPH face recognition model.
- `requirements.txt` - Contains the required Python libraries.
- `dataset/` - Contains the face images used to train the recognition model.

## How the System Works

1. The user starts the controller.
2. The user checks the computer's IP address using `ipconfig`.
3. The Streamlit application is started.
4. The user selects Camera or Upload mode.
5. The system detects and recognizes the user's face.
6. If the identity is successfully verified, the user can click the "OPEN GATE" button.
7. The application sends `AUTH_SUCCESS` to the controller through a TCP socket.
8. The controller receives the authentication message and indicates that the gateway is opened.

## Installation

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the Project Folder

```bash
cd SDN-Gateway-Face-Recognition-Security-System
```

### 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

## How to Run the Project

### Step 1: Find the IP Address

Open Command Prompt and run:

```bash
ipconfig
```

Find the IPv4 address of the computer running the controller.

The IP address is used in `app.py` for the controller connection.

The current configuration is:

```python
client.connect(('192.168.1.6', 9999))
```

Change `192.168.1.6` to the IPv4 address of the computer running `controller.py`.

### Step 2: Start the Controller

Open Command Prompt or Terminal in the project folder and run:

```bash
python controller.py
```

The controller will start listening for authentication requests on port `9999`.

### Step 3: Start the Streamlit Application

Open another Command Prompt or Terminal window in the project folder and run:

```bash
python -m streamlit run app.py --server.address 0.0.0.0
```

The Streamlit application will start and provide a local web address.

Open the provided address in a web browser.

## Training the Face Recognition Model

If a new face dataset is used, place the images inside the `dataset` folder.

Then run:

```bash
python train.py
```

This will create or update:

```text
model.yml
```

The generated `model.yml` file is used by `app.py` for face recognition.

## Important Note

The controller and Streamlit application should be running at the same time.

The controller must be started first:

```bash
python controller.py
```

Then start the Streamlit application:

```bash
python -m streamlit run app.py --server.address 0.0.0.0
```

Make sure the IP address configured in `app.py` matches the IPv4 address of the computer running the controller.

## Security Considerations

This project is an educational prototype demonstrating facial recognition and network authentication concepts.

For a production system, additional security features such as encrypted communication, secure authentication, access control, and protected credentials should be implemented.

## Future Improvements

- Integration with a real SDN controller
- Secure encrypted network communication
- Multi-user face recognition
- User registration system
- Authentication logging
- Role-based access control
- Real-time network monitoring
- Improved face recognition accuracy

## Author

**Rizwa Hassan**

Computer Science Student
