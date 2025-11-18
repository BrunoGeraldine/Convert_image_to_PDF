from flask import Flask, request, send_file, render_template_string
from pdf2docx import Converter
import uuid
import os

app = Flask(__name__)

# Página inicial para upload
HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>PDF para Word</title>
</head>
<body>
    <h1>Converter PDF → Word</h1>
    <form action="/convert" method="post" enctype="multipart/form-data">
        <input type="file" name="pdf" accept="application/pdf" required>
        <button type="submit">Converter</button>
    </form>
</body>
</html>
"""

@app.route("/", methods=["GET"])
def index():
    return render_template_string(HTML)

@app.route("/convert", methods=["POST"])
def convert():
    if "pdf" not in request.files:
        return "Nenhum arquivo enviado", 400

    pdf_file = request.files["pdf"]
    
    # salva pdf temporário
    temp_pdf = f"/tmp/{uuid.uuid4()}.pdf"
    temp_docx = temp_pdf.replace(".pdf", ".docx")

    pdf_file.save(temp_pdf)

    # conversão PDF → DOCX
    converter = Converter(temp_pdf)
    converter.convert(temp_docx)
    converter.close()

    # download do DOCX
    return send_file(
        temp_docx,
        as_attachment=True,
        download_name=pdf_file.filename.replace(".pdf", ".docx")
    )

if __name__ == "__main__":
    app.run(debug=True)
