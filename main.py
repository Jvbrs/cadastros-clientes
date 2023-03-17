from tkinter import*
from tkinter import messagebox
from tkinter import Tk, StringVar, ttk
from PIL import Image, ImageTk
from tkcalendar import Calendar, DateEntry
from datetime import date
from view import *





janela = Tk()
janela.title('')
janela.geometry('1200x600')
janela.configure(background="gray")
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use('clam')

#criando frames

frameCima = Frame(janela, width=1200, height=50, bg="#feffff", relief=FLAT)
frameCima.grid(row=0, column=0)

frameMeio = Frame(janela, width= 1043, height=303, bg="#feffff", pady=20, relief=FLAT)
frameMeio.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frameBaixo = Frame(janela, width= 1043, height=300, bg="#feffff", pady=20, relief=FLAT)
frameBaixo.grid(row=2, column=0, pady=1, padx=0, sticky=NSEW)
#conectando funçoes
 
global tree

def inserir():
    

    nome=e_nome.get()
    idade=e_idade.get()
    turno=e_turno.get()
    endereco=e_endereco.get()
    dataE=e_cale.get()
    dataS=e_cals.get()
    dataPag=e_calpag.get()
    cont=e_contato.get()
    obs=e_pesquisar.get()

    lista_cadastrar = [nome, idade, turno, endereco, dataE, dataS, dataPag, cont, obs]

    for i in lista_cadastrar:
        if i =='':
            messagebox.showerror('Erro', 'Preencha todos os campos')
            return
        
    inserir_cadastro(lista_cadastrar)
    messagebox.showinfo('Sucesso', 'sucesso')
    
    e_nome.delete(0,'end')
    e_idade.delete(0,'end')
    e_turno.delete(0,'end')
    e_endereco.delete(0,'end')
    e_cale.delete(0,'end')
    e_cals.delete(0,'end')
    e_calpag.delete(0,'end')
    e_contato.delete(0,'end')
    e_pesquisar.delete(0,'end')  

    mostrar()


def atualizar():
    try:
        treev_clientes = tree.focus()
        treev_dicionario = tree.item(treev_clientes)
        treev_lista = treev_dicionario['values']

        valor =treev_lista[0]

        e_nome.delete(0,'end')
        e_idade.delete(0,'end')
        e_turno.delete(0,'end')
        e_endereco.delete(0,'end')
        e_cale.delete(0,'end')
        e_cals.delete(0,'end')
        e_calpag.delete(0,'end')
        e_contato.delete(0,'end')
        e_pesquisar.delete(0,'end')

        id=int(treev_lista[0])
        e_nome.insert(0,treev_lista[1])
        e_idade.insert(0,treev_lista[2])
        e_turno.insert(0,treev_lista[3])
        e_endereco.insert(0,treev_lista[4])
        e_cale.insert(0,treev_lista[5])
        e_cals.insert(0,treev_lista[6])
        e_calpag.insert(0,treev_lista[7])
        e_contato.insert(0,treev_lista[8])
        e_pesquisar.insert(0,treev_lista[9])

        def update():
            nome=e_nome.get()
            idade=e_idade.get()
            turno=e_turno.get()
            endereco=e_endereco.get()
            dataE=e_cale.get()
            dataS=e_cals.get()
            dataPag=e_calpag.get()
            cont=e_contato.get()
            obs=e_pesquisar.get()
            
            lista_atualizar = [nome, idade, turno, endereco, dataE, dataS, dataPag, cont, obs, id]
    
            for i in lista_atualizar:
                if i=='':
                    messagebox.showerror('Erro', 'Preencha todos os campos')
                    return
                
            atualizar_dados(lista_atualizar)
            messagebox.showinfo('Sucesso', 'Sucesso')

            e_nome.delete(0,'end')
            e_idade.delete(0,'end')
            e_turno.delete(0,'end')
            e_endereco.delete(0,'end')
            e_cale.delete(0,'end')
            e_cals.delete(0,'end')
            e_calpag.delete(0,'end')
            e_contato.delete(0,'end')
            e_pesquisar.delete(0,'end')

            b_comfirm.destroy()

            mostrar()
            
        b_comfirm = Button(frameMeio,command=update,  width=13, text='Confirmar'.upper(), overrelief=RIDGE, font=('Ivy 8 bold'), bg="#feffff", fg="#2e2d2b")
        b_comfirm.place(x=330, y=185)





    except IndexError:
        messagebox.showerror('Erro', 'Seleciona um dos dados na tebela')
