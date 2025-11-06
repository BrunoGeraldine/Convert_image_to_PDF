import os
from PIL import Image

# Caminho da pasta com as imagens
pasta_imagens = "../image"   # altere conforme necessário

# Cria uma pasta de saída (caso não exista)
pasta_saida = os.path.join(pasta_imagens, "pdfs")
os.makedirs(pasta_saida, exist_ok=True)

# Percorre todos os arquivos da pasta
for arquivo in os.listdir(pasta_imagens):
    if arquivo.lower().endswith((".jpg", ".jpeg")):
        caminho_imagem = os.path.join(pasta_imagens, arquivo)
        
        # Abre a imagem
        with Image.open(caminho_imagem) as img:
            # Converte para modo RGB (necessário para PDF)
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")
            
            # Define o nome do arquivo PDF
            nome_pdf = os.path.splitext(arquivo)[0] + ".pdf"
            caminho_pdf = os.path.join(pasta_saida, nome_pdf)
            
            # Salva como PDF
            img.save(caminho_pdf, "PDF", resolution=100.0)
            print(f"✅ {arquivo} convertido para {nome_pdf}")

print("\nConversão concluída! Os PDFs estão na pasta 'pdfs'.")
