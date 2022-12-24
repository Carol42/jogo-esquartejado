import tkinter as tk
import random

def sortear_palavra():

    palavraOculta = ""

    with open("palavras.txt") as arquivo:
        itens = arquivo.readlines()

    indice = random.randint(0, len(itens) - 1)
    palavra, dica = itens[indice].strip().split(",")

    palavraOculta = "-" * len(palavra)

    return palavra, dica, palavraOculta

def atualiza_palavra():
    global letra
    global palavra
    global letras_acertadas

    palavra_oculta = ""
    for letra in palavra:
        if letra in letras_acertadas:
            palavra_oculta += letra
        else:
            palavra_oculta += "-"
    return palavra_oculta

def jogar():
    global letra
    global palavra
    global pontos
    global erros
    global letras_acertadas

    if not letra_entry.get().isalpha() or len(letra_entry.get()) != 1:
        letra_entry.delete(0, tk.END)
        print("Digite uma letra valida")
        return
    
    letra = letra_entry.get()
    print(f"Letra: {letra}")
        
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
        print("Letra errada!")

    palavra_oculta_label["text"] = atualiza_palavra()
    dica_label["text"] = f"Dica: {dica}"
    erros_label["text"] = f"Erros: {erros}"

    if atualiza_palavra() == palavra:
        print(f"Parabéns! Você acertou a palavra '{palavra}' e fez {pontos} pontos.")
        return
    if erros == 6:
        print(f"Que pena, você perdeu! A palavra era '{palavra}'.")
        return

palavra, dica, palavraOculta = sortear_palavra()
erros = 0
pontos = 0
letras_acertadas = ""

janela = tk.Tk()
janela.title("Jogo da Forca")

dica_label = tk.Label(janela, text = f"Dica: {dica}", font=("Helvetica", 14))
dica_label.pack()

palavra_oculta_label = tk.Label(janela, text = palavraOculta, font=("Helvetica", 24))
palavra_oculta_label.pack()

letra_entry = tk.Entry(janela, font=("Helvetica", 24))
letra_entry.pack()

botao = tk.Button(janela, text="Enviar", command=jogar)
botao.pack()

erros_label = tk.Label(janela, text = f"Erros: {erros}", font=("Helvetica", 14))
erros_label.pack()

# atualizar_interface(palavra, letras_acertadas, dica, erros)

janela.mainloop()