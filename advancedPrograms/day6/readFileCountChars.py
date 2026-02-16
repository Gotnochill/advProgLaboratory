

# Read test.txt and count characters
try:
	with open("test.txt", "r") as f:
		content = f.read()
		print(content)
		print("Number of characters:", len(content))
except FileNotFoundError:
	print("File not found.")