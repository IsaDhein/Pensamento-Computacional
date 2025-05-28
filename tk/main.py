# import tkinter as tk

# def mostrar_opcao(botao):
#     texto = f"Escolheu: {opcao1.get()}"
#     texto += f" {opcao2.get()}"
#     texto += f" {opcao3.get()}"
#     rotulo.config(text= texto)

#     op = [opcao1.get(), opcao2.get(), opcao3.get()]
#     if op.count(True) == 3:
#         if opcao1.get() and opcao2.get():
#             if botao == "Saúde":
#                 opcao1.set(False)
#         if botao == "Tempo":
#                 opcao3.set(False)
#         if botao == "Dinheiro":
#                 opcao2.set(False)
    

        
# janela = tk.Tk()
# janela.title("Exemplo Radiobutton")
# janela.geometry("250x150")

# opcao1 = tk.BooleanVar()
# opcao2 = tk.BooleanVar()
# opcao3 = tk.BooleanVar()
# tk.Radiobutton(janela, text="Tempo", font=("Arial", 10), variable=opcao1, value="True", 
#                        command=lambda:mostrar_opcao("Tempo")).pack()
# tk.Radiobutton(janela, text="Dinheiro", font=("Arial", 10), variable=opcao2, value="True", 
#                        command=lambda:mostrar_opcao("Dinheiro")).pack()
# tk.Radiobutton(janela, text="Saúde", font=("Arial", 10), variable=opcao3, value="True", 
#                        command=lambda:mostrar_opcao("Saúde")).pack()

# rotulo = tk.Label(janela, text="Escolheu:", font=("Arial", 13))
# rotulo.pack(pady=10)
# janela.mainloop()


import tkinter as tk

janela = tk.Tk()
janela.title("Exemplo Radiobutton")
janela.geometry("250x150")
def mostrar_opcao(botao):
    print(botao)
    texto = f"Escolheu: {opcao1.get()}"
    texto += f" {opcao2.get()}"
    texto += f" {opcao3.get()}"
    rotulo.config(text= texto)

    op = [opcao1.get(), opcao2.get(), opcao3.get()]
    if op.count(True) == 3:
        if opcao1.get() and opcao2.get():
            if botao == "Saúde":
                opcao1.set(False)
            if botao == "Tempo":
                opcao3.set(False)
            if botao == "Dinhero":
                opcao2.set(False)
            rotulo.config(text= f"Escolheu: {botao} e perdeu {texto})")
    

opcao1 = tk.BooleanVar()
opcao2 = tk.BooleanVar()
opcao3 = tk.BooleanVar()

tk.Checkbutton(janela, text="Dinhero", variable=opcao1, command=lambda:mostrar_opcao("Dinhero")).pack()
tk.Checkbutton(janela, text="Tempo", variable=opcao2, command=lambda:mostrar_opcao("Tempo")).pack()
tk.Checkbutton(janela, text="Saúde", variable=opcao3, command=lambda:mostrar_opcao("Saúde")).pack()


rotulo = tk.Label(janela, text="Escolheu: A")
rotulo.pack(pady=10)
janela.mainloop()
