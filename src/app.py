import os
from PIL import Image

# Path to the images folder
images_folder = "../image"   # modify as needed

# Create output folder (if it doesn't exist)
output_folder = os.path.join(images_folder, "pdfs")
os.makedirs(output_folder, exist_ok=True)

# Loop through all files in the folder
for file in os.listdir(images_folder):
    if file.lower().endswith((".jpg", ".jpeg")):
        image_path = os.path.join(images_folder, file)
        
        # Open the image
        with Image.open(image_path) as img:
            # Convert to RGB mode (required for PDF)
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")
            
            # Define the PDF filename
            pdf_name = os.path.splitext(file)[0] + ".pdf"
            pdf_path = os.path.join(output_folder, pdf_name)
            
            # Save as PDF
            img.save(pdf_path, "PDF", resolution=100.0)
            print(f"✅ {file} converted to {pdf_name}")

print("\nConversion completed! PDFs are in the 'pdfs' folder.")
