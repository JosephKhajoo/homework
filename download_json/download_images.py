from fill_json import FillJson
from concurrent.futures import ThreadPoolExecutor
import logging
import requests
import json
import os


class ImageDownload():
	def __init__(self, web_link):
		self.web_link = web_link

		if not os.path.exists("images"):
			logging.info("Creating folder 'images'.")
			os.mkdir("images")
		
		a = FillJson(self.web_link)
		a.fill()

		with open("images.json", 'r') as file:
			self.data = json.load(file)["images"]

	def download(self, items):
		pic = requests.get(items["link"])
		with open(os.path.join("images", items["name"]), "wb") as write_file:
			logging.info(f"Downloading `{items['name']}`.")
			print(f"Downloading `{items['name']}`.")
			write_file.write(pic.content)

	def handler(self):
		try:
		    with ThreadPoolExecutor(max_workers=len(self.data)) as executor:
		    	logging.debug(self.data)
		    	logging.debug(f"{len(self.data)} threads created - {executor}")
		    	executor.map(self.download, self.data)
		except AttributeError:
			logging.error("Attribute error occured", exc_info=True)
		else:
		    logging.info("Done.")
		    print("\nDone. ")

img1 = ImageDownload("https://www.xkcd.com/")
img1.handler()
