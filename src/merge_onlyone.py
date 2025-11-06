import os
from PIL import Image

# Main folder path
base_folder = "../imagegroup/pasta_01"  # adjust as needed

# Loop through all subfolders in the base folder
for subfolder_name in sorted(os.listdir(base_folder)):
    subfolder_path = os.path.join(base_folder, subfolder_name)
    
    # Check if it's a folder
    if not os.path.isdir(subfolder_path):
        continue

    # List all JPG files in the subfolder (alphabetical order)
    jpg_files = sorted(
        [f for f in os.listdir(subfolder_path) if f.lower().endswith(".jpg")]
    )

    if not jpg_files:
        print(f"⚠️ No .JPG images found in {subfolder_name}")
        continue

    # Case: subfolder type "-uc" → generate individual PDFs
    if subfolder_name.endswith("-uc"):
        for file in jpg_files:
            img_path = os.path.join(subfolder_path, file)
            pdf_name = os.path.splitext(file)[0] + ".pdf"
            pdf_path = os.path.join(subfolder_path, pdf_name)

            with Image.open(img_path) as img:
                if img.mode in ("RGBA", "P"):
                    img = img.convert("RGB")
                img.save(pdf_path, "PDF", resolution=100.0)

            print(f"✅ {file} converted separately to {pdf_name}")

    # Case: subfolder type "-fv" → generate single PDF with all images
    elif subfolder_name.endswith("-fv"):
        images = []
        for file in jpg_files:
            img_path = os.path.join(subfolder_path, file)
            img = Image.open(img_path)
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")
            images.append(img)

        if images:
            pdf_name = f"{subfolder_name}.pdf"
            pdf_path = os.path.join(subfolder_path, pdf_name)

            images[0].save(
                pdf_path,
                save_all=True,
                append_images=images[1:],
                format="PDF",
                resolution=100.0
            )

            print(f"✅ Folder {subfolder_name} grouped into {pdf_name}")

    else:
        print(f"⚠️ The folder {subfolder_name} doesn't follow the '-uc' or '-fv' pattern and was ignored.")

print("\n🎉 Conversion completed successfully!")
