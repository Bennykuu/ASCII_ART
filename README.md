# ASCII_ART

This project is a creation of an ASCII art generator using Python and the Pillow library. The script takes an input image and processes it to create an ASCII art representation of the image by converting its pixels into corresponding ASCII characters based on their luminance.

### 1. How It Works

⋅⋅* Transforming Images into Grayscale: 
⋅⋅*The input image is converted to grayscale, so it only has brightness values. 

⋅⋅* Scaling Down:
⋅⋅*The image is scaled down to a smaller size using a factor

⋅⋅* ASCII Representation of Image:
⋅⋅*The input image is represented in ASCII using a predefined list of characters: [' ', '.', ':', '=', 'c', 'o', '?', '#', '%', '@'].
⋅⋅*Each character corresponds to a specific range of brightness, with ' ' representing the darkest and '@' representing the brightest regions.
⋅⋅*The luminance of each pixel is normalized to a range of [0, 1] and mapped to the corresponding character based on its brightness.

⋅⋅* Creating the ASCII Art Image:
⋅⋅*A new blank image of the same size as the original is created to hold the ASCII art.
⋅⋅*ASCII characters are drawn onto the new image at positions corresponding to their scaled locations in the original image.

⋅⋅*Output:
⋅⋅*The resulting ASCII art image is displayed.

As for some example

### Originales Bild:
![Original](example_Images/cat1.jpg)

### Transformation (ASCII Faktor 4):
→
![Transformation](example_Images/cat1_ascii_factor4.PNG)
