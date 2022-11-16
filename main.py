import Menu_opcoes
from crud import *

values = {"Procurar Valor": "1",
          "Adicionar valor": "2",
          "Remover valor": "3"}

class Selecao:
    def __init__(self, container):
        self.frame_cima = Frame(container)
        self.frame_baixo = Frame(container)

        self.selecao_valor = StringVar()

        self.label = Label(self.frame_cima, text='O que deseja fazer?', font='Verdana')
        for (text, value) in values.items():
            Radiobutton(self.frame_baixo, text=text, variable=self.selecao_valor,
                        value=value).pack(anchor='w')

        self.label.pack(anchor='w', pady=30)

        self.botao = Button(self.frame_baixo, text='ok', command=self.exibe, padx=20, bg='#51cb59')
        self.botao_sair = Button(self.frame_baixo, text='Sair', command=container.quit, padx=20, bg='#cb5153')

        self.botao.pack(side='left', padx=20)
        self.botao_sair.pack(side='left', pady=20)

        self.frame_cima.pack()
        self.frame_baixo.pack()

    def exibe(self):
        opcao_menu = self.selecao_valor.get()
        print(opcao_menu)
        janela_buscar = Tk()
        Menu_opcoes.Busca(opcao_menu, janela_buscar)
        janela_buscar.title("PROCURAR VALOR")
        janela_buscar.geometry("400x300")
        centro(janela_buscar)
        janela_buscar.mainloop()

def centro(raiz):
    raiz.update_idletasks()

    largura = raiz.winfo_width()
    frame_largura = raiz.winfo_rootx() - raiz.winfo_x()
    largura_tela = largura + 2 * frame_largura

    altura = raiz.winfo_height()
    titulo_height = raiz.winfo_rooty() - raiz.winfo_y()
    altura_tela = altura + titulo_height + frame_largura

    pos_x = (raiz.winfo_screenwidth() // 2) - (largura_tela // 2)
    pos_y = (raiz.winfo_screenheight() // 2) - (altura_tela // 2)

    raiz.geometry('{}x{}+{}+{}'.format(largura, altura, pos_x, pos_y))
    raiz.deiconify()


raiz = Tk()
Selecao(raiz)
raiz.title("MENU INICIAL")
raiz.geometry("300x300")
raiz.resizable()
centro(raiz)

raiz.mainloop()
