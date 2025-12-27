from PIL import Image, PngImagePlugin
from datetime import datetime

def add_metadata(
    input_image: str,
    output_image: str,
    metadata: dict
):
    img = Image.open(input_image)

    png_info = PngImagePlugin.PngInfo()

    for key, value in metadata.items():
        png_info.add_text(key, str(value))

    img.save(output_image, pnginfo=png_info)
    print(f"Saved image with metadata -> {output_image}")

if __name__ == "__main__":
    metadata = {
        "Author": "Your Name",
        "Description": "Example image with metadata",
        "Created": datetime.now().isoformat(),
        "Software": "Python Pillow",
        "Project": "Image Metadata Encoder"
    }

    add_metadata(
        input_image="image.png",
        output_image="image_with_metadata.png",
        metadata=metadata
    )
