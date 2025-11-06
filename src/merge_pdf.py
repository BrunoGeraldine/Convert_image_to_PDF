import os
from PyPDF2 import PdfMerger

# Specific subfolder path
target_folder = "../imagegroup/pasta_01/04-fv"  # adjust path as needed

# Check if folder exists
if not os.path.isdir(target_folder):
    print(f"❌ The folder {target_folder} doesn't exist.")
else:
    # List all PDFs in the folder (alphabetical order)
    pdf_files = sorted(
        [f for f in os.listdir(target_folder) if f.lower().endswith(".pdf")]
    )

    if not pdf_files:
        print(f"⚠️ No PDF files found in {target_folder}.")
    else:
        # Final PDF name = folder name
        folder_name = os.path.basename(target_folder)
        pdf_output = os.path.join(target_folder, f"{folder_name}.pdf")

        merger = PdfMerger()

        for file in pdf_files:
            pdf_path = os.path.join(target_folder, file)

            # Ignore the final PDF if it already exists (to avoid loops)
            if file == f"{folder_name}.pdf":
                continue

            merger.append(pdf_path)
            print(f"📎 Added: {file}")

        # Save the merged PDF
        merger.write(pdf_output)
        merger.close()

        print(f"✅ Final file created: {pdf_output}")
