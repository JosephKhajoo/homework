from fill_json import FillJson
from concurrent.futures import ThreadPoolExecutor
import logging
import requests
import json
import os

datefmt = "%d-%m-%Y %I:%H:%S"
logging.basicConfig(level=logging.DEBUG, filename="events.log", filemode="w", format="%(levelname)s: %(asctime)s - %(message)s", datefmt=datefmt)


class ImageDownload():
	def __init__(self, json_file):
		self.json_file = json_file
		if not os.path.exists("images"):
			logging.info("Creating folder 'images'.")
			os.mkdir("images")
		try:
			with open(json_file, "r") as file:
				self.data = json.load(file)["images"]
				logging.debug(f"Data from json file inside 'images'\n {self.data} {type(self.data)}")
		except FileNotFoundError:
			logging.error(f"File `{self.json_file}` was not found", exc_info=True)

	def download(self, items):
		pic = requests.get(items["link"])
		with open(os.path.join("images", items["name"]), "wb") as write_file:
			logging.info(f"Downloading `{items['name']}`.")
			print(f"Downloading `{items['name']}`.")
			write_file.write(pic.content)

	def handler(self):
		try:
		    with ThreadPoolExecutor(max_workers=len(self.data)) as executor:
		    	logging.debug(f"{len(self.data)} threads created - {executor}")
		    	executor.map(self.download, self.data)
		except AttributeError:
			logging.error("Attribute error occured", exc_info=True)
		else:
		    logging.info("Done.")
		    print("\nDone. ")

img1 = ImageDownload("images.json")
img1.handler()