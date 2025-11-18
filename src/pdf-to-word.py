from pdf2docx import Converter

def pdf_to_word(pdf_file, docx_file):
    # Cria o conversor
    converter = Converter(pdf_file)
    
    # Converte mantendo formatação
    converter.convert(docx_file, start=0, end=None)
    
    # Fecha o conversor
    converter.close()


# Exemplo de uso
pdf_to_word("entrada.pdf", "saida.docx")
