from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from pdf2docx import Converter
import uuid
import os

app = FastAPI()

# Rota para verificar se a API está rodando
@app.get("/")
def home():
    return {"message": "API de conversão PDF → Word está rodando!"}


@app.post("/convert")
async def convert_pdf_to_word(pdf: UploadFile = File(...)):
    # Gera nomes temporários únicos
    temp_pdf = f"/tmp/{uuid.uuid4()}.pdf"
    temp_docx = temp_pdf.replace(".pdf", ".docx")

    # Salva o PDF temporário
    with open(temp_pdf, "wb") as f:
        f.write(await pdf.read())

    # Converte para Word
    try:
        converter = Converter(temp_pdf)
        converter.convert(temp_docx)
        converter.close()
    except Exception as e:
        return {"error": str(e)}

    # Retorna arquivo DOCX
    return FileResponse(
        temp_docx,
        media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        filename=pdf.filename.replace(".pdf", ".docx")
    )
