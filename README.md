# 👨‍💻 Finger Counter with Arduino and OpenCV

This project uses the OpenCV and MediaPipe libraries to detect and count fingers in real-time through a camera. It sends the count data to an Arduino via serial communication. On the Arduino side, LEDs are controlled based on the finger count, illuminating according to the received value.

## ⭐ Features

- **Finger Detection:** Uses the MediaPipe library to detect and count fingers in real-time.
- **Serial Communication:** Sends finger count data from the computer to Arduino via serial port.
- **LED Control:** Arduino interprets the received data and controls LEDs corresponding to the detected finger count.

## ⭐ Components

- **OpenCV:** Used for video capture and image processing.
- **MediaPipe:** Library for detecting hand landmarks.
- **PySerial:** Sends commands via serial communication.
- **Arduino Uno:** Controls LEDs based on commands received via serial.

## ⭐ Prerequisites

- Python 3.x
- Python libraries: OpenCV, MediaPipe, and pySerial
- Arduino IDE
- Visual Studio Code

## ⭐ Materials

- 1x 400-point Breadboard
- 1x Arduino Uno
- 11x Jumper Wires
- 5x LEDs
- Arduino-to-Serial cable

## ⭐ How to Use?

- Clone the repository into your virtual environment for Python with the mentioned libraries.
- Ensure a camera is available for use.
- Assemble the circuit as per the reference image provided in the *circuit* folder.
- Upload the Arduino sketch provided to the Arduino board.
- Run the Python script and use your *left* hand for interacting with the tool.

## ⭐ Final Thoughts

- The project was developed in one week and contributed to various areas of learning, such as embedded systems, circuit assembly, use of new libraries, integration of Python and C++ applications, among others.
  
- Contributions are welcome! For suggestions and modifications, please open an issue or submit a pull request.
