import os
import sys
import yaml
import re
from selenium import webdriver
from tempfile import mkdtemp
from bs4 import BeautifulSoup
import datetime
from datetime import timezone
import json
import threading
import requests

# TODO enrich the script urls as option
# TODO pass thread count as option + docker file
# TODO convert domain to ip


counter = 0
success = 0
failed = 0
errors = []
phuckers = []


def load_schema(schema_path):
    with open(schema_path, 'r') as file:
        if schema_path.endswith('.json'):
            schema = json.load(file)
        elif schema_path.endswith('.yaml') or schema_path.endswith('.yml'):
            schema = yaml.safe_load(file)
        else:
            raise ValueError("Unsupported schema format. Use .json or .yaml/.yml files.")
    return schema


def find_phuckers(raw):
    # TODO broke, need to fix
    for phucker in os.listdir('phuckers'):
        schema = load_schema(f'phuckers/{phucker}')
        for script in raw['pageScripts']:
            _ = re.match(schema["regex_pattern"], str(script))
            phuckers.append({"phucker": phucker, "url": _})


def get_openPhish():
    response = requests.get("https://www.openphish.com/feed.txt")
    if response.status_code == 200:
        urls = response.text.splitlines()
        return urls
    else:
        print(f"Failed to retrieve data: {response.status_code}")
        sys.exit()


def soupList(raw):
    listy = [str(x) for x in raw]
    return listy


def phuck(url):
    global success, failed
    data = {'utc': str(datetime.datetime.now(timezone.utc))[:19]}
    options = webdriver.ChromeOptions()
    service = webdriver.ChromeService("/app/chromedriver")
    options.binary_location = '/app/chrome/chrome'
    options.add_argument("--headless")
    options.add_argument('--no-sandbox')
    options.add_argument("--disable-gpu")
    options.add_argument('--ignore-ssl-errors')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--window-size=1280x1696")
    options.add_argument("--single-process")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-dev-tools")
    options.add_argument("--no-zygote")
    options.add_argument(f"--user-data-dir={mkdtemp()}")
    options.add_argument(f"--data-path={mkdtemp()}")
    options.add_argument(f"--disk-cache-dir={mkdtemp()}")
    options.add_argument("--remote-debugging-port=9222")
    options.set_capability('goog:loggingPrefs', {'browser': 'ALL', 'performance': 'ALL'})
    chrome = webdriver.Chrome(options=options, service=service)
    try:
        chrome.get(url)
    except Exception as e:
        failed += 1
        return {"error": f"Error: WebDriverException occurred. {e}"}
    dom = chrome.page_source
    data['pageTitle'] = chrome.title
    chrome.quit()
    soup = BeautifulSoup(dom, 'html.parser')
    script_tags = soup.find_all('script')
    link_tags = soup.find_all('link')
    data['url'] = url
    data['pageLinks'] = soupList(link_tags)
    data['pageScripts'] = soupList(script_tags)
    print(json.dumps(data, indent=4))


def main():
    global success, failed, errors
    urls = get_openPhish()

    def chunk_list(lst, num_chunks):
        chunk_size = len(lst) // num_chunks
        chunks = [lst[i:i+chunk_size] for i in range(0, len(lst), chunk_size)]
        if len(chunks) > num_chunks:
            chunks[-2] += chunks[-1]
            chunks = chunks[:-1]
        return chunks

    def process_chunk(chunk):
        global counter, success, failed, errors
        for url in chunk:
            counter += 1
            try:
                _ = phuck(url)
                find_phuckers(_)
                success += 1
            except Exception as e:
                errors.append(e)
                failed += 1
            print(counter)

    def process_chunks_in_parallel(lst):
        num_threads = 25
        chunks = chunk_list(lst, num_threads)
        threads = []

        for chunk in chunks:
            thread = threading.Thread(target=process_chunk, args=(chunk,))
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

    process_chunks_in_parallel(urls)
    print(f'Success: {success}')
    print(f'Failed: {failed}')
    print(f'Errors: {list(set(errors))}')
    print(f'phuckers: {phuckers}')


if __name__ == '__main__':
    main()
