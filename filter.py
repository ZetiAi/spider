import os
from bs4 import BeautifulSoup

html_folder = 'html_files/'
text_folder = 'text_files/'

# Ensure text folder exists
if not os.path.exists(text_folder):
    os.makedirs(text_folder)

print("Starting script...")
print("Files found in html_files/:", os.listdir(html_folder))

# Iterate over all files in the HTML folder
for file_name in os.listdir(html_folder):
    print(f"Processing file: {file_name}")
    with open(os.path.join(html_folder, file_name), 'r', encoding='utf-8') as file:
        # Parse HTML content
        soup = BeautifulSoup(file, 'html.parser')
        text = soup.get_text()

        # Clean up the text: strip leading/trailing whitespace and remove empty lines
        cleaned_text = "\n".join(line.strip() for line in text.splitlines() if line.strip())

        # Generate a text file name (keeping the original file name)
        text_file_name = f"{os.path.splitext(file_name)[0]}.txt"

        # Write the cleaned text to a text file in the text_files folder
        with open(os.path.join(text_folder, text_file_name), 'w', encoding='utf-8') as text_file:
            text_file.write(cleaned_text)

print("Script completed.")
