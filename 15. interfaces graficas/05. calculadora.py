import tkinter as tk


class Calc(object):
    def __init__(self, parent=tk.Tk()):
        self.parent = parent
        self.parent.title("PyCalc - Calculadora")
        self.parent.option_add("*Font", "Verdana 12 normal")
       # self.parent.iconbitmap("icones/calc_icon.ico")
        # variavel de controle, utilizada no metodo key_press
        self.decimal_point_open = False
        # variável contendo a expressão pronta para calculo
        self.math_expression = None
        # menubar
        menu_bar = tk.Menu(self.parent)
        menu_bar.add_command(label="Sobre", command=self.about)
        self.parent.config(menu=menu_bar)
        # elementos do display
        self.display_stringvar = tk.StringVar()
        display_entry_validate = (self.parent.register(
            self.only_number_entry), '%S', '%d')
        self.display = tk.Entry(self.parent, font=("Verdana", 20, "normal"), validate="key",
                                validatecommand=display_entry_validate, textvariable=self.display_stringvar)
        self.display.bind('<Return>', self.calc_expression)
        # criação do teclado numerico
        self.bt0 = tk.Button(self.parent, text="0",
                             command=lambda: self.button_press('0'))
        self.bt1 = tk.Button(self.parent, text="1",
                             command=lambda: self.button_press('1'))
        self.bt2 = tk.Button(self.parent, text="2",
                             command=lambda: self.button_press('2'))
        self.bt3 = tk.Button(self.parent, text="3",
                             command=lambda: self.button_press('3'))
        self.bt4 = tk.Button(self.parent, text="4",
                             command=lambda: self.button_press('4'))
        self.bt5 = tk.Button(self.parent, text="5",
                             command=lambda: self.button_press('5'))
        self.bt6 = tk.Button(self.parent, text="6",
                             command=lambda: self.button_press('6'))
        self.bt7 = tk.Button(self.parent, text="7",
                             command=lambda: self.button_press('7'))
        self.bt8 = tk.Button(self.parent, text="8",
                             command=lambda: self.button_press('8'))
        self.bt9 = tk.Button(self.parent, text="9",
                             command=lambda: self.button_press('9'))
        self.bt_mais = tk.Button(
            self.parent, text="+", command=lambda: self.button_press('+'))
        self.bt_menos = tk.Button(
            self.parent, text="-", command=lambda: self.button_press('-'))
        self.bt_mutiplica = tk.Button(
            self.parent, text="*", command=lambda: self.button_press('*'))
        self.bt_divide = tk.Button(
            self.parent, text="/", command=lambda: self.button_press('/'))
        self.bt_ponto = tk.Button(
            self.parent, text=".", command=lambda: self.button_press('.'))
        self.bt_igual = tk.Button(
            self.parent, text="=", command=lambda: self.button_press('='))
        self.bt_limpar = tk.Button(
            self.parent, text="Limpar", command=self.limpar)
        self.bt_sair = tk.Button(
            self.parent, text="Sair(Esc)", command=lambda: self.parent.destroy())
        self.parent.bind("<Escape>", lambda event=None: self.parent.destroy())
        self.mount_gui()
        self.parent.mainloop()

    # monta e configura os componentes gráficos
    def mount_gui(self):
        self.display.grid(row=0, column=0, columnspan=4,
                          sticky="ewns", ipady=5, padx=2, pady=2)
        self.bt0.grid(row=4, column=0, sticky="ewns", padx=2, pady=2)
        self.bt1.grid(row=3, column=0, sticky="ewns", padx=2, pady=2)
        self.bt2.grid(row=3, column=1, sticky="ewns", padx=2, pady=2)
        self.bt3.grid(row=3, column=2, sticky="ewns", padx=2, pady=2)
        self.bt4.grid(row=2, column=0, sticky="ewns", padx=2, pady=2)
        self.bt5.grid(row=2, column=1, sticky="ewns", padx=2, pady=2)
        self.bt6.grid(row=2, column=2, sticky="ewns", padx=2, pady=2)
        self.bt7.grid(row=1, column=0, sticky="ewns", padx=2, pady=2)
        self.bt8.grid(row=1, column=1, sticky="ewns", padx=2, pady=2)
        self.bt9.grid(row=1, column=2, sticky="ewns", padx=2, pady=2)
        self.bt_mais.grid(row=3, column=3, sticky="ewns", padx=2, pady=2)
        self.bt_menos.grid(row=2, column=3, sticky="ewns", padx=2, pady=2)
        self.bt_divide.grid(row=4, column=3, sticky="ewns", padx=2, pady=2)
        self.bt_mutiplica.grid(row=1, column=3, sticky="ewns", padx=2, pady=2)
        self.bt_ponto.grid(row=4, column=1, sticky="ewns", padx=2, pady=2)
        self.bt_igual.grid(row=4, column=2, sticky="ewns", padx=2, pady=2)
        self.bt_limpar.grid(row=5, column=0, columnspan=2,
                            sticky="ewns", padx=2, pady=2)
        self.bt_sair.grid(row=5, column=2, columnspan=2,
                          sticky="ewns", padx=2, pady=2)

    # limpa o display
    def limpar(self):
        self.display_stringvar.set("")
        self.decimal_point_open = False

    # tela sobre
    def about(self):
        about_window = tk.Toplevel(self.parent)
        about_window.title("PyCalc - Sobre")
        about_window.iconbitmap("icones/about_icon.ico")
        tk.Label(about_window, text="PyCalc", font=("Verdana", 15, "bold")).grid(
            row=0, column=0, padx=5, pady=5, sticky="s")
        tk.Label(about_window, text="Calculadora simples").grid(
            row=1, column=0, padx=5, pady=5, sticky="s")
        tk.Label(about_window, text="Desenvolvida em Python 3 e Tkinter").grid(
            row=2, column=0, sticky="s", padx=5)
        tk.Label(about_window, text="tdsb.contato@gmail.com").grid(row=3,
                                                                   column=0, sticky="s", padx=5)

    # validador de entrys somente expressões matemáticas válidas
    def only_number_entry(self, key_press, cod):
        valid_chars = "0123456789.+-*/"
        expression_now = self.display_stringvar.get()
        num_chars_now = len(expression_now)
        # no inicio da expressão, aceita apenas numeros
        if(num_chars_now == 0):
            valid_chars_for_init = "0123456789"
            return key_press in valid_chars_for_init
        else:
            last_char = expression_now[num_chars_now-1]
            # se o ultimo elemento inserido é um operador aceita apenas numeros ou backspace
            if(last_char in "+-*/" and key_press in "+-*/." and cod == '1'):
                return False
            # controla o uso de ponto decimal
            # evita dois operadores seguidos
            elif(last_char in "+-*/" and key_press in "+-*/." and cod == '0'):
                return True
            elif(last_char == '.' and key_press in "+-*/." and cod == '1'):
                return False
            elif(last_char == '.' and key_press in "+-*/." and cod == '0'):
                return True
            elif(self.decimal_point_open and key_press == '.'):
                return False
            elif(not self.decimal_point_open and key_press == '.'):
                self.decimal_point_open = True
                return True
            elif(last_char in "0123456789" and key_press in "+-*/"):
                self.decimal_point_open = False
                return True

    # botão da interface pressionado
    def button_press(self, bt):
        expresion_now = self.display_stringvar.get()
        char_num = len(expresion_now)
        # define caracteres validos para o inicio da expressão
        if(char_num == 0):
            valid_chars_for_init = "0123456789"
            if(bt in valid_chars_for_init):
                expresion_now += bt
                self.display_stringvar.set(expresion_now)
        else:
            # controle do uso de ponto decimal
            last_char = expresion_now[char_num - 1]
            if(bt == '.' and not last_char in "+-*/"):
                if(self.decimal_point_open):
                    print("ponto decimal indisponivel")
                else:
                    expresion_now += bt
                    self.display_stringvar.set(expresion_now)
                    self.decimal_point_open = True
            else:
                if(last_char in ".0123456789" and bt in "0123456789"):
                    expresion_now += bt
                    self.display_stringvar.set(expresion_now)
                elif(last_char in "0123456789" and not self.decimal_point_open and bt in "+-*/"):
                    expresion_now += bt
                    self.display_stringvar.set(expresion_now)
                elif(self.decimal_point_open and not last_char == '.' and bt in "+-*/"):
                    expresion_now += bt
                    self.display_stringvar.set(expresion_now)
                    self.decimal_point_open = False
                # controle do uso de operadores
                elif(last_char in "+-*/" and bt in "0123456789"):
                    expresion_now += bt
                    self.display_stringvar.set(expresion_now)
                # botão = pressionado, obter resultado
                elif(bt == '=' and last_char in "0123456789"):
                    # calcula a expressão
                    self.calc_expression()

    def prepare_expression(self):
        elementos = []
        indice = 0
        for char in self.display_stringvar.get():
            # inicializa a lista com o primeiro numero
            if(len(elementos) == 0 and char in "0123456789"):
                elementos.append(char)
            # novo operador como novo elemento da lista
            elif(len(elementos) > 0 and char in "+-*/"):
                elementos.append(char)
                indice += 1
            elif(elementos[indice] in "+-*/"):
                elementos.append(char)
                indice += 1
            else:
                elementos[indice] += char
        # salva a expressão preparada como atributo do objeto
        self.math_expression = elementos

    # efetua o calculo da expressão
    def calc_expression(self, event=None):
        self.prepare_expression()
        # multiplicação e divisão, precedencia: o que vier primeiro da esquerda para a direita
        while ("*" in self.math_expression or "/" in self.math_expression):
            indice = 0
            for element in self.math_expression:
                if (element == '*'):
                    v1 = float(self.math_expression[indice - 1])
                    v2 = float(self.math_expression[indice + 1])
                    result = str(v1 * v2)
                    self.math_expression[indice] = result
                    self.math_expression.pop(indice + 1)
                    self.math_expression.pop(indice - 1)
                    indice += 1
                    break
                elif (element == '/'):
                    v1 = float(self.math_expression[indice - 1])
                    v2 = float(self.math_expression[indice + 1])
                    result = str(v1 / v2)
                    self.math_expression[indice] = result
                    self.math_expression.pop(indice + 1)
                    self.math_expression.pop(indice - 1)
                    indice += 1
                    break
                else:
                    indice += 1
        # soma e subtração
        # repete até que sobre apenas o resultado
        while (len(self.math_expression) > 1):
            indice = 0
            for element in self.math_expression:
                if (element == '+'):
                    v1 = float(self.math_expression[indice - 1])
                    v2 = float(self.math_expression[indice + 1])
                    result = str(v1 + v2)
                    self.math_expression[indice] = result
                    self.math_expression.pop(indice + 1)
                    self.math_expression.pop(indice - 1)
                    indice += 1
                    break
                if (element == '-'):
                    v1 = float(self.math_expression[indice - 1])
                    v2 = float(self.math_expression[indice + 1])
                    result = str(v1 - v2)
                    self.math_expression[indice] = result
                    self.math_expression.pop(indice + 1)
                    self.math_expression.pop(indice - 1)
                    indice += 1
                    break
                else:
                    indice += 1
        final_result = str(round(float(self.math_expression[0]), 1))
        # insere o resultado no display
        self.display_stringvar.set(final_result)


if (__name__ == "__main__"):
    calc = Calc()
