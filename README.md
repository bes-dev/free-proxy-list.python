# free-proxy-list client

Simple python client to https://free-proxy-list.net/


## Requirements

* Linux, Windows, MacOS
* Python 3.8.+

## Install package

```bash
pip install free_proxy_list
```

## Install the latest version

```bash
git clone https://github.com/bes-dev/free-proxy-list.python
cd free-proxy-list.python
pip install .
```

## Example

```python
from free_proxy_list import FreeProxyListClient

client = FreeProxyListClient()
search_results = client.search(get_random_proxy=True)[0]
print(search_results)
search_results = client.search(https='yes', get_random_proxy=True)[0]
print(search_results)
search_results = client.search(https='yes', get_random_proxy=True, update_proxies=True)[0]
print(search_results)
```
