import urllib.request
import concurrent.futures

URLS = ['https://mail.ru/',
        'https://youtube.com/',
        'https://yandex.ru'
        ]


# load one page
def load_url(url: str, timeout=10):
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()


with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
    future_to_url = {executor.submit(load_url, url): url for url in URLS}
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        try:
            data = future.result()
        except Exception as err:
            print(f'{url} raised exception {err}')
        else:
            print(f'{url} downloaded {len(data)} bytes')


