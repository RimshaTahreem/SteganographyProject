# SteganographyProject
# Steganography

This project focuses on **image-based encryption and decryption**, using **steganography** to hide secret messages inside an image. The project provides a simple but effective way to securely communicate by embedding a message into the pixel values of an image, which can be decrypted later using a passcode.

## Features
- **Encrypts** a secret message by hiding it within an image.
- **Decrypts** the hidden message with a passcode.
- Uses **steganography** to embed and extract messages without visibly altering the image.
- Simple **GUI** for easy interaction.

## Technologies Used
- **Python** (Programming Language)
- **OpenCV** (Image Processing)
- **Tkinter** (GUI Framework)

## Requirements
- Python 3.x
- OpenCV (`pip install opencv-python`)
- Tkinter (Pre-installed with Python)
  
## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/RimshaTahreem/SteganographyProject.git
   ```
3. Install the required libraries:
   ```bash
   pip install opencv-python
   ```
   
4. Run the encryption script or GUI:
   - To run the encryption file:
     ```bash
     python encrypt.py
     ```
   - To run the decryption file:
     ```bash
     python decrypt.py
     ```

5. Follow the prompts in the terminal or GUI to encrypt or decrypt messages.

## Usage
1. **Encryption**:
   - Enter a secret message you want to hide.
   - Choose an image file where the message will be embedded.
   - Provide a passcode for secure decryption.
   - The image will be saved with the hidden message and can be shared.

2. **Decryption**:
   - Select the image with the hidden message.
   - Enter the passcode to retrieve the secret message.

## End Users
- Individuals looking for a simple way to send encrypted messages.
- Educational purposes for learning steganography and encryption techniques.
- Small businesses or personal users who need secure communication.
