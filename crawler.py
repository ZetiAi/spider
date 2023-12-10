# crawler.py

import aiohttp
from bs4 import BeautifulSoup
from collections import deque
from urllib.parse import urljoin, urlparse
from urllib.robotparser import RobotFileParser
import asyncio
import logging
import os 
import hashlib

# Configure logging
logging.basicConfig(level=logging.INFO)

def sanitize_url(url):
    return hashlib.md5(url.encode()).hexdigest()

def ensure_directory_exists(dir_name):
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

def save_html_to_disk(html, url):
    dir_name = 'html_files'
    ensure_directory_exists(dir_name)
    filename = sanitize_url(url)
    with open(os.path.join(dir_name, filename), 'w') as f:
        f.write(html)

async def fetch(session, url, delay=1):
    try:
        async with session.get(url) as response:
            await asyncio.sleep(delay)  # add delay here
            return await response.text()
    except aiohttp.ClientError as e:
        logging.error(f"Request failed for {url}: {str(e)}")
        return None

def extract_links(html, domain):
    soup = BeautifulSoup(html, 'html.parser')
    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']
        url = urljoin(domain, href)
        parsed_url = urlparse(url)
        if parsed_url.netloc == urlparse(domain).netloc:
            yield url

async def fetch_robots_rules(robots_url):
    try:
        parser = RobotFileParser()
        async with aiohttp.ClientSession() as session:
            content = await fetch(session, robots_url)
            parser.parse(content.splitlines())
        return parser
    except Exception as e:
        logging.error(f"Failed to fetch or parse robots.txt: {str(e)}")
        return None

async def crawl(start_url):
    robots_url = urljoin(start_url, '/robots.txt')
    robots_parser = await fetch_robots_rules(robots_url)

    visited = set()
    queue = deque([start_url])

    async with aiohttp.ClientSession() as session:
        while queue:
            current_url = queue.popleft()
            if current_url not in visited and (robots_parser is None or robots_parser.can_fetch('*', current_url)):
                visited.add(current_url)
                logging.info(f"Crawling URL: {current_url}")
                html = await fetch(session, current_url)
                if html:
                    save_html_to_disk(html, current_url)
                    for link in extract_links(html, start_url):
                        if link not in visited and (robots_parser is None or robots_parser.can_fetch('*', link)):
                            queue.append(link)

# Run the crawler
# asyncio.run(crawl('https://svelte.dev/docs'))
