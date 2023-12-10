# Spider

This is a command line based program that allows you to search for all the HTML pages on a webpage. This Python script (`crawler.py`) is an asynchronous web crawler that visits web pages starting from a given URL, extracts and follows links within the same domain, and saves the HTML content of each page to disk. It respects `robots.txt` rules of the domain.

## Features

- Asynchronous requests using `aiohttp`
- Parsing HTML content with `BeautifulSoup`
- Robots.txt compliance checking
- Saving HTML content to disk
- Delayed requests to avoid server overload

## Prerequisites

Before you begin, ensure you have installed:

- Python 3.12 or later
- `aiohttp`
- `bs4` (BeautifulSoup)

These can be installed via `poetry` as detailed in the installation instructions.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/ZetiAi/spider
   ```

2. Navigate to the cloned directory:

   \```bash
   cd [directory]
   \```

3. Install dependencies using poetry:

   \```bash
   poetry install
   \```

## Usage

To run the program, use the following command:

\```bash
poetry run python command_line.py --url [start URL]
\```

Replace `[start URL]` with the URL you want to start crawling from.

## How It Works

1. **Initialization**: The script starts at the provided URL.
2. **Robots.txt**: Fetches `robots.txt` from the domain and parses it.
3. **Crawling**: Begins crawling from the start URL, following links within the same domain.
4. **Saving**: Saves the HTML of each visited page in a directory named `html_files`.
5. **Respectful Crawling**: Includes a delay between requests and checks `robots.txt` for permissions.

## Additional Features

The following command will remove all the HTML code from a directory into a `text_files/`

\```bash
poetry run python filter.py 
\```

The following command will concat all the files into a single file called `combined_text_files`

\```bash
poetry run python join.py
\```

## Logging

The script uses Python's `logging` module to log its activity. By default, it is set to the INFO level.

## Contributing

Contributions to improve this script are welcome. Please follow standard practices for code contributions.


