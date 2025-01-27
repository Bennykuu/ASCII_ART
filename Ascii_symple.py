from PIL import Image, ImageDraw

picture = input("which image do you wanna us:").strip().strip('"').strip("'")
image = Image.open(picture).convert("L")

factor = 8
ASCII = [' ', '.', ':', '=', 'c', 'o', '?', '#', '%', '@']

# Downsampling: Bild auf ein Achtel der Größe verkleinern ( 8 x 8 )
downsized = image.resize((image.size[0] // factor, image.size[1] // factor), Image.Resampling.LANCZOS)

# Neues Bild erstellen für die Ausgabe
output_image = Image.new("RGB", image.size, "black")
draw = ImageDraw.Draw(output_image)

pixels = downsized.load() # Pixel-Access-Objekt
for y in range(downsized.height):
    for x in range(downsized.width):
        luminance = pixels[x, y] / 255  # Normalisiere auf Bereich [0, 1]

        #for replacing the pixels
        uv_x = (x % factor) / factor + luminance # x is pixel position and mod by 8 to put it in the 8x8 range of the ascii charater size
        uv_y = (y % factor) / factor 

        index = min(int(luminance * (len(ASCII)-1)), len(ASCII) - 1) # [0,9]
        symbol = ASCII[index]

        draw.text((x * factor, y * factor), symbol, fill="white")

output_image.show()
