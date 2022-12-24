from tkinter import *
import random

def adicionar_palavra():
    if not (palavra_entry.get().isalpha() and dica_entry.get().isalpha()):
        palavra_entry.delete(0, END)
        dica_entry.delete(0, END)
        mensagem_label_tela_add["text"] = "Por favor, digite palavras validas"
        return
    with open("palavras.txt", 'a') as arquivo:
        arquivo.write(f'{palavra_entry.get()},{dica_entry.get()}\n')
    palavra_entry.delete(0, END)
    dica_entry.delete(0, END)
    mensagem_label_tela_add["text"] = "Palavra e Dica adicionadas"

def add_leaderboard():
    global palavra
    global pontos
    global erros
    global nome

    with open("leaderboard.txt", 'a') as arquivo:
        arquivo.write(f'{nome},{palavra},{pontos},{erros}\n')

def sortear_palavra():
    global palavra
    global dica
    global palavra_oculta

    palavra_oculta = ""

    with open("palavras.txt") as arquivo:
        itens = arquivo.readlines()

    indice = random.randint(0, len(itens) - 1)
    palavra, dica = itens[indice].strip().split(",")

    palavra_oculta = "-" * len(palavra)

def jogar():
    global letra
    global palavra
    global pontos
    global erros
    global letras_acertadas
    global nome
    global palavra_oculta

    if not nome_entry.get().isalpha():
        nome_entry.delete(0, END)
        mensagem_label_tela_add["text"] = "Por favor, digite um nome valido"
        return

    nome = nome_entry.get()
    nome_entry.delete(0, END)

    palavra = ""
    erros = 0
    pontos = 0
    letras_acertadas = ""
    palavra_oculta = ""
    sortear_palavra()

    letra_entry.pack()
    botao_enviar_letra.pack()

    frame_pack(tela_jogo, tela_nome)

def atualiza_palavra():
    global letra
    global palavra
    global letras_acertadas

    palavra_atualizada = ""
    for letra in palavra:
        if letra in letras_acertadas:
            palavra_atualizada += letra
        else:
            palavra_atualizada += "-"
    return palavra_atualizada

def esquarteja(erros):
    if erros == 1:
        canvas.delete(perna_dir)
    elif erros == 2:
        canvas.delete(perna_esq)
    elif erros == 3:
        canvas.delete(braco_dir)
    elif erros == 4:
        canvas.delete(braco_esq)
    elif erros == 5:
        canvas.delete(tronco)
    else:
        canvas.delete(cabeca)

def enviar_letra():
    global letra
    global palavra
    global pontos
    global erros
    global letras_acertadas
    global nome

    mensagem["text"] = ""

    if not letra_entry.get().isalpha() or len(letra_entry.get()) != 1:
        letra_entry.delete(0, END)
        mensagem["text"] = "Por favor, digite uma letra valida"
        return
    
    letra = letra_entry.get()
    mensagem["text"] = f"Letra: {letra}"
        
    letra_entry.delete(0, END)

    if letra in palavra:
        letras_acertadas += letra
        if len(letras_acertadas) == 1:
            pontos += 10
        elif len(letras_acertadas) == 2:
            pontos += 5
        else:
            pontos += 1
    else:
        erros += 1
        mensagem["text"] = "Letra errada!"
        esquarteja(erros)

    palavra_atualizada_label["text"] = atualiza_palavra()
    dica_label["text"] = f"Dica: {dica}"
    pontos_label["text"] = f"Pontos: {pontos}"
    erros_label["text"] = f"Erros: {erros}"

    if atualiza_palavra() == palavra:
        letra_entry.pack_forget()
        botao_enviar_letra.pack_forget()
        mensagem["text"] = f"Parabéns! Você acertou a palavra '{palavra}' e fez {pontos} pontos."
        add_leaderboard()
        return
    if erros >= 6:
        letra_entry.pack_forget()
        botao_enviar_letra.pack_forget()
        mensagem["text"] = f"Que pena, você perdeu! A palavra era '{palavra}'."
        add_leaderboard()
        return

def frame_pack(frame, frame_atual):
    frame_atual.pack_forget()
    frame.pack()

def leaderboard():
    with open("leaderboard.txt", 'r') as arquivo:
        itens = arquivo.read()

    mensagem_leaderboard["text"] = itens
    
    frame_pack(tela_leaderboard, tela_inicial)

