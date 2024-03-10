from PIL import Image
import os


def reduce_jpeg_quality(input_image_path, output_image_path, quality=85):
    # Open the image
    image = Image.open(input_image_path)

    # Save the image with reduced quality
    image.save(output_image_path, quality=quality)


# Example usage:
directoy = os.path.join(os.path.dirname(__file__), 'img')
fileList = os.listdir(directoy)

for i in range(len(fileList)):
    image_path = os.path.join(directoy, f"mockImage{i}.jpg")
    reduce_jpeg_quality(image_path, image_path, quality=1)
