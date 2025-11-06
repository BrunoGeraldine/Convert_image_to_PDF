# Conversor de Imagens para PDF

Este projeto oferece um conjunto de scripts Python para converter e organizar imagens JPG em arquivos PDF, com diferentes opções de agrupamento e organização.

## 📁 Estrutura de Diretórios

```
.
├── image/                  # Pasta para imagens soltas
│   ├── pasta_01/          # Subpasta para conjunto de imagens
│   └── pasta_02/          # Subpasta para outro conjunto
│
├── imagegroup/            # Pasta para imagens agrupadas
│   ├── pasta_01/         # Contém subpastas com sufixos -uc ou -fv
│   ├── pasta_02/         # Mesma estrutura
│   └── pasta_03/         # Mesma estrutura
│
└── src/                  # Scripts Python
    ├── app.py
    ├── agrupa-cada.py
    ├── agrupa-pdf.py
    └── agrupa-todos.py
```

### Nomenclatura das Pastas
- Pastas com sufixo `-uc`: Geram PDFs individuais para cada imagem
- Pastas com sufixo `-fv`: Geram um único PDF contendo todas as imagens

## 🛠️ Scripts Disponíveis

### 1. `app.py`
Script básico para converter imagens soltas em PDFs individuais.
- **Entrada**: Imagens JPG na pasta `image`
- **Saída**: Cria uma pasta `pdfs` com um arquivo PDF para cada imagem
- **Uso**: `python src/app.py`

### 2. `agrupa-cada.py`
Processa imagens em subpastas com regras específicas baseadas no sufixo.
- **Entrada**: Imagens em pastas do tipo `-uc` ou `-fv` dentro de `imagegroup/pasta_XX`
- **Comportamento**:
  - Para pastas `-uc`: Cria PDFs individuais
  - Para pastas `-fv`: Cria um único PDF com todas as imagens
- **Uso**: `python src/agrupa-cada.py`

### 3. `agrupa-pdf.py`
Une múltiplos arquivos PDF em um único documento.
- **Entrada**: Arquivos PDF em uma pasta específica
- **Saída**: Um arquivo PDF único com o nome da pasta
- **Uso**: `python src/agrupa-pdf.py`

### 4. `agrupa-todos.py`
Combina todas as imagens JPG de uma pasta em um único PDF.
- **Entrada**: Imagens JPG em uma pasta específica
- **Saída**: Um arquivo PDF único chamado `contrato_completo.pdf`
- **Uso**: `python src/agrupa-todos.py`

## 🚀 Como Usar

1. Clone o repositório
2. Instale as dependências:
```bash
pip install Pillow PyPDF2
```

3. Organize suas imagens nas pastas apropriadas:
   - Use `image/` para conversões simples
   - Use `imagegroup/` para conversões com regras de agrupamento

4. Execute o script desejado conforme sua necessidade:
   - Para conversões simples: `python src/app.py`
   - Para agrupamento com regras: `python src/agrupa-cada.py`
   - Para unir PDFs: `python src/agrupa-pdf.py`
   - Para agrupar todas as imagens: `python src/agrupa-todos.py`

## ⚙️ Requisitos

- Python 3.x
- Pillow (PIL)
- PyPDF2

## 📝 Notas

- As imagens são convertidas com resolução de 100.0 DPI
- Imagens em modo RGBA ou P são automaticamente convertidas para RGB
- Os arquivos são processados em ordem alfabética
- Os scripts incluem mensagens de progresso com emojis para melhor visualização

## 📄 Licença

Este projeto está sob a licença incluída no arquivo LICENSE.
