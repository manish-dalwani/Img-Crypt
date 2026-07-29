
## 📌 **Overview**
This is a Python-based Steganography Tool designed for Kali Linux. It allows users to hide and retrieve messages from images securely. The tool also supports password-based encryption for added security.

## ✨ **Features**
- Encode messages into image files.
- Decode hidden messages from steganographic images.
- Encrypt messages before encoding with a user-defined password using AES encryption.
- Supports BMP and PNG formats.
- Uses Colorama for enhanced terminal output with better formatting for clarity.


## 📂 **Installation**
Follow the steps below to set up Img-Crypt on your system.

**Step 1:** Clone the Repository:

```bash
  sudo su
  git clone https://github.com/manish-dalwani/Img-Crypt.git
  cd Img-Crypt
```

**Step 2:** Make Script Executable:

```bash
  chmod +x install.sh
  chmod +x uninstall.sh
  chmod +x img-crypt.py
```

**Step 3:** Convert Windows files to Linux

```bash
  dos2unix install.sh
  dos2unix uninstall.sh
  dos2unix img-crypt.py
```

**Step 4:** Script Installation

```bash
  ./install.sh
```

**Step 5:** Run the Utility from any Directory

```bash
  img-crypt
```
If you encounter any issues, feel free to **open an issue** on GitHub or reach out.

## 🔧 **Usage**

**Encoding a Message into an Image:**
- Select Encode a message *(Option 1)*.
- Choose to enter the text manually or load it from a file.
- Provide an image file *(JPEG or PNG format)*.
- Set a password *(Optional)*.
- Save the encoded image.

![Encoding a Message into an Image](https://github.com/manish-dalwani/Img-Crypt/blob/main/Snapshot/secret_insert.png?raw=true)


**Decoding a Message from an Image:**
- Select Decode a message *(Option 2)*.
- Provide the encoded image file.
- Enter the password *(if applicable)*.
- View or save the decoded message.

![Decoding a Message from an Image](https://github.com/manish-dalwani/Img-Crypt/blob/main/Snapshot/secret_extract.png?raw=true)


## 👨‍💻 **Authors**

- [@manish-dalwani](https://github.com/manish-dalwani)


## 🤝 **Contribute & Collaborate!**

👨‍💻 If you find bugs, discover vulnerabilities, or want to add features, feel free to open an issue or submit a pull request. Let’s make this tool even better together!

📬 Connect with me on [**LinkedIn**](https://www.linkedin.com/in/manish-dalwani/)

## 📜 **License**
This project is licensed under [MPL-2.0](https://github.com/manish-dalwani/Img-Crypt/blob/main/LICENSE), meaning you can freely use and modify the code, but selling it without permission is not allowed.