#função delete
def deletar():
    try:
        treev_clientes = tree.focus()
        treev_dicionario = tree.item(treev_clientes)
        treev_lista = treev_dicionario['values']

        valor =treev_lista[0]

        deletar_dados([valor])

        messagebox.showinfo('Sucesso', 'Sucesso')

        mostrar()

    except IndexError:
        messagebox.showerror('Erro', 'Seleciona um dos dados na tebela')


# função ver item
def ver_cliente1(): 
    treev_clientes = tree.focus()
    treev_dicionario = tree.item(treev_clientes)
    treev_lista = treev_dicionario['values']

    valor = [int(treev_lista[0])] 

    cliente = ver_cliente(valor)

    
    vdados = cliente[0][1]
    l_vdados = Label(frameMeio, text='Nome: '+vdados, height=1, anchor=NW, font=('Ivy 10 bold'), bg="#feffff", fg="#403d3d")
    l_vdados.place(x=700, y=10)
        
    vdados = cliente[0][2]
    l_vdados = Label(frameMeio, text='idade: '+str(vdados), height=1, anchor=NW, font=('Ivy 10 bold'), bg="#feffff", fg="#403d3d")
    l_vdados.place(x=850, y=10)

    vdados = cliente[0][3]
    l_vdados = Label(frameMeio, text='Turno: '+vdados, height=1, anchor=NW, font=('Ivy 10 bold'), bg="#feffff", fg="#403d3d")
    l_vdados.place(x=700, y=40)
        
    vdados = cliente[0][4]
    l_vdados = Label(frameMeio, text='Endereço: '+vdados, height=1, anchor=NW, font=('Ivy 10 bold'), bg="#feffff", fg="#403d3d")
    l_vdados.place(x=850, y=40)
        
    vdados = cliente[0][5]
    l_vdados = Label(frameMeio, text='Entrada: '+vdados, height=1, anchor=NW, font=('Ivy 10 bold'), bg="#feffff", fg="#403d3d")
    l_vdados.place(x=700, y=70)

    vdados = cliente[0][6]
    l_vdados = Label(frameMeio, text='Saida: '+vdados, height=1, anchor=NW, font=('Ivy 10 bold'), bg="#feffff", fg="#403d3d")
    l_vdados.place(x=850, y=70)
        
    vdados = cliente[0][7]
    l_vdados = Label(frameMeio, text='Ultimo Pagamento: '+vdados, height=1, anchor=NW, font=('Ivy 10 bold'), bg="#feffff", fg="#403d3d")
    l_vdados.place(x=700, y=100)
        
    vdados = cliente[0][8]
    l_vdados = Label(frameMeio, text='Contato: '+vdados, height=1, anchor=NW, font=('Ivy 10 bold'), bg="#feffff", fg="#403d3d")
    l_vdados.place(x=700, y=130)

    vdados = cliente[0][8]
    l_vdados = Label(frameMeio, text='Observações: '+vdados, height=1, anchor=NW, font=('Ivy 10 bold'), bg="#feffff", fg="#403d3d")
    l_vdados.place(x=700, y=160)
    

    

#logo
app_img = Image.open('iconprincipal.png.png')
app_img = app_img.resize((45,45))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, text='Clientes Arvore da vida', width=900, compound=LEFT, relief=RAISED, anchor=NW, font=('Verdana 20 bold'), bg= "#feffff", fg="#403d3d")
app_logo.place(x=0, y=0)

#frame meio
l_nome = Label(frameMeio, text='Nome', height=1, anchor=NW, font=('Ivy 10 bold'), bg="#feffff", fg="#403d3d")
l_nome.place(x=10, y=10)
e_nome = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_nome.place(x=130, y=11)

l_idade = Label(frameMeio, text='Idade', height=1, anchor=NW, font=('Ivy 10 bold'), bg="#feffff", fg="#403d3d")
l_idade.place(x=10, y=40)
e_idade = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_idade.place(x=130, y=41)

l_turno = Label(frameMeio, text='Turno', height=1, anchor=NW, font=('Ivy 10 bold'), bg="#feffff", fg="#403d3d")
l_turno.place(x=10, y=70)
e_turno = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_turno.place(x=130, y=71)


l_endereco = Label(frameMeio, text='Endereço', height=1, anchor=NW, font=('Ivy 10 bold'), bg="#feffff", fg="#403d3d")
l_endereco.place(x=10, y=100)
e_endereco = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_endereco.place(x=130, y=101)

l_cale = Label(frameMeio, text='Data de entrada', height=1, anchor=NW, font=('Ivy 10 bold'), bg="#feffff", fg="#403d3d")
l_cale.place(x=10, y=130)
e_cale = DateEntry(frameMeio, width=12,Background='darkblue', bordewidth= 2, year=2023)
e_cale.place(x=130, y=131)

