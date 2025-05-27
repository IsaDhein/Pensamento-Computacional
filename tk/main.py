import tkinter as tk
def imprimirInfos():
    global is_on
    is_on = not is_on
    if is_on: 
        rotulo.config(text="Olá mundo!")
    else:
        rotulo.config(text="Olá turma!")
is_on = False

janela = tk.Tk()
janela.title("Exemplo Botão")
janela.geometry("600x400")
rotulo = tk.Label(janela, text="Clique no botão abaixo" , 
                          font=("Arial", 16))
rotulo.pack(pady=10)
botao = tk.Button(janela, text="Clique aqui", command=imprimirInfos)
botao.pack(pady=10)
janela.mainloop()
