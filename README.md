# Image Encryption Tool

## Description

This project is a simple image encryption tool that uses pixel manipulation techniques to encrypt and decrypt images. By performing operations such as swapping pixel values or applying basic mathematical operations to each pixel, this tool allows users to securely encrypt their images and later decrypt them.

## Features

- Encrypts images using pixel manipulation techniques.
- Decrypts images to their original form.
- User-friendly interface for selecting images and entering encryption keys.
- Supports various image formats (e.g., PNG, JPEG).

## Technologies Used

- **Python**: Core programming language for the project.
- **Pillow (PIL)**: Library for image processing.
- **NumPy**: Library for numerical operations on arrays.
- **VSCode**: Integrated development environment (IDE) for coding.
- **Git & GitHub**: Version control and project collaboration.

## Setup and Installation

1. **Install Python**: Download and install Python from [python.org](https://www.python.org/).

2. **Clone the Repository**:

   ```bash

   git clone <repository-url>

Navigate to the Project Directory:

bash
cd image_encryption_tool
Create a Virtual Environment (optional but recommended):

bash
python -m venv env
Activate the Virtual Environment:

On Windows:

bash
.\env\Scripts\activate
On macOS/Linux:

bash
source env/bin/activate
Install Required Packages:

bash
pip install -r requirements.txt
How to Use
Run the Program:

bash
python image_encryption_tool.py
Encrypt an Image:

Select the image file you want to encrypt.

Enter an encryption key (an integer).

Provide the output path for the encrypted image.

Decrypt an Image:

Select the encrypted image file.

Enter the decryption key (the same key used for encryption).

Provide the output path for the decrypted image.

Example
Encryption Process
plaintext
Starting the program...
Select an option:

1. Encrypt an Image
2. Decrypt an Image
Enter your choice: 1
Encryption selected
Enter the path to the image file: example.png
Enter the encryption key (integer): 12345
Enter the output path for the encrypted image: encrypted_example.png
Encrypting image...
Image encrypted successfully!
Decryption Process
plaintext
Starting the program...
Select an option:
1.Encrypt an Image
2.Decrypt an Image
Enter your choice: 2
Decryption selected
Enter the path to the encrypted image file: encrypted_example.png
Enter the decryption key (integer): 12345
Enter the output path for the decrypted image: decrypted_example.png
Decrypting image...
Image decrypted successfully!
Learning Outcomes
Image Processing: Understanding how to manipulate image pixels using Python.

Encryption Techniques: Learning basic techniques for encrypting and decrypting data.

Python Programming: Enhancing skills in Python, including libraries like Pillow and NumPy.

Version Control: Using Git and GitHub for version control and collaboration.

Documentation: Recognizing the importance of clear and detailed project documentation.

Contribution
Feel free to fork this repository, submit issues, and send pull requests. Contributions are welcome!

License
This project is licensed under the MIT License - see the LICENSE file for details.

Connect with Me
I'm eager to apply my skills in a professional setting and contribute to innovative cybersecurity solutions. If you have any opportunities or would like to collaborate, feel free to reach out. I am rooting for you too!
