Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
... 
... dict_size = random.randint(5, 10)
... 
... random_dict = {f"key_{i}": random.randint(1, 100) for i in range(dict_size)}
... 