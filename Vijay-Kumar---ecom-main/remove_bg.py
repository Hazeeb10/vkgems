from rembg import remove
from PIL import Image
import os

def process_img(input_path, output_path):
    try:
        input_image = Image.open(input_path)
        output_image = remove(input_image)
        output_image.save(output_path)
        print(f"Successfully removed background from {input_path}")
    except Exception as e:
        print(f"Failed {input_path}: {e}")

if __name__ == "__main__":
    process_img("public/images/logo_original.png", "public/images/logo.png")
    
    # We use the previous new logo image as input, it will overwrite itself
    process_img("public/images/new logo.png", "public/images/new logo.png")
