from random import randint
#Desafio diário 01 (26/10/2023 - terminado em 12 minutos)
"""print("Bem-vindo(a) ao testador de conhecimentos CB VILANIA")
print("----------------------------------------------------")
print("+++++Apenas números inteiros+++++")

try:
    n = int(input("Quantos números você gostaria de inserir? "))
except ValueError:
    print("Entrada inválida. Insira um número inteiro.")
    exit()

acumulo = []
for i in range(n):
    try:
        valor = int(input(f"Qual o {i+1}º valor a ser inserido? "))
        acumulo.append(valor)
    except ValueError:
        print("Entrada inválida. Insira um número inteiro.")

if not acumulo:
    print("Nenhum número válido foi inserido. Encerrando o programa.")
else:
    media = sum(acumulo) / n
    maiorNota = max(acumulo)
    menorNota = min(acumulo)
    faixa = maiorNota - menorNota

    print("\nAqui estão as estatísticas das notas inseridas:")
    print(f"Média: {media:.2f}")
    print(f"Maior nota: {maiorNota}")
    print(f"Menor nota: {menorNota}")
    print(f"Faixa de notas: {faixa}")
    print(f"Quantidade total de notas: {n}")
"""

#Desafio diário 02(27/10/2023 - terminado em 9 minutos)
"""print("____Calculaora de fatoriais____")
def calcular_fatorial(numero):
    if numero < 0:
        return "O fatorial de um número negativo não é definido."
    elif numero == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, numero + 1):
            resultado *= i
        return resultado

numero = int(input("Digite um número inteiro não negativo para calcular o fatorial: "))
fatorial = calcular_fatorial(numero)

print(f"{numero}! = {fatorial}")
"""

#Desafio diário 03(28/10/2023 - terminado em 4 minutos)
"""print("Número mágico, vou pensar em um número mágico de 0 a 100 e veremos em quantas tentativas você acertará")
pc = randint(0,100)
guess = -1
tentativas = 1
while not pc == guess:
    
    guess = int(input("Qual o seu chute?"))
    if guess > pc:
        print(f"O número que estou pensando é menor que {guess}")
    
    if guess < pc:
        print(f"O número que estou pensando é maior que {guess}")

    tentativas += 1

print(f"Parabéns, você acertou em {tentativas} tentativas")"""

#Desafio diário 04(29 /10/2023 - terminado em 19 minutos)
"""import random
import string

print("Bem-vindo ao Gerador de Senhas!")

comprimento = int(input("Digite o comprimento da senha desejada: "))

usar_maiusculas = input("Deseja incluir letras maiúsculas? (Sim ou Não): ").strip().lower() == "sim"
usar_minusculas = input("Deseja incluir letras minúsculas? (Sim ou Não): ").strip().lower() == "sim"
usar_numeros = input("Deseja incluir números? (Sim ou Não): ").strip().lower() == "sim"
usar_especiais = input("Deseja incluir caracteres especiais? (Sim ou Não): ").strip().lower() == "sim"

caracteres = ""

if usar_maiusculas:
    caracteres += string.ascii_uppercase
if usar_minusculas:
    caracteres += string.ascii_lowercase
if usar_numeros:
    caracteres += string.digits
if usar_especiais:
    caracteres += string.punctuation

if not (usar_maiusculas or usar_minusculas or usar_numeros or usar_especiais):
    print("Você precisa escolher pelo menos um tipo de caractere para criar a senha.")
else:
    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    print("A senha gerada é:", senha)
"""

#Desafio diário 05(30/10/2023 - terminado em 28 minutos)

"""import tkinter as tk

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Jogo da Velha")
        self.current_player = "X"
        self.board = [["", "", ""], ["", "", ""], ["", "", ""]]
        self.buttons = []
        for row in range(3):
            button_row = []
            for col in range(3):
                button = tk.Button(self.master, text="", font=("Helvetica", 20), width=5, height=2, command=lambda row=row, col=col: self.button_click(row, col))
                button.grid(row=row, column=col)
                button_row.append(button)
            self.buttons.append(button_row)

    def button_click(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.check_win():
                self.highlight_winner()
                tk.messagebox.showinfo("Jogo da Velha", f"O jogador {self.current_player} ganhou!")
                self.reset()
            elif self.check_tie():
                self.highlight_tie()
                tk.messagebox.showinfo("Jogo da Velha", "Empate!")
                self.reset()
            else:
                if self.current_player == "X":
                    self.current_player = "O"
                else:
                    self.current_player = "X"

    def check_win(self):
        for i in range(3):
            if (self.board[i][0] == self.board[i][1] == self.board[i][2] != "") or \
               (self.board[0][i] == self.board[1][i] == self.board[2][i] != ""):
                return True
        if (self.board[0][0] == self.board[1][1] == self.board[2][2] != "") or \
           (self.board[0][2] == self.board[1][1] == self.board[2][0] != ""):
            return True
        return False

    def check_tie(self):
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == "":
                    return False
        return True

    def reset(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text="", bg="SystemButtonFace")  # Reset background color
                self.board[row][col] = ""
        self.current_player = "X"

    def highlight_winner(self):
        for i in range(3):
            if (self.board[i][0] == self.board[i][1] == self.board[i][2] != ""):
                for col in range(3):
                    self.buttons[i][col].config(bg="green")
            if (self.board[0][i] == self.board[1][i] == self.board[2][i] != ""):
                for row in range(3):
                    self.buttons[row][i].config(bg="green")
        if (self.board[0][0] == self.board[1][1] == self.board[2][2] != ""):
            for i in range(3):
                self.buttons[i][i].config(bg="green")
        if (self.board[0][2] == self.board[1][1] == self.board[2][0] != ""):
            for i in range(3):
                self.buttons[i][2 - i].config(bg="green")

    def highlight_tie(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(bg="red")

root = tk.Tk()
game = TicTacToe(root)
root.mainloop()
"""

