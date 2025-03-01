import queue
import requests
import sys
import threading

AGENT = "Mozzila/5.0 (x11; Linux x86_64: rv:19.0) Gecko/20100101 Firefox/19.0"
EXTENSIONS = [".php," ".bak", ".org", ".inc"]
TARGET = "http://testphp.vulnweb.com"
THREADS = 50
WORDLIST = "/home/tim/Downloads/all.txt"

def get_words(resume=None):
    def extend_words(word):
        if "." in word:
            words.put(f'/{word}/')
        else: words.put(f'/word/')

        for extension in EXTENTIONS:
            words.put(f'/{word}{extensions}')

    with open(WORDLIST) as f:
        raw_words =f.read()
        