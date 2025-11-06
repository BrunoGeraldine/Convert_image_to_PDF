# Resumo dos Scripts

## 📄 app.py
Conversor básico de imagens para PDF.
Processa todas as imagens JPG/JPEG da pasta 'image'.
Cria uma subpasta 'pdfs' para armazenar os resultados.
Cada imagem se torna um PDF individual com o mesmo nome.

## 📄 agrupa-cada.py
Processador inteligente com regras por sufixo de pasta.
Analisa pastas '-uc' para criar PDFs individuais.
Analisa pastas '-fv' para criar um PDF único por pasta.
Mantém a organização hierárquica da pasta 'imagegroup'.

## 📄 agrupa-pdf.py
Unificador de arquivos PDF existentes.
Combina todos os PDFs de uma pasta específica.
Cria um novo PDF com o nome da pasta.
Ignora o arquivo final para evitar loops infinitos.

## 📄 agrupa-todos.py
Agrupador de imagens em PDF único.
Processa todas as imagens JPG de uma pasta específica.
Combina todas em um único arquivo 'contrato_completo.pdf'.
Mantém a ordem alfabética das imagens no documento final.