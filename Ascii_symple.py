from PIL import Image, ImageDraw

class ASCIIArt:
    def __init__(self, image_path, factor=8):
        self.image_path = image_path.strip().strip('"').strip("'")  # Falls User Anführungszeichen nutzt
        self.factor = factor
        self.ASCII = [' ', '.', ':', '=', 'c', 'o', '?', '#', '%', '@']
        self.image = Image.open(self.image_path).convert("L")

    def generate_ascii_art(self):
        # Downsampling: Bild auf ein Achtel der Größe verkleinern ( 8 x 8 )
        downsized = self.image.resize((self.image.size[0] // self.factor, self.image.size[1] // self.factor), Image.Resampling.LANCZOS)

        # Neues Bild erstellen für die Ausgabe
        output_image = Image.new("RGB", self.image.size, "black")
        draw = ImageDraw.Draw(output_image)

        pixels = downsized.load() # Pixel-Access-Objekt

        for y in range(downsized.height):
            for x in range(downsized.width):
                luminance = pixels[x, y] / 255  # Normalisiere auf Bereich [0, 1]

                # for replacing the pixels
                uv_x = (x % self.factor) / self.factor + luminance    # x is pixel position and mod by 8 to put it in the 8x8 range of the ascii charater size
                uv_y = (y % self.factor) / self.factor

                index = min(int(luminance * (len(self.ASCII) - 1)), len(self.ASCII) - 1) # [0,9]
                symbol = self.ASCII[index]

                draw.text((x * self.factor, y * self.factor), symbol, fill="white")

        return output_image

    def show_ascii_image(self):
        img = self.generate_ascii_art()
        img.show()

    def save_ascii_image(self, output_path="ascii_output.jpg"):
        img = self.generate_ascii_art()
        img.save(output_path)

# Nutzung:
picture = input("Which image do you want to use: ")
ascii_art = ASCIIArt(picture, factor=8)
ascii_art.show_ascii_image()
ascii_art.save_ascii_image("ascii_output.jpg")
