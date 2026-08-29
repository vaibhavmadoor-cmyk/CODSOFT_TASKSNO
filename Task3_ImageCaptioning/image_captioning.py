from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import os


print("======================================")
print("       CODSOFT IMAGE CAPTIONING AI")
print("======================================")
print()


# Load the pre-trained image captioning model
print("Loading AI model...")

processor = BlipProcessor.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)

model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)

print("AI model loaded successfully!")
print()


def generate_caption(image_path):
    """Generate a caption for an image."""

    image = Image.open(image_path).convert("RGB")

    inputs = processor(images=image, return_tensors="pt")

    output = model.generate(**inputs, max_new_tokens=30)

    caption = processor.decode(
        output[0],
        skip_special_tokens=True
    )

    return caption


while True:

    image_path = input(
        "Enter the path of an image (or type 'exit' to quit): "
    ).strip()

    if image_path.lower() == "exit":
        print("Thank you for using the Image Captioning AI!")
        break

    # Remove quotes if the user copies a path with quotes
    image_path = image_path.strip('"').strip("'")

    if not os.path.exists(image_path):
        print("❌ Image not found. Please check the file path.")
        print()
        continue

    try:
        caption = generate_caption(image_path)

        print()
        print("🖼️ Image:", image_path)
        print("🤖 Generated Caption:", caption)
        print()

    except Exception as e:
        print("❌ Could not process the image.")
        print("Error:", e)
        print()