#!/usr/bin/env python3

from PIL import Image
# https://github.com/psibi/Rizzy/blob/master/stepic.py
import stepic
import base64
import os
import sys
import time
from cryptography.fernet import Fernet

from colorama import Style, Fore, Back, init, deinit
import random

# Initialize colorama for Windows compatibility
init(autoreset=True, convert=True)

# Deinitialize colorama (fixes some CMD issues)
deinit()

# Colors
# Function to print colored text
def ver_color(text, fg=Fore.RED, bg=Back.WHITE, style=Style.BRIGHT):
    return f"{style}{fg}{bg}{text}{Style.RESET_ALL}"

def blue_color(text, fcolor=Fore.BLUE, style=Style.BRIGHT):
    return f"{fcolor}{style}{text}{Style.RESET_ALL}"

def cyan_color(text, fcolor=Fore.CYAN, style=Style.BRIGHT):
    return f"{fcolor}{style}{text}{Style.RESET_ALL}"

def green_color(text, fcolor=Fore.GREEN, style=Style.BRIGHT):
    return f"{fcolor}{style}{text}{Style.RESET_ALL}"

def purple_color(text, fcolor=Fore.MAGENTA, style=Style.BRIGHT):
    return f"{fcolor}{style}{text}{Style.RESET_ALL}"

def red_color(text, fcolor=Fore.RED, style=Style.BRIGHT):
    return f"{fcolor}{style}{text}{Style.RESET_ALL}"

def white_color(text, fcolor=Fore.WHITE, style=Style.BRIGHT):
    return f"{fcolor}{style}{text}{Style.RESET_ALL}"

def yellow_color(text, fcolor=Fore.YELLOW, style=Style.BRIGHT):
    return f"{fcolor}{style}{text}{Style.RESET_ALL}"

# List of available color options from colorama
color_options = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]

# Randomly select a color from the list
selected_color = random.choice(color_options)

def exit_program():
    print()
    print(f"\n{yellow_color('⚠')} {red_color(' Interrupted by user.')}")
    print(green_color("👋 Exiting Img-Crypt..."))
    print(yellow_color("Thank you for using Img-Crypt!"))
    sys.exit(0)

def typewriter(text, delay=0.1):
    try:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()
    except KeyboardInterrupt:
        exit_program()

def safe_input(message):
    try:
        return input(message)
    except (KeyboardInterrupt, EOFError):
        exit_program()

def generate_key(password):
    return base64.urlsafe_b64encode(password.ljust(32)[:32].encode())

def encrypt_message(message, password):
    key = generate_key(password)
    cipher = Fernet(key)
    encrypted_message = cipher.encrypt(message.encode())
    return encrypted_message.decode()

def decrypt_message(encrypted_message, password):
    key = generate_key(password)
    cipher = Fernet(key)
    decrypted_message = cipher.decrypt(encrypted_message.encode())
    return decrypted_message.decode()

def get_valid_file(prompt, file_type):
    while True:
        file_name = safe_input(prompt).strip()
        if file_name:
            try:
                if file_type == "image":
                    return Image.open(file_name), file_name
                elif file_type == "text":
                    with open(file_name, 'r') as file:
                        return file.read(), file_name
            except Exception as e:
                print(red_color(f"❗ Error: {e}. Please enter a valid {file_type} file.\n"))
        else:
            print(red_color(f"❗ {file_type.capitalize()} file name cannot be empty.\n"))

def encode_text():
    img, img_path = get_valid_file(cyan_color("Enter image name or path with extension (e.g., image.jpg): "), "image")

    print()
    while True:
        print(f"{red_color('[')}{white_color('01')}{red_color(']')} {yellow_color('Enter text manually.')}")
        print(f"{red_color('[')}{white_color('02')}{red_color(']')} {yellow_color('Load text from a file.')}")
        option = safe_input(f"{blue_color('Select an option: ')}")
        print()
        if option in ['1', '01']:
            # message = ""
            # while not message.strip():
            #     message = input(f"{cyan_color('Enter the text to encode: ')}")
            #     if not message.strip():
            #         print(red_color("❗ Message cannot be empty. Please enter a valid message.\n"))
            # break
            while True:
                message = safe_input(cyan_color("Enter the text to encode: ")).strip()
                if message:
                    break
                print(red_color("❗ Message cannot be empty.\n"))
            break
        
        elif option in ['2', '02']:
            message, text_path = get_valid_file(cyan_color("Enter text file name or path with extension (e.g., S3cr3t.txt): "), "text")
            img_size, text_size = os.path.getsize(img_path), os.path.getsize(text_path)
            if text_size*3 > img_size:
                while True:
                    print(red_color("❗ Text file is larger than the image file."))
                    print()
                    print(f"{red_color('[')}{white_color('01')}{red_color(']')} {yellow_color('Provide a larger image file.')}")
                    print(f"{red_color('[')}{white_color('02')}{red_color(']')} {yellow_color('Provide a smaller text file.')}")
                    choice = safe_input(blue_color("Select an option: ")).strip()
                    print()
                    if choice == '1':
                        img, img_path = get_valid_file(cyan_color("Enter a larger image file: "), "image")
                        img_size = os.path.getsize(img_path)
                    elif choice == '2':
                        message, text_path = get_valid_file(cyan_color("Enter a smaller text file: "), "text")
                        text_size = os.path.getsize(text_path)
                    if img_size >= text_size*3:
                        break
            break
        else:
            print(red_color('❌ Invalid option. Please select a valid option.\n'))
    
    if safe_input(purple_color("\nDo you want to provide a password? (Y/N): ")).strip().lower() == "y":
        while True:
            password = safe_input(cyan_color("\nEnter password (8-32 characters): ")).strip()
            if 8 <= len(password) <= 32:
                message = encrypt_message(message, password)
                break
            print(red_color("❗ Password must be between 8 and 32 characters."))
    
    # encoded_img = stepic.encode(img, message.encode())

    try:
        if img.mode not in ("RGB", "RGBA", "CMYK"):
            img = img.convert("RGB")
        encoded_img = stepic.encode(img, message.encode())
    except Exception as e:
        print(red_color(f"❌ Unable to encode the image: {e}"))
        return

    while True:
        output_path = safe_input(cyan_color(f"\nEnter filename to save with extension (.bmp or .png): ")).strip()

        # Empty input
        if not output_path:
            output_path = "encoded_image.png"
            break

        # User entered only ".png" or ".bmp"
        if output_path in (".png", ".bmp"):
            print(red_color(f"❌ Please enter a valid filename (e.g., secret.png)"))
            continue

        # Valid extension
        if output_path.lower().endswith((".png", ".bmp")):
            break

        # Missing extension
        print(red_color("❌ Output filename must end with .png or .bmp"))

    try:
        encoded_img.save(output_path)
        print(green_color(f"\n✅ Encoded image saved as {output_path}\n"))
    except Exception as e:
        print(red_color(f"❌ Failed to save image: {e}"))

