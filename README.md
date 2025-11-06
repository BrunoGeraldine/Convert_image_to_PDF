# Image to PDF Converter

This project provides a set of Python scripts to convert and organize JPG images into PDF files, with different grouping and organization options.

## 📁 Directory Structure

```
.
├── image/                  # Folder for loose images
│   ├── pasta_01/          # Subfolder for image set
│   └── pasta_02/          # Subfolder for another set
│
├── imagegroup/            # Folder for grouped images
│   ├── pasta_01/         # Contains subfolders with -uc or -fv suffixes
│   ├── pasta_02/         # Same structure
│   └── pasta_03/         # Same structure
│
└── src/                  # Python Scripts
    ├── app.py
    ├── merge_onlyone.py
    ├── merge_pdf.py
    └── merge_all.py
```

### Folder Naming Convention
- Folders with `-uc` suffix: Generate individual PDFs for each image
- Folders with `-fv` suffix: Generate a single PDF containing all images

## 🛠️ Available Scripts

### 1. `app.py`
Basic script to convert loose images to individual PDFs.
- **Input**: JPG images in the `image` folder
- **Output**: Creates a `pdfs` folder with a PDF file for each image
- **Usage**: `python src/app.py`

### 2. `merge_onlyone.py`
Processes images in subfolders with specific rules based on suffix.
- **Input**: Images in folders of type `-uc` or `-fv` inside `imagegroup/pasta_XX`
- **Behavior**:
  - For `-uc` folders: Creates individual PDFs
  - For `-fv` folders: Creates a single PDF with all images
- **Usage**: `python src/merge_onlyone.py`

### 3. `merge_pdf.py`
Merges multiple PDF files into a single document.
- **Input**: PDF files in a specific folder
- **Output**: A single PDF file with the folder name
- **Usage**: `python src/merge_pdf.py`

### 4. `merge_all.py`
Combines all JPG images from a folder into a single PDF.
- **Input**: JPG images in a specific folder
- **Output**: A single PDF file named `contrato_completo.pdf`
- **Usage**: `python src/merge_all.py`

## 🚀 How to Use

1. Clone the repository
2. Install dependencies:
```bash
pip install Pillow PyPDF2
```

3. Organize your images in the appropriate folders:
   - Use `image/` for simple conversions
   - Use `imagegroup/` for conversions with grouping rules

4. Run the desired script according to your needs:
   - For simple conversions: `python src/app.py`
   - For grouping with rules: `python src/merge_onlyone.py`
   - For merging PDFs: `python src/merge_pdf.py`
   - For grouping all images: `python src/merge_all.py`

## ⚙️ Requirements

- Python 3.x
- Pillow (PIL)
- PyPDF2

## 📝 Notes

- Images are converted with 100.0 DPI resolution
- Images in RGBA or P mode are automatically converted to RGB
- Files are processed in alphabetical order
- Scripts include progress messages with emojis for better visualization

## 📄 License

This project is under the license included in the LICENSE file.
