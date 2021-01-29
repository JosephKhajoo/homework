import logging
import time

def function_timer(filename="output.txt") -> callable:
	def wrapper(func: callable) -> callable:
		def decor(*args):
			start = time.time()
			result = func(*args)
			finish = time.time() - start
			try:
				with open(filename, "w") as file:
					file.write(f"{result}\n\nFinished in {finish} seconds.")
			except Exception as e:
				logging.error(f"An error occurred in `decor` function - {e}")

			print(f"Finished in {finish} seconds")
		return decor
	return wrapper


@function_timer("file.txt")
def my_func(num):
	a = [i ** 4 for i in range(num)]
	return a

my_func(1000)
