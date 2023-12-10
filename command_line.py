# command_line.py

import argparse
from crawler import crawl
import asyncio

def parse_args(args=None):
    parser = argparse.ArgumentParser(description='Svelte Documentation Spider CLI')
    parser.add_argument('--url', type=str, default='https://svelte.dev/docs', help='The URL to start scraping from')
    return parser.parse_args(args)

def main():
    args = parse_args()
    print(f"Starting spider at: {args.url}")
    try:
        asyncio.run(crawl(args.url))
    except Exception as e:
        print(f"An error occurred while running the crawler: {str(e)}")

if __name__ == '__main__':
    main()