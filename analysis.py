# Path to the file
file_path = 'combined_text_files.txt'

# Open and read the file
with open(file_path, 'r') as file:
    content = file.read()

# Get the number of characters
num_characters = len(content)

print(f"The file contains {num_characters} characters.")
