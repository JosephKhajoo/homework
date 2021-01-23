import json
import requests
import time

# class FillJson:
# 	def __init__(self, link):
# 		self.link = link
# 		if not os.path.exists("images.json"):
# 			with open("images.json", "w") as json_file:
# 				self.json_file = json_file

# 	def get_links(self):
# 		resp = requests.get(self.link)

def get_links():
	links = []

	main_link = "https://xkcd.com"

	source = requests.get(main_link).text
	png_index = 0

	print(source, file="temp.txt")

	while png_index != -1:
		time.sleep(0.5)
		png_index = source.find("png", png_index) + 3

		print(png_index)
		source = source[:png_index]
		links.append(source.split('"')[-1])

		source = source[png_index + 3:]

	return links

print(get_links())