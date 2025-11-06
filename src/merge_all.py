import os
from PIL import Image

# Path to the images folder
images_folder = "../imagegroup/pasta_01/04-fv"   # modify as needed
output_file = "../imagegroup/pasta_01/04-fv/contrato_completo.pdf"  # final PDF name

# List all JPG files in the folder (alphabetical order)
files = sorted(
    [f for f in os.listdir(images_folder) if f.lower().endswith(".jpg")]
)

# Ensure there are images in the folder
if not files:
    print("❌ No .JPG images found in the folder.")
else:
    images = []

    for file in files:
        path = os.path.join(images_folder, file)
        img = Image.open(path)
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")
        images.append(img)

    # The first image is the main one; others are added to the PDF
    images[0].save(
        output_file,
        save_all=True,
        append_images=images[1:],
        format="PDF",
        resolution=100.0
    )

    print(f"✅ PDF generated successfully: {output_file}")
