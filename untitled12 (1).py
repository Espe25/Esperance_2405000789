# -*- coding: utf-8 -*-
"""Untitled12.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1KMu45zG5sKpSsoHKvFv9EzwlVQKuLYHO
"""

import requests

def check_website(url):
    try:
        response = requests.get(url, timeout=5)
        return f"Website {url} is up (Status: {response.status_code})"
    except requests.exceptions.RequestException:
        return f"Website {url} is unreachable."

# Test the function with your URL
print(check_website("https://uok.ac.rw"))