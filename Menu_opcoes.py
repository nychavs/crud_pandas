from tkinter import *

import crud

valuesBusca = {"Buscar nome do lab pelo Codigo": "1",
               "Buscar descrição do lab pelo Centro de Lotação": "2",
               "Buscar localização a partir da Sigla": "3",
               "Buscar o lab de um coordenador especifico": "4",
               "Buscar laboratorios que estao no mesmo centro": "5"}

valuesAdd = {"Adicionar linhas (um laboratorio e todas suas info)": "1",
             "Adicionar colunas (informacao especifica)": "2"}

valuesRemove = {"Remover linhas (um laboratorio e todas suas info)": "1",
                "Remover colunas (informacao especifica)": "2"}


class Busca:
    def __init__(self, opcao_menu, container):
        self.opcao_menu = opcao_menu
        self.frame_cima = Frame(container)
        self.frame_baixo = Frame(container)

        self.selecao = StringVar(self.frame_cima)

        self.label = Label(self.frame_cima, text='O que deseja?', font='Verdana')
        if self.opcao_menu == "1":
            for (text, valor) in valuesBusca.items():
                Radiobutton(self.frame_baixo, text=text, variable=self.selecao,
                            value=valor).pack(anchor='w')
        elif self.opcao_menu == "2":
            for (text, valor) in valuesAdd.items():
                Radiobutton(self.frame_baixo, text=text, variable=self.selecao,
                            value=valor).pack(anchor='w')
        elif self.opcao_menu == "3":
            for (text, valor) in valuesRemove.items():
                Radiobutton(self.frame_baixo, text=text, variable=self.selecao,
                            value=valor).pack(anchor='w')

        self.label.pack(anchor='w', pady=30)

        self.botao3 = Button(self.frame_baixo, text='Ok', command=self.exibe, padx=20, bg='#51cb59')
        self.botao_sairrr = Button(self.frame_baixo, text='Sair', command=container.quit, padx=20, bg='#cb5153')

        self.botao3.pack(side='left', padx=20)
        self.botao_sairrr.pack(side='left', pady=20)

        self.frame_cima.pack()
        self.frame_baixo.pack()

    def exibe(self):
        opc = self.selecao.get()
        janela_principal = Tk()
        crud.Janela(opc, self.opcao_menu, janela_principal)
        janela_principal.title("MENU DECISAO")
        janela_principal.geometry("300x300")
        janela_principal.mainloop()


