import tkinter as tk
from tkinter import filedialog, messagebox
from pdf2docx import Converter
import threading

def select_pdf():
    filename = filedialog.askopenfilename(
        title="Selecione um arquivo PDF",
        filetypes=[("Arquivo PDF", "*.pdf")]
    )
    if filename:
        pdf_path_var.set(filename)

def select_output():
    filename = filedialog.asksaveasfilename(
        title="Salvar como",
        defaultextension=".docx",
        filetypes=[("Documento Word", "*.docx")]
    )
    if filename:
        output_path_var.set(filename)

def convert_pdf_to_word():
    pdf_path = pdf_path_var.get()
    output_path = output_path_var.get()

    if not pdf_path:
        messagebox.showerror("Erro", "Selecione um arquivo PDF.")
        return

    if not output_path:
        messagebox.showerror("Erro", "Escolha onde salvar o arquivo Word.")
        return

    status_var.set("Convertendo... Aguarde.")
    
    def run_conversion():
        try:
            converter = Converter(pdf_path)
            converter.convert(output_path)
            converter.close()

            status_var.set("Conversão concluída!")
            messagebox.showinfo("Sucesso", "PDF convertido para Word com sucesso!")
        except Exception as e:
            status_var.set("Erro na conversão.")
            messagebox.showerror("Erro", f"Ocorreu um erro:\n{e}")

    # Rodar em thread separada (mantém GUI responsiva)
    threading.Thread(target=run_conversion).start()


# ------------------------------
# GUI (Tkinter)
# ------------------------------
root = tk.Tk()
root.title("Conversor PDF para Word")
root.geometry("500x250")
root.resizable(False, False)

pdf_path_var = tk.StringVar()
output_path_var = tk.StringVar()
status_var = tk.StringVar()

# Título
tk.Label(root, text="Conversor PDF → Word", font=("Arial", 16, "bold")).pack(pady=10)

# Seletor PDF
tk.Label(root, text="Arquivo PDF:").pack(anchor="w", padx=20)
frame1 = tk.Frame(root)
frame1.pack(padx=20, fill="x")
tk.Entry(frame1, textvariable=pdf_path_var, width=50).pack(side="left", padx=5)
tk.Button(frame1, text="Selecionar", command=select_pdf).pack(side="right")

# Seletor de saída
tk.Label(root, text="Salvar como (DOCX):").pack(anchor="w", padx=20, pady=(10,0))
frame2 = tk.Frame(root)
frame2.pack(padx=20, fill="x")
tk.Entry(frame2, textvariable=output_path_var, width=50).pack(side="left", padx=5)
tk.Button(frame2, text="Salvar", command=select_output).pack(side="right")

# Botão converter
tk.Button(root, text="Converter", font=("Arial", 12, "bold"),
          command=convert_pdf_to_word, bg="#4CAF50", fg="white").pack(pady=15)

# Status
tk.Label(root, textvariable=status_var, fg="blue").pack()

root.mainloop()
