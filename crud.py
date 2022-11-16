from tkinter import *
from tkinter import messagebox
import pandas as pd

plan = pd.read_excel('25 - Projetos de pesquisa sem financiamento 2022.xlsx')

class Janela:
    def __init__(self, opc, opcao_menu, container):
        print(opcao_menu)
        print(opc)
        self.opc = opc
        self.opcao_menu = opcao_menu
        self.frame1 = Frame(container)
        self.frame1["pady"] = 20
        self.frame1.pack()
        self.frame2 = Frame(container)
        self.frame2.pack()
        self.frame3 = Frame(container)
        self.frame3["pady"] = 20
        self.frame3.pack()
        self.frame4 = Frame(container)
        self.frame4.pack()

        if opcao_menu == "1":
            self.titulo = Label(self.frame1, text="Dados para buscar na planilha")
            self.dadoLabel = Label(self.frame2, text="Dado: ")
            self.dadoLabel.pack(side=LEFT)
            self.dado = Entry(self.frame2)
            self.dado.pack(side=LEFT)
            self.dado["width"] = 30
            self.bt1 = Button(self.frame4, text="ok", command=self.clicar, padx=20, pady=5)

        elif opcao_menu == "2":
            self.titulo = Label(self.frame1, text="Dados para adicionar na planilha")
            if self.opc == "1":
                self.dadoLabel = Label(self.frame2, text="Aqui voce adicionará um NOVO\n laboratorio com" +
                 "TODAS as informacoes\n portanto, cique em ok para continuar")
            elif self.opc == "2":
                self.dadoLabel = Label(self.frame2, text="Nome da COLUNA que deseja adicionar")
                self.dado = Entry(self.frame3)
                self.dado.pack(side=LEFT)
                self.dado["width"] = 30
            self.dadoLabel.pack(side=LEFT)
            self.bt1 = Button(self.frame4, text="ok", command=self.clicar, padx=20, pady=5)

        elif opcao_menu == "3":
            self.titulo = Label(self.frame1, text="Dados para remover na planilha")
            if self.opc == "1":
                self.dadoLabel = Label(self.frame2, text="Insira o numero da LINHA que\n deseja remover pelo terminal.")
            elif self.opc == "2":
                self.dadoLabel = Label(self.frame2, text="Nome da COLUNA que deseja remover")
                self.dado = Entry(self.frame3)
                self.dado.pack(side=LEFT)
                self.dado["width"] = 30
            self.dadoLabel.pack(side=LEFT)
            self.dadoLabel.pack(side=LEFT)
            self.bt1 = Button(self.frame4, text="ok", command=self.clicar, padx=20, pady=5)

        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()
        self.bt1.pack()

    def clicar(self):
        opcao = self.opc
        if self.opcao_menu == "1":
            get_dado = self.dado.get()
            plan_buscar(opcao, get_dado)
        elif self.opcao_menu == "2":
            if opcao == "2":
                get_dado = self.dado.get()
                plan_adicionar(opcao, get_dado)
        elif self.opcao_menu == "3":
            if opcao=="1":
                get_dado = 0
                plan_remover(opcao, get_dado)
            else:
                get_dado = self.dado.get()
                plan_remover(opcao, get_dado)

    def exibe(self, titulo, texto):
        messagebox.showinfo(titulo, texto)


def plan_buscar(opcao, get_dado, self=None):
    if opcao == "1":
        for i, j in enumerate(plan['Cod_laboratorio']):
            if j == get_dado:
                texto = (plan['Nome_do_laboratorio'][i])
                print(texto)
        titulo = 'VERIFIQUE NA SUA PLANILHA'
        Janela.exibe(self,titulo, texto)
    elif opcao == "2":
        for i, j in enumerate(plan['Centro_de_lotacao']):
            if j == get_dado:
                texto = (plan['Nome_do_laboratorio'][i])
                print(texto)
        titulo = 'VERIFIQUE NA SUA PLANILHA'
        Janela.exibe(self,titulo, texto)
    elif opcao == "3":
        for i, j in enumerate(plan['Sigla']):
            if j == get_dado:
                texto = (plan['Localizacao_fisica'][i])
                print(texto)
        titulo = 'VERIFIQUE NA SUA PLANILHA'
        Janela.exibe(self,titulo, texto)
    elif opcao == "4":
        for i, j in enumerate(plan['Coordenador']):
            if j == get_dado:
                texto = (plan['Nome_do_laboratorio'][i])
                print(texto)
        titulo = 'VERIFIQUE NA SUA PLANILHA'
        Janela.exibe(self,titulo, texto)
    elif opcao == "5": 
        centro_formacao = (plan.loc[plan['Centro_de_lotacao']==get_dado])
        print(centro_formacao['Nome_do_laboratorio'])

def plan_adicionar(opcao, get_dado, self=None):
    titulo = 'INFORMACAO RECEBIDA!'
    texto = 'por favor, insira as demais informacoes pelo terminal.'
    Janela.exibe(self, titulo, texto)
    if opcao == "1":
        add = 1
        while add == 1:
            linha = len(plan)
            for i in plan:
                outras_info = input(f'{i}: ')
                plan.loc[linha+1, i] = outras_info
                plan.to_excel('25 - Projetos de pesquisa sem financiamento 2022.xlsx', index=False)
            print("concluido, verifique planilha")
            add = int(input("Deseja adicionar novamente? digite 1 pra sim e 0 para nao"))
        print("encerrado.")
    elif opcao == "2":
        add = 1
        while add == 1:
            num_lab = int(input("Quantos laboratorios voce deseja inserir algo (Serao listados de acordo com a planilha): "))
            for i in range(0, num_lab):
                j = plan.loc[i, 'Cod_laboratorio']
                k = int(input(f'Insira o dado para {j}: '))
                plan.loc[i, get_dado] = k
                plan.to_excel('25 - Projetos de pesquisa sem financiamento 2022.xlsx', index=False)
            print("concluido, verifique planilha")
            add = int(input("Deseja adicionar novamente? digite 1 pra sim e 0 para nao"))
        print("encerrado.")


def plan_remover(opcao, get_dado, self=None):
    if opcao == "1":
        get_dado_remov = int(input("Insira o numero da linha: "))
        plan.drop(get_dado_remov)
    elif opcao =="2":
        del plan[get_dado]
    plan.to_excel('25 - Projetos de pesquisa sem financiamento 2022.xlsx', index=False)
    Janela.exibe(self,"VERIFIQUE SUA PLANILHA", "REMOVIDO COM SUCESSO")
