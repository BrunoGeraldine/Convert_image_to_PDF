import os
from PIL import Image



# Caminho da pasta com as imagens
pasta_imagens = "../imagegroup/pasta_01/04-fv"   # altere conforme necessário
arquivo_saida = "../imagegroup/pasta_01/04-fv/contrato_completo.pdf"  # nome do PDF final

# Lista todos os arquivos JPG da pasta (ordem alfabética)
arquivos = sorted(
    [f for f in os.listdir(pasta_imagens) if f.lower().endswith(".jpg")]
)

# Garante que há imagens na pasta
if not arquivos:
    print("❌ Nenhuma imagem .JPG encontrada na pasta.")
else:
    imagens = []

    for arquivo in arquivos:
        caminho = os.path.join(pasta_imagens, arquivo)
        img = Image.open(caminho)
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")
        imagens.append(img)

    # A primeira imagem é a principal; as demais são adicionadas ao PDF
    imagens[0].save(
        arquivo_saida,
        save_all=True,
        append_images=imagens[1:],
        format="PDF",
        resolution=100.0
    )

    print(f"✅ PDF gerado com sucesso: {arquivo_saida}")
