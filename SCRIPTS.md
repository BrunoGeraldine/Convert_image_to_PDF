# Scripts Summary

## 📄 app.py
Basic image to PDF converter.
Processes all JPG/JPEG images from the 'image' folder.
Creates a 'pdfs' subfolder to store the results.
Each image becomes an individual PDF with the same name.

## 📄 merge_onlyone.py
Intelligent processor with folder suffix rules.
Analyzes '-uc' folders to create individual PDFs.
Analyzes '-fv' folders to create a single PDF per folder.
Maintains the hierarchical organization of the 'imagegroup' folder.

## 📄 merge_pdf.py
Existing PDF files unifier.
Combines all PDFs from a specific folder.
Creates a new PDF with the folder name.
Ignores the final file to avoid infinite loops.

## 📄 merge_all.py
Single PDF image grouper.
Processes all JPG images from a specific folder.
Combines all into a single 'contrato_completo.pdf' file.
Maintains alphabetical order of images in the final document.