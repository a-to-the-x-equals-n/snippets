from PIL import Image

# Open the image file
image_path = "slate.png"
image = Image.open(image_path)

# Get the most common color (assuming solid color background)
most_common_color = image.convert("RGB").getpixel((0, 0))

# Convert RGB to hex
hex_color = "#{:02X}{:02X}{:02X}".format(*most_common_color)
print(hex_color)