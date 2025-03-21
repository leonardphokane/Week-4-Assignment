# Week-4-Assignment

# Function to encrypt content using Caesar Cipher
def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text

# Function to read, encrypt, and write to a new file
def encrypt_file(input_filename, output_filename, shift):
    try:
        # Open the input file for reading
        with open(input_filename, 'r') as infile:
            content = infile.read()

        # Encrypt the content
        encrypted_content = caesar_cipher_encrypt(content, shift)

        # Write the encrypted content to the output file
        with open(output_filename, 'w') as outfile:
            outfile.write(encrypted_content)

        print(f"File content has been encrypted and written to {output_filename}")

    except FileNotFoundError:
        print(f"Error: The file {input_filename} does not exist.")

    except IOError as e:
        print(f"Error: {e}")

input_file = input("Enter the name of the file where content is stored: ") + ".txt"
output_file = input("Enter the name of the file where to update the content: ") + ".txt"
shift = 3
encrypt_file(input_file, output_file, shift)