#Desafio diário 06(31/10/2023 - terminado em 7 minutos)
"""print("Calculadora de IMC")
peso = float(input("Qual o peso analisado?"))
altura = float(input("Qual a altura analisada? (em m)"))
imc = peso / (altura ** 2)
if imc < 18.5:
    print(f"Abaixo do peso, imc: {imc}")
elif 18.5 < imc <= 24.9:
    print(f"Peso normal, imc: {imc}")
elif 25 <= imc <= 29.9:
    print(f"Sobrepeso, imc: {imc}")
elif 30 <= imc <= 34.9:
    print(f"Obesidade grau I, imc: {imc}")
elif 35 <= imc <= 39.9:
    print(f"Obesidade grau II, imc: {imc}")
elif imc >= 40:
    print(f"Obesidade grau III, imc: {imc}")
"""
#Desafio diário 07(01/11/2023 - terminado em 4 minutos)
"""print("Multiplicadora simples")
a = int(input("Qual o primeiro número? "))
b = int(input("Por quanto ele será multiplicado?"))
print(f"O resultado da multiplicação realizada é: {a*b}")"""

#Desafio diário 08(02/11/2023 - terminado 3 em minutos)
"""print("Verificar par")
a = int(input("Insira o número a ser analisado: "))
if a%2 == 0:
    print(f"O número inserido ({a}) é par")
else:
    print(f"O número inserido ({a}) é impar")"""

#Desafio diário 09(03/11/2023 - terminado em 2 minutos)
"""print("Verificar impar")
a = int(input("Insira o número a ser analisado: "))
if a%2 == 0:
    print(f"O número inserido ({a}) é par")
else:
    print(f"O número inserido ({a}) é impar")"""

#Desafio diário 10(04/11/2023 - terminado em 8 minutos)
"""print("Vamos jogar dados, quem tirar o maior número vence!")
while True:
    print("1  -  Jogar Dados ||||| 2  -  Abandonar o jogo")
    a = input()

    if a == '2':
        break
    elif a == '1':
        pessoa = randint(1, 6)
        pc = randint(1, 6)

        if pessoa > pc:
            print(f"Que droga, você venceu! Eu tirei {pc} e você {pessoa}")
        elif pc > pessoa:
            print(f"Que bom, eu venci! Eu tirei {pc} e você {pessoa}")
        else:
            print(f"Que curioso, empatamos! Eu tirei {pc} e você {pessoa}")
    else:
        print("Opção inválida. Escolha 1 para jogar dados ou 2 para abandonar o jogo.")
"""

#Desafio diário 11(05/11/2023 - terminado em 19 minutos)
"""def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius

def celsius_to_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    fahrenheit = celsius_to_fahrenheit(celsius)
    return fahrenheit

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    kelvin = celsius_to_kelvin(celsius)
    return kelvin

# Exemplos de uso
kelvin = 300.0
celsius = kelvin_to_celsius(kelvin)
fahrenheit = kelvin_to_fahrenheit(kelvin)

print(f"{kelvin} Kelvin é igual a {celsius} Celsius")
print(f"{kelvin} Kelvin é igual a {fahrenheit} Fahrenheit")
"""

#Desafio diário 12(06/11/2023 - terminado em 30 minutos)
"""import tkinter as tk
from tkinter import messagebox
import time

# Configuração do tempo Pomodoro (25 minutos)
pomodoro_time = 25 * 60
# Configuração do tempo de pausa curta (5 minutos)
short_break_time = 5 * 60
# Configuração do tempo de pausa longa (15 minutos)
long_break_time = 15 * 60

class PomodoroTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Cronômetro Pomodoro")

        self.time_remaining = pomodoro_time
        self.running = False
        self.update_interval = 1000  # Atualizar a cada segundo (1000 ms)

        self.label = tk.Label(root, text="", font=("Helvetica", 48))
        self.label.pack(pady=10)

        self.start_button = tk.Button(root, text="Iniciar Pomodoro", command=self.start_timer)
        self.start_button.pack()
        self.stop_button = tk.Button(root, text="Parar", command=self.stop_timer, state=tk.DISABLED)
        self.stop_button.pack()
        self.reset_button = tk.Button(root, text="Reiniciar", command=self.reset_timer, state=tk.DISABLED)
        self.reset_button.pack()

    def update_display(self):
        minutes, seconds = divmod(self.time_remaining, 60)
        self.label.config(text=f"{minutes:02d}:{seconds:02d}")

    def start_timer(self):
        if not self.running:
            self.running = True
            self.update_timer()

            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
            self.reset_button.config(state=tk.NORMAL)

    def stop_timer(self):
        if self.running:
            self.running = False
            self.root.after_cancel(self.timer_id)

            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)

    def reset_timer(self):
        self.stop_timer()
        self.time_remaining = pomodoro_time
        self.update_display()

    def update_timer(self):
        if self.time_remaining > 0:
            self.update_display()
            self.time_remaining -= 1
            self.timer_id = self.root.after(self.update_interval, self.update_timer)
        else:
            self.complete_pomodoro()

    def complete_pomodoro(self):
        self.stop_timer()
        self.show_message("Pomodoro Concluído!", "É hora de fazer uma pausa curta.")
        self.reset_timer()

    def show_message(self, title, message):
        messagebox.showinfo(title, message)

if __name__ == "__main__":
    root = tk.Tk()
    app = PomodoroTimer(root)
    root.mainloop()
"""