# SDN Gateway & Face Recognition Security System

## Project Overview

This project combines Software-Defined Networking (SDN) with an autonomous facial recognition security layer to provide secure and intelligent access control.

The system is designed to monitor and control network access while using facial recognition technology to authenticate authorized users. The facial recognition component uses the Local Binary Pattern Histogram (LBPH) algorithm to identify registered users.

## Key Features

- Software-Defined Networking (SDN) based network control
- Facial recognition-based authentication
- LBPH face recognition algorithm
- Secure access control
- Client-server communication
- Automated authentication workflow
- Network security monitoring
- Python-based implementation

## Technologies Used

- Python
- Software-Defined Networking (SDN)
- OpenCV
- LBPH Face Recognition
- Socket Programming
- Computer Vision

## System Architecture

The system consists of multiple components working together:

1. **Face Recognition Module**
   - Captures and processes facial data.
   - Uses the LBPH algorithm to recognize registered users.

2. **Authentication Layer**
   - Verifies the identity of the user.
   - Determines whether access should be granted or denied.

3. **SDN Gateway**
   - Acts as a controlled entry point for network communication.
   - Manages access based on authentication results.

4. **Controller**
   - Handles communication between the client and gateway.
   - Processes authentication status and network access requests.

## Project Workflow

1. User attempts to access the protected system.
2. The facial recognition module captures the user's face.
3. The LBPH algorithm compares the captured face with registered facial data.
4. The system determines whether the user is authorized.
5. Authentication status is communicated to the network gateway.
6. Authorized users are granted access.

## Project Structure
SDN-Gateway-Face-Recognition-Security-System/
│
├── Python source files
├── Face recognition module
├── SDN gateway components
├── Controller co
