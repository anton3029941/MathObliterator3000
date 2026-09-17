from pix2text import Pix2Text

# Initialize the model engine
p2t = Pix2Text.from_config()

# Path to your image
img_path = 'server/images/limit.jpg'

# Extract and recognize contents
results = p2t.recognize(img_path)

# Print out the results (includes positions, types, and raw string data)
for item in results:
    print(item, end="")