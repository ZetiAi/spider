import os

# Directory containing the text files
directory = 'text_files/'

# Initialize an empty string to store the concatenated content
concatenated_content = ''

# Iterate over each file in the directory
for filename in os.listdir(directory):
    # Check if the file is a text file
    if filename.endswith('.txt'):
        # Construct the full file path
        file_path = os.path.join(directory, filename)
        
        # Open and read the file content
        with open(file_path, 'r') as file:
            content = file.read()
            concatenated_content += content + '\n'  # Add a newline between files

# Optionally, write the concatenated content to a new file
with open('combined_text_files.txt', 'w') as output_file:
    output_file.write(concatenated_content)

print("Concatenation complete. Content written to 'combined_text_files.txt'.")
