# Define a function to read from a file
def read_file(file_path):
    try:
        with open(file_path, "r") as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
        return None
    except IOError as e:
        print(f"Error reading the file: {e}")
        return None

# Define a function to modify the content
def modify_content(content):
    # Example modification: Convert text to uppercase and add a footer
    modified_content = content.upper()
    modified_content += "\n\n--- End of File ---"
    return modified_content

# Define a function to write to a new file
def write_file(file_path, content):
    try:
        with open(file_path, "w") as file:
            file.write(content)
    except IOError as e:
        print(f"Error writing to the file: {e}")

# Define a function to create input.txt if it doesn't exist
def create_input_file():
    try:
        with open("input.txt", "w") as input_file:
            input_file.write("This is the first line.\n")
            input_file.write("Here is the second line.\n")
            input_file.write("The third line is here.\n")
            input_file.write("This is the fourth line.\n")
            input_file.write("Finally, the fifth line.\n")
        print("The file 'input.txt' has been created successfully!")
    except IOError as e:
        print(f"Error creating the file: {e}")

# Main execution
def main():
    input_file = "input.txt"  # Path to the input file
    output_file = "output.txt"  # Path to the output file

    # Ensure input.txt exists
    create_input_file()

    # Step 1: Read the original file's contents
    content = read_file(input_file)
    if content is None:
        return  # Exit if the file could not be read

    # Step 2: Modify the content
    modified_content = modify_content(content)

    # Step 3: Write the modified content to a new file
    write_file(output_file, modified_content)

    # Step 4: Print a success message
    print(f"Success! The modified content has been written to '{output_file}'.")

# Call the main function
if __name__ == "__main__":
    main()