l_cals = Label(frameMeio, text='Data de saida', height=1, anchor=NW, font=('Ivy 10 bold'), bg="#feffff", fg="#403d3d")
l_cals.place(x=10, y=160)
e_cals = DateEntry(frameMeio, width=12,Background='darkblue', bordewidth= 2, year=2023)
e_cals.place(x=130, y=161)

l_calpag = Label(frameMeio, text='Ultimo pagamento', height=1, anchor=NW, font=('Ivy 10 bold'), bg="#feffff", fg="#403d3d")
l_calpag.place(x=10, y=190)
e_calpag = DateEntry(frameMeio, width=12,Background='darkblue', bordewidth= 2, year=2023)
e_calpag.place(x=130, y=191)

l_contato = Label(frameMeio, text='Contato', height=1, anchor=NW, font=('Ivy 10 bold'), bg="#feffff", fg="#403d3d")
l_contato.place(x=10, y=220)
e_contato = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_contato.place(x=130, y=221)

l_pesquisar = Label(frameMeio, text='Observação', height=1, anchor=NW, font=('Ivy 10 bold'), bg="#feffff", fg="#403d3d")
l_pesquisar.place(x=10, y=250)
e_pesquisar = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_pesquisar.place(x=130, y=251)

#cirando buttom
app_add = Image.open('cadastrar.png')
app_add = app_add.resize((20,20))
app_add = ImageTk.PhotoImage(app_add)

b_cadastrar = Button(frameMeio, command=inserir, image=app_add, width=95, text='  Cadastrar'.upper(), compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivy 8'), bg="#feffff", fg="#2e2d2b")
b_cadastrar.place(x=330, y=10)

app_atualizar = Image.open('update.png')
app_atualizar = app_atualizar.resize((20,20))
app_atualizar = ImageTk.PhotoImage(app_atualizar)

b_atulizar = Button(frameMeio,command=atualizar, image=app_atualizar, width=95, text='  Atulizar'.upper(), compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivy 8'), bg="#feffff", fg="#2e2d2b")
b_atulizar.place(x=330, y=50)

app_delete = Image.open('delete.png')
app_delete = app_delete.resize((20,20))
app_delete = ImageTk.PhotoImage(app_delete)

b_delete = Button(frameMeio,command=deletar, image=app_delete, width=95, text='  delete'.upper(), compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivy 8'), bg="#feffff", fg="#2e2d2b")
b_delete.place(x=330, y=90)

app_cliente = Image.open('cliente.png')
app_cliente = app_cliente.resize((20,20))
app_cliente = ImageTk.PhotoImage(app_cliente)

b_cliente = Button(frameMeio, command=ver_cliente1, image=app_cliente, width=95, text='  cliente'.upper(), compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivy 8'), bg="#feffff", fg="#2e2d2b")
b_cliente.place(x=330, y=251)

l_quantidade = Label(frameMeio, text='',pady=5, width=14, height=2, anchor=CENTER, font=('Ivy 17 bold'), bg="#4fa882", fg="#403d3d")
l_quantidade.place(x=450, y=17)

l_quantidade_ = Label(frameMeio, text=' Quantidade Total de Clientes. ',  height=1, anchor=NW, font=('Ivy 10 bold'), bg="#4fa882", fg="#403d3d")
l_quantidade_.place(x=450, y=12)

def mostrar():
    global tree


    tabela_head = ['#Numero','Nome',  'Idade','Turno','Endereço', 'Data de entrada', 'Data de saida', 'Ultimo pagamento', 'Contato responsavel', 'Observações']

    lista_itens = ver_dados()



    tree = ttk.Treeview(frameBaixo, selectmode="extended",columns=tabela_head, show="headings")

    # vertical scrollbar
    vsb = ttk.Scrollbar(frameBaixo, orient="vertical", command=tree.yview)

    # horizontal scrollbar
    hsb = ttk.Scrollbar(frameBaixo, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')
    frameBaixo.grid_rowconfigure(0, weight=12)

    hd=["center","center","center","center","center","center","center","center","center","center"]
    h=[80,100,40,80,160,110,110,120,130,180]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # adjust the column's width to the header string
        tree.column(col, width=h[n],anchor=hd[n])
        n+=1

    # inserindo os itens dentro da tabela
    for item in lista_itens:
        tree.insert('', 'end', values=item)
    

    quantidade = []

    for iten in lista_itens:
        quantidade.append(iten[1])


    Total_itens = len(quantidade)


    l_quantidade['text'] = Total_itens

mostrar()




janela.mainloop()