def decode_text():
    img, _ = get_valid_file(cyan_color("Enter encoded image name or path with extension (e.g., encoded_image.bmp): "), "image")
    try:
        decoded_message = stepic.decode(img)
        if not decoded_message:
            print(red_color("❌ This image does not contain any secret message."))
            return
    except Exception:
        print(red_color("❌ This image does not contain any secret message."))
        # print(red_color("\n❌ Error decoding the image. It may not contain any secret message.\n"))
        return
    
    if decoded_message.startswith("gAAAAA"):  # Encrypted text detected
        print(red_color('\n🔒 This image has a password-protected message.'))
        retries = 3
        while retries > 0:
            try:
                password = safe_input(cyan_color('Enter password to decode: '))
                decoded_message = decrypt_message(decoded_message, password)
                break
            except Exception:
            # except:
                retries -= 1
                print(red_color(f'Incorrect password. {retries} attempts left.\n'))
        if retries == 0:
            print(red_color('❗Maximum attempts reached. Exiting...\n'))
            return
    
    if len(decoded_message) > 100:
        choice = safe_input(purple_color("\nThe decoded message is long. Do you want to save it to a file? (Y/N): ")).strip().lower()

        if choice == "y":
            file_name = safe_input(cyan_color("\nEnter the file name to save the decoded message (e.g., output.txt): ")).strip()
        
            if not file_name.lower().endswith(('.txt')):
                file_name = "output.txt"

            with open(file_name, "w", encoding="utf-8") as file:
                file.write(decoded_message)
        
            # print(f"\n{green_color('✅ Decoded message saved in ')}", file_name)
            print(green_color(f'\n✅ Decoded message saved in {file_name}\n'))
        else:
            print(f"\n{green_color('✅ Decoded message:')}", decoded_message, "\n")
    else:
        print(f"\n{green_color('✅ Decoded message:')}", decoded_message, "\n")

def main():
    print()
    typewriter(red_color("DISCLAIMER: ") + yellow_color("This tool is intended for educational purposes only. Use it responsibly. The creator is not liable for any unethical or illegal use."), delay=0.015)

    logo = f"""
    {selected_color}{Style.BRIGHT}
       ____  __  __  ___        ___  ____  _  _  ____  ____ 
      (_  _)(  \\/  )/ __) ___  / __)(  _ \\( \\/ )(  _ \\(_  _)
       _)(_  )    (( (_-.(___)( (__  )   / \\  /  ) __/  )(  
      (____)(_/\\/\\_)\\___/      \\___)(_)\\_) (__) (__)   (__)    {ver_color('[v2.0]')}
    {Style.RESET_ALL}
    """

    print(logo)
    print(f"\n{red_color('LinkedIn:')} {cyan_color('https://www.linkedin.com/in/manish-dalwani/')}\n")
    print(f"{blue_color('~~~~~~~~~~~~~~~~~')} {green_color('Welcome to Basic Steganography Utility')} {blue_color('~~~~~~~~~~~~~~~~~')}")
    while True:
        print(f"\n{red_color('[')}{white_color('01')}{red_color(']')} {yellow_color('Encode a message into an Image')}")
        print(f"{red_color('[')}{white_color('02')}{red_color(']')} {yellow_color('Decode a message from an Image')}")
        option = safe_input(f"{blue_color('Select an option: ')}")
        print()

        if option in ['1', '01']:
            encode_text()
            break
        elif option in ['2', '02']:
            decode_text()
            break
        else:
            # print()
            print(f"{red_color('❌ Invalid option. Please select a valid option.')}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit_program()
