import os
from PyPDF2 import PdfMerger

# Caminho da subpasta específica
pasta_alvo = "../imagegroup/pasta_01/04-fv"  # ajuste o caminho conforme necessário

# Verifica se a pasta existe
if not os.path.isdir(pasta_alvo):
    print(f"❌ A pasta {pasta_alvo} não existe.")
else:
    # Lista todos os PDFs dentro da pasta (ordem alfabética)
    arquivos_pdf = sorted(
        [f for f in os.listdir(pasta_alvo) if f.lower().endswith(".pdf")]
    )

    if not arquivos_pdf:
        print(f"⚠️ Nenhum arquivo PDF encontrado em {pasta_alvo}.")
    else:
        # Nome do PDF final = nome da pasta
        nome_pasta = os.path.basename(pasta_alvo)
        pdf_saida = os.path.join(pasta_alvo, f"{nome_pasta}.pdf")

        merger = PdfMerger()

        for arquivo in arquivos_pdf:
            caminho_pdf = os.path.join(pasta_alvo, arquivo)

            # Ignora o PDF final se ele já existir (para evitar loops)
            if arquivo == f"{nome_pasta}.pdf":
                continue

            merger.append(caminho_pdf)
            print(f"📎 Adicionado: {arquivo}")

        # Salva o PDF agrupado
        merger.write(pdf_saida)
        merger.close()

        print(f"✅ Arquivo final criado: {pdf_saida}")
