import tkinter as tk
import json
from tkinter import messagebox

# FUNÇÃO DO LOGIN

def fazer_login():
    usuario = campo_usuario.get()
    senha = campo_senha.get()

    if usuario == "admin" and senha == "123":
        print("Login realizado com sucesso!")
        abrir_sistema()
    else:
        print("Usuário ou senha incorretos!")
        messagebox.showerror("Erro", "Usuário ou senha incorretos!")


# DADOS DAS PENDÊNCIAS

ARQUIVO_DADOS = "pendencias.json"

def carregar_pendencias():
    try:
        with open(ARQUIVO_DADOS, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

def salvar_pendencias():
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as arquivo:
        json.dump(pendencias, arquivo, ensure_ascii=False, indent=4)

pendencias = carregar_pendencias()        
        
# ATUALIZA A LISTBOX COM AS PENDÊNCIAS ATUAIS

def atualizar_lista():
    lista_pendencias.delete(0, tk.END)
    for p in pendencias:
        lista_pendencias.insert(tk.END, f"{p['descricao']} - Responsável: {p['responsavel']}")


# JANELA DE NOVA PENDÊNCIA

def nova_pendencia():
    janela = tk.Toplevel(sistema)
    janela.title("Nova Pendência")
    janela.geometry("400x300")

    label_descricao = tk.Label(janela, text="Descrição")
    label_descricao.pack(pady=(15, 0))

    campo_descricao = tk.Entry(janela, width=40)
    campo_descricao.pack()

    label_responsavel = tk.Label(janela, text="Responsável")
    label_responsavel.pack(pady=(15, 0))

    campo_responsavel = tk.Entry(janela, width=40)
    campo_responsavel.pack()

    def cadastrar():
        descricao = campo_descricao.get().strip()
        responsavel = campo_responsavel.get().strip()

        if descricao == "" or responsavel == "":
            messagebox.showwarning("Atenção", "Preencha todos os campos!")
            return

        pendencias.append({
            "descricao": descricao,
            "responsavel": responsavel
        })

        salvar_pendencias()
        atualizar_lista()
        print(f"Pendência cadastrada: {descricao} - {responsavel}")
        janela.destroy()

    botao_cadastrar = tk.Button(janela, text="Cadastrar", command=cadastrar)
    botao_cadastrar.pack(pady=20)


# SEGUNDA TELA (SISTEMA)

def abrir_sistema():
    tela_login.destroy()

    global sistema, lista_pendencias

    sistema = tk.Tk()
    sistema.title("Sistema de Controle de Pendências")
    sistema.geometry("500x400")

    titulo = tk.Label(
        sistema,
        text="Sistema de Controle de Pendências",
        font=("Arial", 18)
    )
    titulo.pack(pady=20)

    botao_nova = tk.Button(
        sistema,
        text="Nova pendência",
        command=nova_pendencia
    )
    botao_nova.pack(pady=10)

    lista_pendencias = tk.Listbox(sistema, width=60, height=12)
    lista_pendencias.pack(pady=10)
    atualizar_lista()

    sistema.mainloop()


# JANELA DE LOGIN

tela_login = tk.Tk()
tela_login.title("Login")
tela_login.geometry("400x300")

titulo = tk.Label(
    tela_login,
    text="Login",
    font=("Arial", 20)
)
titulo.pack(pady=20)


# USUÁRIO

label_usuario = tk.Label(
    tela_login,
    text="Usuário"
)
label_usuario.pack()

campo_usuario = tk.Entry(tela_login)
campo_usuario.pack()


# SENHA

label_senha = tk.Label(
    tela_login,
    text="Senha"
)
label_senha.pack()

campo_senha = tk.Entry(
    tela_login,
    show="*"
)
campo_senha.pack()


# BOTÃO LOGIN

botao_login = tk.Button(
    tela_login,
    text="Entrar",
    command=fazer_login
)
botao_login.pack(pady=20)

tela_login.mainloop()
