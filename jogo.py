import tkinter as tk
import random

def sortear_palavra():

    palavra_oculta = ""

    with open("palavras.txt") as arquivo:
        itens = arquivo.readlines()

    indice = random.randint(0, len(itens) - 1)
    palavra, dica = itens[indice].strip().split(",")

    palavra_oculta = "-" * len(palavra)

    return palavra, dica, palavra_oculta

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

def jogar():
    global letra
    global palavra
    global pontos
    global erros
    global letras_acertadas

    if not letra_entry.get().isalpha() or len(letra_entry.get()) != 1:
        letra_entry.delete(0, tk.END)
        mensagem["text"] = "Por favor, digite uma letra valida"
        return
    
    letra = letra_entry.get()
    mensagem["text"] = f"Letra: {letra}"
        
    letra_entry.delete(0, tk.END)

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
        mensagem["text"] = f"Parabéns! Você acertou a palavra '{palavra}' e fez {pontos} pontos."
        letra_entry.destroy()
        botao.destroy()
        return
    if erros >= 6:
        mensagem["text"] = f"Que pena, você perdeu! A palavra era '{palavra}'."
        letra_entry.destroy()
        botao.destroy()
        return

palavra, dica, palavra_oculta = sortear_palavra()
erros = 0
pontos = 0
letras_acertadas = ""

janela = tk.Tk()
janela.geometry("800x600")
janela.title("Jogo do Esquartejado")

dica_label = tk.Label(janela, text = f"Dica: {dica}", font=("Helvetica", 14))
dica_label.pack()

palavra_atualizada_label = tk.Label(janela, text = palavra_oculta, font=("Helvetica", 24))
palavra_atualizada_label.pack()

letra_entry = tk.Entry(janela, font=("Helvetica", 24))
letra_entry.pack()

botao = tk.Button(janela, text="Enviar", command=jogar)
botao.pack()

mensagem = tk.Label(janela, text="", font=("Helvetica", 14))
mensagem.pack()

pontos_label = tk.Label(janela, text = f"Pontos: {pontos}", font=("Helvetica", 14))
pontos_label.pack()

erros_label = tk.Label(janela, text = f"Erros: {erros}", font=("Helvetica", 14))
erros_label.pack()

canvas = tk.Canvas(janela, width=300, height=400)
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

janela.mainloop()