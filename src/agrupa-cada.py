import os
from PIL import Image

# Caminho da pasta principal
pasta_base = "../imagegroup/pasta_01"  # ajuste se necessário

# Percorre todas as subpastas dentro da pasta base
for nome_subpasta in sorted(os.listdir(pasta_base)):
    caminho_subpasta = os.path.join(pasta_base, nome_subpasta)
    
    # Verifica se é uma pasta
    if not os.path.isdir(caminho_subpasta):
        continue

    # Lista todos os arquivos JPG dentro da subpasta (ordem alfabética)
    arquivos_jpg = sorted(
        [f for f in os.listdir(caminho_subpasta) if f.lower().endswith(".jpg")]
    )

    if not arquivos_jpg:
        print(f"⚠️ Nenhuma imagem .JPG encontrada em {nome_subpasta}")
        continue

    # Caso: subpasta tipo "-uc" → gerar PDFs individuais
    if nome_subpasta.endswith("-uc"):
        for arquivo in arquivos_jpg:
            caminho_img = os.path.join(caminho_subpasta, arquivo)
            nome_pdf = os.path.splitext(arquivo)[0] + ".pdf"
            caminho_pdf = os.path.join(caminho_subpasta, nome_pdf)

            with Image.open(caminho_img) as img:
                if img.mode in ("RGBA", "P"):
                    img = img.convert("RGB")
                img.save(caminho_pdf, "PDF", resolution=100.0)

            print(f"✅ {arquivo} convertido separadamente em {nome_pdf}")

    # Caso: subpasta tipo "-fv" → gerar PDF único com todas as imagens
    elif nome_subpasta.endswith("-fv"):
        imagens = []
        for arquivo in arquivos_jpg:
            caminho_img = os.path.join(caminho_subpasta, arquivo)
            img = Image.open(caminho_img)
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")
            imagens.append(img)

        if imagens:
            nome_pdf = f"{nome_subpasta}.pdf"
            caminho_pdf = os.path.join(caminho_subpasta, nome_pdf)

            imagens[0].save(
                caminho_pdf,
                save_all=True,
                append_images=imagens[1:],
                format="PDF",
                resolution=100.0
            )

            print(f"✅ Pasta {nome_subpasta} agrupada em {nome_pdf}")

    else:
        print(f"⚠️ A pasta {nome_subpasta} não segue o padrão '-uc' ou '-fv' e foi ignorada.")

print("\n🎉 Conversão concluída com sucesso!")
