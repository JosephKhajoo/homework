import requests
import logging
import json
import time
import os

datefmt = "%d-%m-%Y %I:%H:%S"

logging.basicConfig(level=logging.DEBUG, filename="events.log", filemode="w", format="%(levelname)s: %(filename)s %(asctime)s - %(message)s", datefmt=datefmt)


class FillJson:
	def __init__(self, web_link):
		self.web_link = web_link
		self.image_links = {"images": []}
		if not os.path.exists("images.json"):
			with open("images.json", "w") as json_file:
				self.json_file = json_file
				json.dump(self.image_links, self.json_file, indent=2)
		else:
			self.json_file = "images.json"

	def find_all_indexes(self, input_str, search_str):
	    l1 = []
	    length = len(input_str)
	    index = 0
	    while index < length:
	        i = input_str.find(search_str, index)
	        if i == -1:
	            return l1
	        l1.append(i)
	        index = i + 1
	    return l1

	def get_filename(self, link):
		if "?" in link:
			name = link.split("?")[0].split("/")[-1]
		else:
			name = link.split("/")[-1]
		return name

	def json_dump(self, data):
		with open(self.json_file, "w") as file:
			logging.debug(f"Dumping into the json file - {data}")
			json.dump(data, file, indent=2)

	def fill(self):
		source = requests.get(self.web_link).text
		indexes = self.find_all_indexes(source, "png")

		for i in indexes:
			temp = source[:i+3]
			link = temp.split('"')[-1]
			logging.debug(f"Link generated from temp - {link}")
			if link[:4] == "http":
				logging.info(f"Found a link that starts with http - {link}")
				filename = self.get_filename(link)
				self.image_links["images"].append({"name": filename, "link": link})

			elif link[:2] == "//":
				link = "https:" + link
				logging.info(f"Found a link that starts with // the generated link is - {link}")
				filename = self.get_filename(link)
				self.image_links["images"].append({"name": filename, "link": link})

			elif link[0] == "/" and link[1] != "/":
				link = self.web_link + link
				filename = self.get_filename(link)
				logging.info(f"Found a link that starts with / the generated link is - {link}")
				self.image_links["images"].append({"name": filename, "link": link})

		self.json_dump(self.image_links)