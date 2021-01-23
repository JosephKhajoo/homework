from random import randint
import logging

logging.basicConfig(filename="logs.txt", filemode="w", format="%(levelname)s: %(message)s - %(asctime)s", level=logging.DEBUG)

for i in range(10):
	rand = randint(0, 50)
	if rand <= 9 and rand >= 0:
		logging.debug(f"The number {rand} is between this range (0, 9)")
	elif rand <= 19 and rand >= 10:
		logging.info(f"The number {rand} is between this range (10, 19)")
	elif rand <= 29 and rand >= 20:
		logging.warning(f"The number {rand} is between this range (20, 29)")
	elif rand <= 39 and rand >= 30:
		logging.error(f"The number {rand} is between this range (30, 39)")
	elif rand <= 50 and rand >= 40:
		logging.critical(f"The number {rand} is between this range (40, 50)")