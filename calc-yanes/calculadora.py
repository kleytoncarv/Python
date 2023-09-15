import tkinter as tk

def calcular():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operacao = operacao_var.get()

        if operacao == "Soma":
            resultado.set(num1 + num2)
        elif operacao == "Subtração":
            resultado.set(num1 - num2)
        elif operacao == "Multiplicação":
            resultado.set(num1 * num2)
        elif operacao == "Divisão":
            if num2 == 0:
                resultado.set("Erro: Divisão por zero")
            else:
                resultado.set(num1 / num2)
    except ValueError:
        resultado.set("Erro: Entrada inválida")

# Cria a janela principal
janela = tk.Tk()
janela.title("Calculadora")

# Criação de widgets
entry_num1 = tk.Entry(janela)
entry_num2 = tk.Entry(janela)
operacao_var = tk.StringVar()
operacao_var.set("Soma")
operacao_menu = tk.OptionMenu(janela, operacao_var, "Soma", "Subtração", "Multiplicação", "Divisão")
resultado = tk.StringVar()

# Botão para calcular
calcular_button = tk.Button(janela, text="Calcular", command=calcular)

# Exibição do resultado
resultado_label = tk.Label(janela, textvariable=resultado)

# Layout dos widgets
entry_num1.grid(row=0, column=0)
entry_num2.grid(row=0, column=1)
operacao_menu.grid(row=0, column=2)
calcular_button.grid(row=1, column=0, columnspan=3)
resultado_label.grid(row=2, column=0, columnspan=3)

# Loop principal
janela.mainloop()