palavra = ""
dica = ""
palavra_oculta = ""
sortear_palavra()
erros = 0
pontos = 0
letras_acertadas = ""
nome = ""

janela = Tk()
janela.geometry("800x800")
janela.title("Jogo do Esquartejado")

tela_inicial = Frame(janela)
tela_add = Frame(janela)
tela_nome = Frame(janela)
tela_leaderboard = Frame(janela)
tela_jogo = Frame(janela)

'''

    Tela inicial

'''

botao_tela_jogo = Button(tela_inicial, text="Jogar", command=lambda:frame_pack(tela_nome, tela_inicial))
botao_tela_jogo.pack()

botao_adicionar = Button(tela_inicial, text="Adicionar novas palavras", command=lambda:frame_pack(tela_add, tela_inicial))
botao_adicionar.pack()

botao_leaderboard = Button(tela_inicial, text="Leaderboard", command=leaderboard)
botao_leaderboard.pack()

'''

    Tela de adição

'''

palavra_entry = Entry(tela_add, font=("Helvetica", 24))
palavra_entry.pack()

dica_entry = Entry(tela_add, font=("Helvetica", 24))
dica_entry.pack()

botao_enviar_palavra = Button(tela_add, text="Enviar", command=adicionar_palavra)
botao_enviar_palavra.pack()

mensagem_label_tela_add = Label(tela_add, text = "", font=("Helvetica", 14))
mensagem_label_tela_add.pack()

botao_voltar_IA = Button(tela_add, text="Voltar", command=lambda:frame_pack(tela_inicial, tela_add))
botao_voltar_IA.pack()

'''

    Tela de leaderboard

'''

mensagem_leaderboard = Label(tela_leaderboard, text = "", font=("Helvetica", 14))
mensagem_leaderboard.pack()

botao_voltar_IL = Button(tela_leaderboard, text="Voltar", command=lambda:frame_pack(tela_inicial, tela_leaderboard))
botao_voltar_IL.pack()

'''

    Tela de nome

'''

mensagem_nome = Label(tela_nome, text = "Por favor, informe o seu nome: ", font=("Helvetica", 14))
mensagem_nome.pack()

nome_entry = Entry(tela_nome, font=("Helvetica", 24))
nome_entry.pack()

botao_enviar_nome = Button(tela_nome, text="Enviar", command=jogar)
botao_enviar_nome.pack()

botao_voltar_IN = Button(tela_nome, text="Voltar", command=lambda:frame_pack(tela_inicial, tela_nome))
botao_voltar_IN.pack()

'''

    Tela do jogo

'''

dica_label = Label(tela_jogo, text = f"Dica: {dica}", font=("Helvetica", 14))
dica_label.pack()

palavra_atualizada_label = Label(tela_jogo, text = palavra_oculta, font=("Helvetica", 24))
palavra_atualizada_label.pack()

letra_entry = Entry(tela_jogo, font=("Helvetica", 24))
letra_entry.pack()

botao_enviar_letra = Button(tela_jogo, text="Enviar", command=enviar_letra)
botao_enviar_letra.pack()

mensagem = Label(tela_jogo, text="", font=("Helvetica", 14))
mensagem.pack()

pontos_label = Label(tela_jogo, text = f"Pontos: {pontos}", font=("Helvetica", 14))
pontos_label.pack()

erros_label = Label(tela_jogo, text = f"Erros: {erros}", font=("Helvetica", 14))
erros_label.pack()

canvas = Canvas(tela_jogo, width=300, height=400)
canvas.pack()
canvas.create_line(50, 350, 250, 350, width=5)
canvas.create_line(100, 350, 100, 100, width=5)
canvas.create_line(200, 350, 200, 100, width=5)
cabeca = canvas.create_oval(125, 100, 175, 150, fill="white", width=5)
tronco = canvas.create_line(150, 150, 150, 250, width=5)
braco_esq = canvas.create_line(150, 200, 100, 175, width=5)
braco_dir = canvas.create_line(150, 200, 200, 175, width=5)
perna_esq = canvas.create_line(150, 250, 100, 300, width=5)
perna_dir = canvas.create_line(150, 250, 200, 300, width=5)

botao_voltar_IJ = Button(tela_jogo, text="Voltar", command=lambda:frame_pack(tela_inicial, tela_jogo))
botao_voltar_IJ.pack()

frame_pack(tela_inicial, tela_jogo)

janela.mainloop()