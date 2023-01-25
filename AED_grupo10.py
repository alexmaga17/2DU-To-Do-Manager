# IMPORTS
from os import read
from tkinter.ttk import * 
from shutil import copy2
import pathlib
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox, Labelframe
import datetime
from datetime import timedelta
from tkcalendar import Calendar,DateEntry
import matplotlib
matplotlib.use('TkAgg')
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk, Image
import re
import pyglet, os

# Adiciona Fontes exteriores
pyglet.font.add_file('Gilroy-Medium.otf')
pyglet.font.add_file('Gilroy-Black.otf')
pyglet.font.add_file('Gilroy-Regular.otf')
pyglet.font.add_file('Gilroy-Bold.otf')

# Inicia uma varíavel que passará a True se o utilizador introduzir uma conta válida
loginTF = False

# Inicia variáveis que vão guardar as informações do utilizador
nomeUtilizadorLoggedIn = " "
emailLoggedIn = " "
rankLoggedIn = " "
passwordLoggedIn = " "
avatar = " "
filename = ""
filename2 = ""

showPasse = False

# Função relacionada com a janela de login
def funcJanelaInicial():
    global showPasse
    def funcShowPasse():
        global showPasse
        if not showPasse:
            showPasse = True
            entryPasse['show'] = ""
        elif showPasse == True:
            showPasse = False
            entryPasse['show'] = "*"

    def funcbtnLogin():
        global loginTF, janelaInicial, nomeUtilizadorLoggedIn, emailLoggedIn, rankLoggedIn, passwordLoggedIn # "Globaliza" as informações do user , para q possam ser usadas em todas as funções
        # Abre o ficheiro utilizadores em modo Read
        ficheiro = open("utilizadores.txt", "r", encoding="utf-8")
        # Passa o user name dado para uma variável
        nomeUtilizadorDado = entryNomeUtilizador.get()
        # Passa a palavra-passe dada para uma varíavel
        passeDada = entryPasse.get()
        # Passa os dados do ficheiro utilizadores.txt para uma varíavel
        linhas = ficheiro.readlines()
        # Ciclo for que precorre todas as contas no ficheiro utilizadores.txt
        for linha in linhas:
            # Converte a informação da conta numa lista
            linhaDividida = list(linha.split(";"))
            # Passa a variável loginTF a True se as informações do utilizador estiverem na mesma linha e nas posições certas
            if nomeUtilizadorDado == linhaDividida[0] and passeDada == linhaDividida[2]:
                loginTF = True
                nomeUtilizadorLoggedIn = nomeUtilizadorDado
                emailLoggedIn = linhaDividida[1]
                rankLoggedIn = linhaDividida[3]
                janelaInicial.destroy()
                funcJanelaPrincipal()
        if loginTF == False:
            messagebox.showerror(title="ERRO", message="CONTA NÃO EXISTENTE!")
    # Função associada ao botão de registo
    def funcbtnRegisto():
        funcJanelaRegisto()
    # Função que permite dar login pressionando a tecla "ENTER"
    def enter(event=None):
        funcbtnLogin()

    # Inicia uma janela inicial com título "2Du - Inicio de Sessão"
    janelaInicial = Tk()
    janelaInicial.title("2Du - Inicio de Sessão")
    bg = "#282929"
    colorRed="#ff5454"
    janelaInicial.configure(bg=bg)

    # Faz com que a janela comece no centro
    w = 300  # width for the Tk root
    h = 500  # height for the Tk root
    ws = janelaInicial.winfo_screenwidth()
    hs = janelaInicial.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    janelaInicial.geometry("%dx%d+%d+%d" % (w, h, x, y))

    # Se pressionar enter, a função da linha 42 é executada e o botão Login é acionado
    janelaInicial.bind("<Return>", enter)

    # Widgets da página inicial
    my_pic = Image.open("images\\LOGO.png")
    resized = my_pic.resize((200,200), Image.ANTIALIAS)


    new_pic = ImageTk.PhotoImage(resized)
    janelaInicial.new_pic = new_pic
    my_label = Label(janelaInicial,image=new_pic,width=200,height=200,borderwidth=0,highlightthickness=0)
    my_label.pack()

    lblNomeUtilizador = Label(janelaInicial, text="Nome de Utilizador", bg=bg,fg="white", font=("Gilroy-Semibold",16))
    lblNomeUtilizador.place(x=50, y=177)

    entryNomeUtilizador = Entry(janelaInicial, width=20, font=("Gilroy-Medium",12),selectbackground=colorRed)
    entryNomeUtilizador.place(x=45, y=207)
    entryNomeUtilizador.focus()

    lblPasse = Label(janelaInicial, text="Palavra-Passe", bg=bg,fg="white", font=("Gilroy-Semibold",16))
    lblPasse.place(x=69, y=247)

    entryPasse = Entry(janelaInicial, width=20, show="*", font=("Gilroy-Medium",12),selectbackground=colorRed)
    entryPasse.place(x=45, y=277)
    #Utilizar uma imagem criada pelo grupo como botão para dar login
    btn7_img = Image.open("images\\btn7.png")
    btn7_img_resized = btn7_img.resize((190, 40), Image.ANTIALIAS)
    btn7_imagem = ImageTk.PhotoImage(btn7_img_resized)
    janelaInicial.btn7_imagem = btn7_imagem
    btnLogin = Button(janelaInicial, image = btn7_imagem, width = 190, height = 40, compound = CENTER,bg=bg,command=funcbtnLogin,highlightthickness = 0, bd = 0)
    btnLogin.place(x=52, y=380)
    #Utilizar uma imagem criada pelo grupo como botão para passar à janela de registo
    btn8_img = Image.open("images\\btn8.png")
    btn8_img_resized = btn8_img.resize((144, 30), Image.ANTIALIAS)
    btn8_imagem = ImageTk.PhotoImage(btn8_img_resized)
    janelaInicial.btn8_imagem = btn8_imagem
    btnRegisto = Button(janelaInicial, image = btn8_imagem, width = 144, height = 30, compound = CENTER,bg=bg,command=funcbtnRegisto,highlightthickness = 0, bd = 0)
    btnRegisto.place(x=75, y=430)

    btn17_img = Image.open("images\\btn17.png")
    btn17_img_resized = btn17_img.resize((120, 30), Image.ANTIALIAS)
    btn17_imagem = ImageTk.PhotoImage(btn17_img_resized)
    janelaInicial.btn17_imagem = btn17_imagem
    btnPasse = Button(janelaInicial, image=btn17_imagem,command=funcShowPasse, width = 120, height = 30, compound = CENTER,bg=bg,highlightthickness = 0, bd = 0)
    btnPasse.place(x=84,y=305)

    return janelaInicial

janelaInicial = funcJanelaInicial()

# Função relacionada com a janela de criação de conta
def funcJanelaRegisto():
    # Função que é ativada quando o botão de criar conta é ativado
    def funcbtnCriarConta():
        global emailLoggedIn, nomeUtilizadorLoggedIn, rankLoggedIn, passwordLoggedIn, filename  # Variáveis que podem ser utilizadas em qualquer função
        ficheiro = open("utilizadores.txt", "r", encoding="utf-8")
        linhas = ficheiro.readlines()
        emailValidar = entryEmail.get()
        userValidar = entryNomeUtilizador.get()
        passeValidar = entryPasse.get()
        cPasseValidar = entryCPasse.get()
        # Ciclo para evitar que seja criadas contas com nomes de utilizador e emails iguais a contas já existentes e também para verificar quas palavras passes inseridas são iguais
        for linha in linhas:
            linhaDividida = list(linha.split(";"))
            if linhaDividida[0] == userValidar:
                messagebox.showerror(
                    title="Erro", message="Nome de Utilizador já em utilização!"
                )
                return
            elif linhaDividida[1] == emailValidar:
                messagebox.showerror(title="Erro", message="Email já em utilização!")
                return
            elif passeValidar != cPasseValidar:
                messagebox.showerror(title="Erro", message="Palavras-passe não são iguais")
                return
        ficheiro.close()
        # Abre o ficheiro utilizadores.txt em mode Append
        ficheiro = open("utilizadores.txt", "a", encoding="utf-8")
        # Passa os dados introduzidos para variáveis
        emailLoggedIn = entryEmail.get()
        nomeUtilizadorLoggedIn = entryNomeUtilizador.get()
        passwordLoggedIn = entryPasse.get()
        # Dá o rank "user" ao novo utilizador
        rankLoggedIn = "user"
        # Junta os dados numa string e adiciona-a ao ficheiro utilizadores
        conta = (
            nomeUtilizadorLoggedIn
            + ";"
            + emailLoggedIn
            + ";"
            + passwordLoggedIn
            + ";"
            + rankLoggedIn
            + "\n"
        )
        ficheiro.write(conta)
        # Volta a colocar a variável password vazia
        passwordLoggedIn = " "
        imageDirectory = str(pathlib.Path(__file__).parent.absolute())
        imageDirectory += "/images/users/"
        imageDirectory += entryNomeUtilizador.get() + ".png"
        if filename == "":
            copy2("images/Default.png",imageDirectory)
        else:
            copy2(filename, imageDirectory)
        # Invoca a Janela Inicial e fecha a Janela de Registo
        janelaRegisto.withdraw()
        

    # Inicia uma janela de registo com dimensões 600x450 e título "2Du - Registo"
    janelaRegisto = Toplevel()
    janelaRegisto.title("2Du - Registo")
    bg = "#282929"
    colorRed="#ff5454"
    janelaRegisto.configure(bg=bg)

    # Faz com que a janela comece no centro
    w = 1000
    h = 450
    ws = janelaRegisto.winfo_screenwidth()
    hs = janelaRegisto.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    janelaRegisto.geometry("%dx%d+%d+%d" % (w, h, x, y))

    # Widgets da janela de registo
    lblTitulo = Label(janelaRegisto, text="CRIAR CONTA", bg=bg, fg=colorRed, font=("Gilroy-Black",65))
    lblTitulo.place(x=35, y=17)

    lblNomeUtilizador = Label(
        janelaRegisto, text="Nome de Utilizador:", bg=bg, fg="white", font=("Gilroy-Bold",20)
    )
    lblNomeUtilizador.place(x=40, y=143)
    entryNomeUtilizador = Entry(janelaRegisto, width=22, font=("Gilroy-Medium",14),selectbackground=colorRed)
    entryNomeUtilizador.place(x=44, y=185)

    lblEmail = Label(janelaRegisto, text="E-mail:", bg=bg, fg="white", font=("Gilroy-Bold",20))
    lblEmail.place(x=350, y=143)
    entryEmail = Entry(janelaRegisto, width=22, font=("Gilroy-Medium",14),selectbackground=colorRed)
    entryEmail.place(x=354, y=185)

    lblPasse = Label(janelaRegisto, text="Palavra-Passe:", bg=bg, fg="white", font=("Gilroy-Bold",20))
    lblPasse.place(x=40, y=267)
    entryPasse = Entry(janelaRegisto, show="*", width=22, font=("Gilroy-Medium",14),selectbackground=colorRed)
    entryPasse.place(x=44, y=304)

    lblCPasse = Label(janelaRegisto, text="Confirmar Palavra-Passe:", bg=bg, fg="white", font=("Gilroy-Bold",15))
    lblCPasse.place(x=350, y=267)
    entryCPasse = Entry(janelaRegisto, show="*", width=22, font=("Gilroy-Medium",14),selectbackground=colorRed)
    entryCPasse.place(x=354, y=304)

    # Função que é ativada quando o botão de selecionar avatar é ativa
    def funcAbrirImagem():
        global new_pic, filename
        # A varíavel "filename" recebe o caminho da pasta do avatar
        filename = filedialog.askopenfilename(title = "Select file",filetypes = (("all files","*.*"),("jpeg files","*.jpg"),("png files", "*.png")))
        my_pic = Image.open(filename)
        # A varíavel "new_pic" recebe o avatar com as novas dimensões
        new_pic = ImageTk.PhotoImage(my_pic.resize((180, 180)))
        janelaRegisto.new_pic = new_pic
        # O canvas mostra o novo avatar
        canvas.itemconfig(image_id, image=new_pic)

    # Canvas que mostra o avatar, por definição mostra o avatar "Default"
    canvas = Canvas(janelaRegisto,bg=bg,width=180,height=180,borderwidth=0,highlightthickness=0)
    canvas.place(x=720, y=120)
    my_pic = Image.open("images\\Default.png")
    resized = my_pic.resize((180,180), Image.ANTIALIAS)
    new_pic = ImageTk.PhotoImage(resized)
    janelaRegisto.new_pic = new_pic
    image_id = canvas.create_image(0, 0, anchor='nw', image=new_pic)

    #botão(imagem) para abrir uma imagem
    btn4_img = Image.open("images\\btn4.png")
    btn4_img_resized = btn4_img.resize((240, 36), Image.ANTIALIAS)
    btn4_imagem = ImageTk.PhotoImage(btn4_img_resized)
    janelaRegisto.btn4_imagem = btn4_imagem
    btnUpload = Button(janelaRegisto, image = btn4_imagem, width = 240, height = 36, compound = CENTER,bg=bg,highlightthickness = 0, bd = 0, command=funcAbrirImagem)
    btnUpload.place(x=690, y=340)
    #botão(imagem) para abrir criar conta
    btn8_2_img = Image.open("images\\btn8.png")
    btn8_2_img_resized = btn8_2_img.resize((190, 40), Image.ANTIALIAS)
    btn8_2_imagem = ImageTk.PhotoImage(btn8_2_img_resized)
    janelaInicial.btn8_2_imagem = btn8_2_imagem
    btnRegisto = Button(janelaRegisto, image = btn8_2_imagem, width = 190, height = 40, compound = CENTER,bg=bg,command=funcbtnCriarConta,highlightthickness = 0, bd = 0)
    btnRegisto.place(x=257, y=370)
    # Função para voltar á janela anterior
    def funcVoltar():
        janelaRegisto.withdraw()
    #Botão que permite voltar á janela de login (funcVoltar)
    btn16_img = Image.open("images\\btn16.png")
    btn16_img_resized = btn16_img.resize((190, 40), Image.ANTIALIAS)
    btn16_imagem = ImageTk.PhotoImage(btn16_img_resized)
    janelaInicial.btn16_imagem = btn16_imagem
    btnVoltar = Button(janelaRegisto, image = btn16_imagem, width = 190, height = 40, compound = CENTER,bg=bg, command=funcVoltar,highlightthickness = 0, bd = 0)
    btnVoltar.place(x=45, y=370)


# Função relacionada com a janela principal
def funcJanelaPrincipal():
    def funcAddTarefa():
        global nomeUtilizadorLoggedIn
        #abre o ficheiro tarefas para leitura
        ficheiro = open("tarefas.txt", "r", encoding="utf-8")
        linhas = ficheiro.readlines()
        dataCheck = cal.get_date()
        dataCheck = datetime.datetime.strptime(str(dataCheck), '%Y-%m-%d').strftime('%d/%m/%Y')
        # Ciclo para verficar se a tarefa inserida já se encontra no ficheiro tarefas
        for linha in linhas:
            linhaDividida = list(linha.split(";"))
            if linhaDividida[1] == entryTarefa.get() and linhaDividida[0] == comboUtilizadores.get() and linhaDividida[2] == dataCheck and linhaDividida[4] == comboCategoria.get():
                messagebox.showerror(title="Erro", message="Tarefa Duplicada!")
                return
        # Ciclos para verficiar se todas as informações sobre a tarefa são preenchidas        
        if not entryTarefa.get():
            messagebox.showerror(title="Erro", message="Insira um nome para a tarefa")
            return
        elif not comboCategoria.get():
            messagebox.showerror(title="Erro", message="Insira uma categoria")
            return
        elif not comboUtilizadores.get():
            messagebox.showerror(
                title="Erro", message="Escolha um utilizador para associar à tarefa"
            )
            return
        # Guardar todas as informações sobre a trefa numa linha do ficheiro separando os topicos por ";"    
        tarefasAGuardar = ""
        ficheiro = open("tarefas.txt", "a", encoding="utf-8")
        userAAdicionar = comboUtilizadores.get()
        tarefasAGuardar += userAAdicionar + ";"
        tarefaAAdicionar = entryTarefa.get()
        tarefasAGuardar += tarefaAAdicionar + ";"
        dataAAdicionar = cal.get_date()
        dataAAdicionar = datetime.datetime.strptime(str(dataAAdicionar), '%Y-%m-%d').strftime('%d/%m/%Y')
        tarefasAGuardar += dataAAdicionar + ";"
        estadoAGuardar = "Não Realizada"
        tarefasAGuardar += estadoAGuardar + ";"
        categoriaAGuardar = comboCategoria.get()
        tarefasAGuardar += categoriaAGuardar + ";"
        # Verificar se o utilizador quer ou não um lembrete e adicionar essa informação á ao ficheiro
        lembreteSimNao = selected.get()
        if lembreteSimNao == "Não":
            tarefasAGuardar += "Sem Lembrete;"
        elif lembreteSimNao == "Sim":
            tarefasAGuardar += datetime.datetime.strptime(str(cal2.get_date()), '%Y-%m-%d').strftime('%d/%m/%Y') + ";"
        tarefasAGuardar += nomeUtilizadorLoggedIn + ";"
        tarefasAGuardar += "nNotificado" + ";"
        tarefasAGuardar += "nNotificadoLem"
        ficheiro.write(tarefasAGuardar + "\n")
        ficheiro.close()
        ficheiro = open("tarefas.txt", "r", encoding="utf-8")
        listaTarefas.delete(*listaTarefas.get_children())
        linhas = ficheiro.readlines()
        # Ciclo para inserir as informações da tarefa numa  linha da componente TreeView
        for linha in linhas:
            linhaDividida = list(linha.split(";"))
            if linhaDividida[0] == nomeUtilizadorLoggedIn:
                listaTarefas.insert(
                    "",
                    "end",
                    values=(
                        linhaDividida[1],
                        linhaDividida[2],
                        linhaDividida[3],
                        linhaDividida[4],
                        linhaDividida[5],
                    ),
                )
        # Colocar o nome da imagem associada á tarefa com as caracteristicas da mesma
        imageDirectory1 = str(pathlib.Path(__file__).parent.absolute())
        imageDirectory2 = str(pathlib.Path(__file__).parent.absolute())
        imageDirectory1 += "/images/DefaultTarefa.png"
        imageDirectory2 += "/images/tarefas/"
        imageDirectory2 += userAAdicionar + "-" + tarefaAAdicionar + "-"+ str(cal.get_date().strftime('%d_%m_%Y')) + "-"+ categoriaAGuardar + ".png"
        copy2(imageDirectory1, imageDirectory2)
        if listaTarefas.get_children() != () and lblSTarefas:
            lblSTarefas.place(x=1280, y=1186)
        funcbtnFiltro()
    # Função para remover uma tarefa (tanto na TreeView como no ficheiro associado)
    def funcRemoveTarefa():
        global nomeUtilizadorLoggedIn
        # Guarda o ID da linha da tabela
        if not listaTarefas.selection():
            return
        idLinha = listaTarefas.selection()
        # Guarda o index desse ID
        indexLinha = listaTarefas.index(idLinha)
        # Abre o ficheiro tarefas.txt em modo read e guarda o seu contúdo da variável linhas
        ficheiro = open("tarefas.txt", "r", encoding="utf-8")
        linhas = ficheiro.readlines()
        ficheiro.close()
        # Abre o ficheiro tarefas.txt em modo write
        ficheiro = open("tarefas.txt", "w", encoding="utf-8")
        # Remove todos os items da lista
        listaTarefas.delete(*listaTarefas.get_children())
        # Inicia um contador a 0
        count = 0
        # Ciclo for que adiciona de novo as tarefas à tabela e ao ficheiro,
        # menos a tarefa que tem o mesmo index do que a que queremos remover
        for linha in linhas:
            linhaDividida = list(linha.split(";"))
            if linhaDividida[0] != nomeUtilizadorLoggedIn:
                ficheiro.write(linha)
            elif (linhaDividida[0] == nomeUtilizadorLoggedIn and len(linhaDividida)==9):
                if count != indexLinha:
                    ficheiro.write(linha)
                    listaTarefas.insert(
                        "",
                        "end",
                        values=(
                            linhaDividida[1],
                            linhaDividida[2],
                            linhaDividida[3],
                            linhaDividida[4],
                            linhaDividida[5],
                        ),
                    )
                else:
                    os.remove("images/tarefas/" + linhaDividida[0] + "-" + linhaDividida[1] + "-" + datetime.datetime.strptime(linhaDividida[2], '%d/%m/%Y').strftime('%d_%m_%Y') + "-" + linhaDividida[4] +".png")
                count += 1
            elif linhaDividida[0] == nomeUtilizadorLoggedIn and len(linhaDividida)==10:
                if not(linhaDividida[9] == "nAceitou\n" or linhaDividida[9] == "nAceitou") and (count != indexLinha):
                    listaTarefas.insert("","end",values=(linhaDividida[1],linhaDividida[2],linhaDividida[3],linhaDividida[4],linhaDividida[5],),)
                else:
                    os.remove("images/tarefas/" + linhaDividida[0] + "-" + linhaDividida[1] + "-" + datetime.datetime.strptime(linhaDividida[2], '%d/%m/%Y').strftime('%d_%m_%Y') + "-" + linhaDividida[4] +".png")
                count += 1

        if listaTarefas.get_children() != () and lblSTarefas:
            lblSTarefas.place(x=1280, y=1086)
        else:
            lblSTarefas.place(x=280, y=186)


    # Funcão que desativa o calendário se o utilizador não quiser lembrete
    def check():
        if selected.get() == "Não":
            cal2.configure(state="disabled")
        elif selected.get() == "Sim":
            cal2.configure(state="normal")
    # Função para mostrar as tarefas de acordo com um escolhido de uma lista
    def funcbtnFiltro():
        if comboFiltro.get() == "Todas as Tarefas":
            ficheiro = open("tarefas.txt", "r", encoding="utf-8")
            linhas = ficheiro.readlines()
            listaTarefas.delete(*listaTarefas.get_children())
            for linha in linhas:
                linhaDividida = list(linha.split(";"))
                if (linhaDividida[0] == nomeUtilizadorLoggedIn and len(linhaDividida)==9):
                    listaTarefas.insert(
                        "",
                        "end",
                        values=(
                            linhaDividida[1],
                            linhaDividida[2],
                            linhaDividida[3],
                            linhaDividida[4],
                            linhaDividida[5],
                        ),
                    )
                elif linhaDividida[0] == nomeUtilizadorLoggedIn and len(linhaDividida)==10:
                    if not(linhaDividida[9] == "nAceitou\n" or linhaDividida[9] == "nAceitou"):
                        listaTarefas.insert("","end",values=(linhaDividida[1],linhaDividida[2],linhaDividida[3],linhaDividida[4],linhaDividida[5],),)
            if listaTarefas.get_children() != () and lblSTarefas:
                lblSTarefas.place(x=1280, y=1086)
            else:
                lblSTarefas.place(x=280, y=186) 

        elif comboFiltro.get() == "Hoje":
            data = datetime.datetime.now()
            dataOrdenada = data.strftime("%d/%m/%Y")
            ficheiro = open("tarefas.txt", "r", encoding="utf-8")
            linhas = ficheiro.readlines()
            listaTarefas.delete(*listaTarefas.get_children())
            for linha in linhas:
                linhaDividida = list(linha.split(";"))
                if (
                    linhaDividida[2] == dataOrdenada
                    and linhaDividida[0] == nomeUtilizadorLoggedIn
                    and len(linhaDividida)==9
                ):
                    listaTarefas.insert(
                        "",
                        "end",
                        values=(
                            linhaDividida[1],
                            linhaDividida[2],
                            linhaDividida[3],
                            linhaDividida[4],
                            linhaDividida[5],
                        ),
                    )
                elif linhaDividida[2] == dataOrdenada and linhaDividida[0] == nomeUtilizadorLoggedIn and len(linhaDividida)==10:
                    if not(linhaDividida[9] == "nAceitou\n" or linhaDividida[9] == "nAceitou"):
                        listaTarefas.insert("","end",values=(linhaDividida[1],linhaDividida[2],linhaDividida[3],linhaDividida[4],linhaDividida[5],),)
            if listaTarefas.get_children() != () and lblSTarefas:
                lblSTarefas.place(x=1280, y=1086)
            else:
                lblSTarefas.place(x=280, y=186) 

        elif comboFiltro.get() == "Próximas Tarefas":
            data = datetime.datetime.now()
            dataOrdenadaString = data.strftime("%d/%m/%Y")
            dataOrdenada = datetime.datetime.strptime(dataOrdenadaString, "%d/%m/%Y")
            ficheiro = open("tarefas.txt", "r", encoding="utf-8")
            linhas = ficheiro.readlines()
            listaTarefas.delete(*listaTarefas.get_children())
            for linha in linhas:
                linhaDividida = list(linha.split(";"))
                dataTarefa = datetime.datetime.strptime(linhaDividida[2], "%d/%m/%Y")
                if (dataOrdenada <= dataTarefa <= dataOrdenada + timedelta(hours=24)) and (linhaDividida[0] == nomeUtilizadorLoggedIn) and (len(linhaDividida)==9):
                    listaTarefas.insert(
                        "",
                        "end",
                        values=(
                            linhaDividida[1],
                            linhaDividida[2],
                            linhaDividida[3],
                            linhaDividida[4],
                            linhaDividida[5],
                        ),
                    )
                elif (dataOrdenada <= dataTarefa <= dataOrdenada + timedelta(hours=24)) and (linhaDividida[0] == nomeUtilizadorLoggedIn) and (len(linhaDividida)==10):
                    if not(linhaDividida[9] == "nAceitou\n" or linhaDividida[9] == "nAceitou"):
                        listaTarefas.insert("","end",values=(linhaDividida[1],linhaDividida[2],linhaDividida[3],linhaDividida[4],linhaDividida[5],),)
            if listaTarefas.get_children() != () and lblSTarefas:
                lblSTarefas.place(x=1280, y=1086)
            else:
                lblSTarefas.place(x=280, y=186)

        elif "Estado: " in comboFiltro.get():
            ficheiro = open("tarefas.txt", "r", encoding="utf-8")
            linhas = ficheiro.readlines()
            listaTarefas.delete(*listaTarefas.get_children())
            for linha in linhas:
                linhaDividida = list(linha.split(";"))
                estado = "Estado: " + linhaDividida[3]
                if (
                    estado == comboFiltro.get()
                    and linhaDividida[0] == nomeUtilizadorLoggedIn
                    and len(linhaDividida)==9
                ):
                    listaTarefas.insert(
                        "",
                        "end",
                        values=(
                            linhaDividida[1],
                            linhaDividida[2],
                            linhaDividida[3],
                            linhaDividida[4],
                            linhaDividida[5],
                        ),
                    )
                elif estado == comboFiltro.get() and linhaDividida[0] == nomeUtilizadorLoggedIn and len(linhaDividida)==10:
                    if not(linhaDividida[9] == "nAceitou\n" or linhaDividida[9] == "nAceitou"):
                        listaTarefas.insert("","end",values=(linhaDividida[1],linhaDividida[2],linhaDividida[3],linhaDividida[4],linhaDividida[5],),)
            if listaTarefas.get_children() != () and lblSTarefas:
                lblSTarefas.place(x=1280, y=1086)
            else:
                lblSTarefas.place(x=280, y=186)                         

        elif "Categoria: " in comboFiltro.get():
            ficheiro = open("tarefas.txt", "r", encoding="utf-8")
            linhas = ficheiro.readlines()
            listaTarefas.delete(*listaTarefas.get_children())
            for linha in linhas:
                linhaDividida = list(linha.split(";"))
                categoria = "Categoria: " + linhaDividida[4]
                if (
                    categoria == comboFiltro.get()
                    and linhaDividida[0] == nomeUtilizadorLoggedIn
                    and len(linhaDividida)==9
                ):
                    listaTarefas.insert(
                        "",
                        "end",
                        values=(
                            linhaDividida[1],
                            linhaDividida[2],
                            linhaDividida[3],
                            linhaDividida[4],
                            linhaDividida[5],
                        ),
                    )
                elif categoria == comboFiltro.get() and linhaDividida[0] == nomeUtilizadorLoggedIn and len(linhaDividida)==10:
                    if not(linhaDividida[9] == "nAceitou\n" or linhaDividida[9] == "nAceitou"):
                        listaTarefas.insert("","end",values=(linhaDividida[1],linhaDividida[2],linhaDividida[3],linhaDividida[4],linhaDividida[5],),)
            if listaTarefas.get_children() != () and lblSTarefas:
                lblSTarefas.place(x=1280, y=1086)
            else:
                lblSTarefas.place(x=280, y=186)                         
    
    def funcJanelaResultadoTarefaExterior(count,linhaDividida):
        # Função que vai ser realizada caso o utilizador não aceite a tarefa atibuida por outro utilizador 
        def funcNAceitou(count,linhaDividida):
            def funcFecharNAceitou():
                janelaNAceitou.destroy()
            # Inicia uma janela principal com e título "2Du - Notificação"
            janelaNAceitou = Toplevel()
            janelaNAceitou.title("2Du - Notificação")
            # Faz com que a janela comece no centro
            w = 430
            h = 230
            ws = janelaNAceitou.winfo_screenwidth()
            hs = janelaNAceitou.winfo_screenheight()
            x = (ws / 2) - (w / 2)
            y = (hs / 2) - (h / 2)
            janelaNAceitou.geometry("%dx%d+%d+%d" % (w, h, x, y))
            bg = "#282929"
            colorRed="#ff5454"
            janelaNAceitou.configure(bg=bg)

            lblTitulo = Label(janelaNAceitou, text="TAREFA EXTERIOR",bg=bg, fg=colorRed, font=("Gilroy-Black",35), anchor="e", justify=LEFT)
            lblTitulo.place(x=10,y=10)

            texto = "O utilizador " + "\nnão aceitou a tarefa"

            lblNAceitou=Label(janelaNAceitou, text=texto,bg=bg, fg="white", font=("Gilroy-Bold",16), anchor="e", justify=LEFT)
            lblNAceitou.place(x=10,y=80)

            tarefaAvisar = linhaDividida[1]
            userAvisar = linhaDividida[6]

            lblTarefaAvisar = Label(janelaNAceitou, text=tarefaAvisar,bg=bg, fg=colorRed, font=("Gilroy-Bold",19), anchor="e", justify=LEFT)
            lblTarefaAvisar.place(x=10,y=135)

            lblUserAvisar = Label(janelaNAceitou, text=userAvisar,bg=bg, fg=colorRed, font=("Gilroy-Bold",19), anchor="e", justify=LEFT)
            lblUserAvisar.place(x=130,y=75)

            btn15_img = Image.open("images\\btn15.png")
            btn15_img_resized = btn15_img.resize((64, 28), Image.ANTIALIAS)
            btn15_imagem = ImageTk.PhotoImage(btn15_img_resized)
            janelaNAceitou.btn15_imagem = btn15_imagem
            btnOk = Button(janelaNAceitou, image = btn15_imagem, width = 64, height = 28, compound = CENTER,command=funcFecharNAceitou,bg=bg,highlightthickness = 0, bd = 0)
            btnOk.place(x=13, y=195)

            ficheiro = open("tarefas.txt", "r", encoding="utf-8")
            linhas = ficheiro.readlines()
            ficheiro.close()
            ficheiro = open("tarefas.txt", "w", encoding="utf-8")
            listaTarefas.delete(*listaTarefas.get_children())
            count2 = 0
            for linha in linhas:
                if count != count2:
                    linhaDividida = list(linha.split(";"))
                    ficheiro.write(linha)
                    if linhaDividida[0] == nomeUtilizadorLoggedIn:
                        listaTarefas.insert("","end",values=(linhaDividida[1],linhaDividida[2],linhaDividida[3],linhaDividida[4],linhaDividida[5],),)
                count2 += 1

        # Função que vai ser realizada caso o utilizador aceite a tarefa atibuida por outro utilizador 
        def funcAceitou(count,linhaDividida):
            def funcFecharAceitou():
                janelaAceitou.destroy()
            # Inicia uma janela com e título "2Du - Notificação"
            janelaAceitou = Toplevel()
            janelaAceitou.title("2Du - Notificação")
            bg = "#282929"
            janelaAceitou.configure(bg=bg)

            # Faz com que a janela comece no centro
            w = 430
            h = 230
            ws = janelaAceitou.winfo_screenwidth()
            hs = janelaAceitou.winfo_screenheight()
            x = (ws / 2) - (w / 2)
            y = (hs / 2) - (h / 2)
            janelaAceitou.geometry("%dx%d+%d+%d" % (w, h, x, y))

            lblTitulo = Label(janelaAceitou, text="TAREFA EXTERIOR",bg=bg, fg=colorRed, font=("Gilroy-Black",35), anchor="e", justify=LEFT)
            lblTitulo.place(x=10,y=10)

            texto = "O utilizador " + "\naceitou a tarefa"

            lblAceitou=Label(janelaAceitou, text=texto,bg=bg, fg="white", font=("Gilroy-Bold",16), anchor="e", justify=LEFT)
            lblAceitou.place(x=10,y=80)

            tarefaAvisar = linhaDividida[1]
            userAvisar = linhaDividida[6]

            lblTarefaAvisar = Label(janelaAceitou, text=tarefaAvisar,bg=bg, fg=colorRed, font=("Gilroy-Bold",19), anchor="e", justify=LEFT)
            lblTarefaAvisar.place(x=10,y=135)

            lblUserAvisar = Label(janelaAceitou, text=userAvisar,bg=bg, fg=colorRed, font=("Gilroy-Bold",19), anchor="e", justify=LEFT)
            lblUserAvisar.place(x=130,y=75)

            btn15_img = Image.open("images\\btn15.png")
            btn15_img_resized = btn15_img.resize((64, 28), Image.ANTIALIAS)
            btn15_imagem = ImageTk.PhotoImage(btn15_img_resized)
            janelaAceitou.btn15_imagem = btn15_imagem
            btnOk = Button(janelaAceitou, image = btn15_imagem, width = 64, height = 28, compound = CENTER,command=funcFecharAceitou,bg=bg,highlightthickness = 0, bd = 0)
            btnOk.place(x=13, y=195)

            ficheiro = open("tarefas.txt", "r", encoding="utf-8")
            linhas = ficheiro.readlines()
            ficheiro.close()
            ficheiro = open("tarefas.txt", "w", encoding="utf-8")
            listaTarefas.delete(*listaTarefas.get_children())
            count2 = 0
            for linha in linhas:
                if count == count2:
                    linhaDividida = list(linha.split(";"))
                    linhaDividida[9] ="AceitouNotif\n"
                    linha = ";".join(linhaDividida)
                    ficheiro.write(linha)
                    if linhaDividida[0] == nomeUtilizadorLoggedIn:
                        listaTarefas.insert("","end",values=(linhaDividida[1],linhaDividida[2],linhaDividida[3],linhaDividida[4],linhaDividida[5],),)
                else:
                    linhaDividida = list(linha.split(";"))
                    ficheiro.write(linha)
                    if linhaDividida[0] == nomeUtilizadorLoggedIn:
                        listaTarefas.insert("","end",values=(linhaDividida[1],linhaDividida[2],linhaDividida[3],linhaDividida[4],linhaDividida[5],),)
                count2 += 1 

        if (linhaDividida[9] == "nAceitou\n"):
            funcNAceitou(count,linhaDividida)
        elif (linhaDividida[9] == "Aceitou\n"):
            funcAceitou(count,linhaDividida)

    def funcJanelaTarefaExterior(count,linhaDividida):
        def funcSim():
            ficheiro = open("tarefas.txt", "r", encoding="utf-8")
            linhas = ficheiro.readlines()
            ficheiro.close()
            ficheiro = open("tarefas.txt", "w", encoding="utf-8")
            listaTarefas.delete(*listaTarefas.get_children())
            count2 = 0
            for linha in linhas:
                linhaDividida = list(linha.split(";"))
                if count == count2:
                    linhaDividida[-1] = linhaDividida[-1].strip()
                    linhaDividida.append("Aceitou\n")
                    linha = ";".join(linhaDividida)
                    ficheiro.write(linha)
                else:
                    ficheiro.write(linha)
                count2 += 1
            ficheiro.close()
            janelaTarefaExterior.grab_release()
            ficheiro = open("tarefas.txt", "r", encoding="utf-8")
            linhas = ficheiro.readlines()
            listaTarefas.delete(*listaTarefas.get_children())
            for linha in linhas:
                linhaDividida = list(linha.split(";"))
                if (linhaDividida[0] == nomeUtilizadorLoggedIn and len(linhaDividida)==9):
                    listaTarefas.insert("","end",values=(linhaDividida[1],linhaDividida[2],linhaDividida[3],linhaDividida[4],linhaDividida[5],),)
                elif linhaDividida[0] == nomeUtilizadorLoggedIn and len(linhaDividida)==10:
                    if not(linhaDividida[9] == "nAceitou\n" or linhaDividida[9] == "nAceitou"):
                        listaTarefas.insert("","end",values=(linhaDividida[1],linhaDividida[2],linhaDividida[3],linhaDividida[4],linhaDividida[5],),)
            janelaTarefaExterior.destroy()
            if listaTarefas.get_children() != () and lblSTarefas:
                lblSTarefas.place(x=1280, y=1086)
            else:
                lblSTarefas.place(x=280, y=186)   

        def funcNao(linhaDivididaExterior):
            ficheiro = open("tarefas.txt", "r", encoding="utf-8")
            linhas = ficheiro.readlines()
            ficheiro.close()
            ficheiro = open("tarefas.txt", "w", encoding="utf-8")
            listaTarefas.delete(*listaTarefas.get_children())
            for linha in linhas:
                linhaDividida = list(linha.split(";"))
                if linhaDivididaExterior[0] == linhaDividida[0] and linhaDivididaExterior[1] == linhaDividida[1] and linhaDivididaExterior[2] == linhaDividida[2] and linhaDivididaExterior[4] == linhaDividida[4]:
                    linhaDividida[-1] = linhaDividida[-1].strip()
                    linhaDividida.append("nAceitou\n")
                    linha = ";".join(linhaDividida)
                    ficheiro.write(linha)
                else:
                    ficheiro.write(linha)
            ficheiro.close()
            ficheiro = open("tarefas.txt", "r", encoding="utf-8")
            linhas = ficheiro.readlines()
            listaTarefas.delete(*listaTarefas.get_children())
            for linha in linhas:
                linhaDividida = list(linha.split(";"))
                if (linhaDividida[0] == nomeUtilizadorLoggedIn and len(linhaDividida)==9):
                    listaTarefas.insert("","end",values=(linhaDividida[1],linhaDividida[2],linhaDividida[3],linhaDividida[4],linhaDividida[5],),)
                elif linhaDividida[0] == nomeUtilizadorLoggedIn and len(linhaDividida)==10:
                    if not(linhaDividida[9] == "nAceitou\n" or linhaDividida[9] == "nAceitou"):
                        listaTarefas.insert("","end",values=(linhaDividida[1],linhaDividida[2],linhaDividida[3],linhaDividida[4],linhaDividida[5],),)
            if listaTarefas.get_children() != () and lblSTarefas:
                lblSTarefas.place(x=1280, y=1086)
            else:
                lblSTarefas.place(x=280, y=186)

            os.remove("images/tarefas/" + linhaDivididaExterior[0] + "-" + linhaDivididaExterior[1] + "-" + datetime.datetime.strptime(linhaDivididaExterior[2], '%d/%m/%Y').strftime('%d_%m_%Y') + "-" + linhaDivididaExterior[4] +".png")
            janelaTarefaExterior.destroy()

        # Inicia uma janela com e título "2Du - Tarefa Exterior"
        janelaTarefaExterior = Toplevel()
        janelaTarefaExterior.title("2Du - Tarefa Exterior")
        bg = "#282929"
        janelaTarefaExterior.configure(bg=bg)

        # Faz com que a janela comece no centro
        w = 430
        h = 270
        ws = janelaTarefaExterior.winfo_screenwidth()
        hs = janelaTarefaExterior.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        janelaTarefaExterior.geometry("%dx%d+%d+%d" % (w, h, x, y))

        janelaTarefaExterior.grab_set()

        lblTitulo = Label(janelaTarefaExterior, text="TAREFA EXTERIOR",bg=bg, fg=colorRed, font=("Gilroy-Black",35), anchor="e", justify=LEFT)
        lblTitulo.place(x=10,y=10)

        aviso = "O utilizador " + "\natribuiu-lhe a seguinte tarefa:"
        tarefaAvisar = linhaDividida[1]
        userAvisar = linhaDividida[6]

        lblAviso = Label(janelaTarefaExterior, text=aviso,bg=bg, fg="white", font=("Gilroy-Bold",16), anchor="e", justify=LEFT)
        lblAviso.place(x=10,y=80)

        lblTarefaAvisar = Label(janelaTarefaExterior, text=tarefaAvisar,bg=bg, fg=colorRed, font=("Gilroy-Bold",19), anchor="e", justify=LEFT)
        lblTarefaAvisar.place(x=10,y=135)

        lblUserAvisar = Label(janelaTarefaExterior, text=userAvisar,bg=bg, fg=colorRed, font=("Gilroy-Bold",19), anchor="e", justify=LEFT)
        lblUserAvisar.place(x=130,y=75)

        lblPergunta = Label(janelaTarefaExterior, text="Deseja aceitar esta tarefa?",bg=bg, fg="white", font=("Gilroy-Bold",16), anchor="e", justify=LEFT)
        lblPergunta.place(x=10,y=180)

        btn13_img = Image.open("images\\btn13.png")
        btn13_img_resized = btn13_img.resize((64, 28), Image.ANTIALIAS)
        btn13_imagem = ImageTk.PhotoImage(btn13_img_resized)
        janelaTarefaExterior.btn13_imagem = btn13_imagem
        btnSim = Button(janelaTarefaExterior, image = btn13_imagem, width = 64, height = 28, compound = CENTER,bg=bg,command=funcSim,highlightthickness = 0, bd = 0)
        btnSim.place(x=13, y=215)

        btn14_img = Image.open("images\\btn14.png")
        btn14_img_resized = btn14_img.resize((64, 28), Image.ANTIALIAS)
        btn14_imagem = ImageTk.PhotoImage(btn14_img_resized)
        janelaTarefaExterior.btn14_imagem = btn14_imagem
        btnNao = Button(janelaTarefaExterior, image = btn14_imagem, width = 64, height = 28, compound = CENTER,bg=bg,command=lambda: funcNao(linhaDividida),highlightthickness = 0, bd = 0)
        btnNao.place(x=90, y=215)

        btnTeste = Button(janelaTarefaExterior,text="teste", width = 64, height = 28, compound = CENTER,bg=bg,fg="white",command=lambda: funcNao(linhaDividida),highlightthickness = 0, bd = 0)
        btnTeste.place(x=160,y=215)


    # Inicia uma janela principal com dimensões 600x450 e título "2Du"
    janelaPrincipal = Tk()
    janelaPrincipal.title("2Du")
    bg = "#282929"
    colorRed="#ff5454"
    janelaPrincipal.configure(bg=bg)

    # Faz com que a janela comece no centro
    w = 1020
    h = 800
    ws = janelaPrincipal.winfo_screenwidth()
    hs = janelaPrincipal.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    janelaPrincipal.geometry("%dx%d+%d+%d" % (w, h, x, y))


    # Pega no nome das colunas e cria uma treeview com essas colunas
    style = ttk.Style()
    style.configure("Treeview",foreground="black",rowheight=30, font=("Gilroy-Bold",17))
    style.map("Treeview",background=[("selected",colorRed)])
    style = ttk.Style()
    style.configure("Treeview.Heading", font=("Gilroy-Medium",11))
    colunas = ("Tarefa", "Data", "Estado", "Categoria", "Lembrete")
    listaTarefas = ttk.Treeview(janelaPrincipal, columns=colunas, show="headings")
    listaTarefas.place(x=10, y=70)
    listaTarefas.column("Tarefa",anchor="c")
    listaTarefas.column("Data",anchor="c")
    listaTarefas.column("Estado",anchor="c")
    listaTarefas.column("Categoria",anchor="c")
    listaTarefas.column("Lembrete",anchor="c")
    for col in colunas:
        listaTarefas.heading(
            col,
            text=col,
        )
        listaTarefas.column(col, minwidth=0, width=198)

    # Adiciona as tarefas do utilizador no startup
    ficheiro = open("tarefas.txt", "r", encoding="utf-8")
    linhas = ficheiro.readlines()
    data = datetime.datetime.now()
    dataOrdenada = data.strftime("%d/%m/%Y")
    count = 0
    #Faz aparecer as tarefas do utilizador logado 
    for linha in linhas:
        linhaDividida = list(linha.split(";"))
        if len(linhaDividida)==10:
            if (linhaDividida[9] == "nAceitou\n" and linhaDividida[0] != nomeUtilizadorLoggedIn and linhaDividida[6] == nomeUtilizadorLoggedIn) or (linhaDividida[9] == "Aceitou\n" and linhaDividida[0] != nomeUtilizadorLoggedIn and linhaDividida[6]== nomeUtilizadorLoggedIn):
                funcJanelaResultadoTarefaExterior(count,linhaDividida)
        if linhaDividida[0] == nomeUtilizadorLoggedIn:
            if linhaDividida[0] != linhaDividida[6] and len(linhaDividida)==9:
                funcJanelaTarefaExterior(count,linhaDividida)
            elif (len(linhaDividida)==10 and (linhaDividida[9] == "Aceitou\n" or linhaDividida[9] == "Aceitou" or linhaDividida[9] == "AceitouNotif\n" or linhaDividida[9] == "AceitouNotif")) or len(linhaDividida)==9:
                listaTarefas.insert(
                    "",
                    "end",
                    values=(
                        linhaDividida[1],
                        linhaDividida[2],
                        linhaDividida[3],
                        linhaDividida[4],
                        linhaDividida[5],
                    ),
                )
                if dataOrdenada == linhaDividida[2] and (linhaDividida[7] == "nNotificado" or linhaDividida[7] == "nNotificado\n"):
                    funcJanelaNotificacaoData(count, linhaDividida)
                if dataOrdenada == linhaDividida[5] and (linhaDividida[8] == "nNotificadoLem" or linhaDividida[8] == "nNotificadoLem\n"):
                    funcJanelaNotificacaoLembrete(count, linhaDividida)
        count += 1

    ###################################
    #             Filtros             #
    ###################################
    # Cria uma lista com três filtros iniciais
    filtros = ["Todas as Tarefas", "Hoje", "Próximas Tarefas"]
    # Abre o ficheiro categorias.txt para adicionar as categorias à lista filtros
    ficheiro = open("categorias.txt", "r", encoding="utf-8")
    linha = ficheiro.readline()
    linhaDividida = list(linha.split(";"))
    for palavra in linhaDividida:
        filtros.append("Categoria: " + palavra)
    ficheiro.close()
    # Abre o ficheiro estados.txt para adicionar os estados à lista filtros
    ficheiro = open("estados.txt", "r", encoding="utf-8")
    linha = ficheiro.readline()
    linhaDividida = list(linha.split(";"))
    for palavra in linhaDividida:
        filtros.append("Estado: " + palavra)
    ficheiro.close()

    ##################################
    #   Widgets da janela principal  #
    ##################################
    s = Style()
    s.configure('My.TFrame', background=bg)
    group1 = ttk.Frame(janelaPrincipal, width=1000, height=400, style='My.TFrame')
    group1.place(x=10, y=470)
    #Fazer aparecer o logótipo da aplicação
    my_pic2 = Image.open("images\\LOGO2.png")
    resized2 = my_pic2.resize((162,61), Image.ANTIALIAS)
    new_pic2 = ImageTk.PhotoImage(resized2)
    janelaPrincipal.new_pic2 = new_pic2
    my_label2 = Label(janelaPrincipal,image=new_pic2,width=162,height=61,borderwidth=0,highlightthickness=0,bg=bg)
    my_label2.place(x=10,y=4)

    # Botão Add Tarefa
    btn6_img = Image.open("images\\btn6.png")
    btn6_img_resized = btn6_img.resize((574, 86), Image.ANTIALIAS)
    btn6_imagem = ImageTk.PhotoImage(btn6_img_resized)
    janelaPrincipal.btn6_imagem = btn6_imagem
    btnAddTarefa = Button(
        group1,
        image = btn6_imagem,
        command=funcAddTarefa,
        compound = CENTER,bg=bg,
        width=574,
        height=86,
        highlightthickness = 0,
        bd = 0,
    )
    btnAddTarefa.place(x=413, y=210)

    # Botão Remover Tarefa
    btn1_img = Image.open("images\\btn1.png")
    btn1_img_resized = btn1_img.resize((380, 57), Image.ANTIALIAS)
    btn1_imagem = ImageTk.PhotoImage(btn1_img_resized)
    janelaPrincipal.btn1_imagem = btn1_imagem
    btnRemoveTarefa = Button(janelaPrincipal, image = btn1_imagem, width = 380, height = 57, compound = CENTER,bg=bg,command=funcRemoveTarefa,highlightthickness = 0, bd = 0)
    btnRemoveTarefa.place(x=615, y=420)

    # Botão Editar Tarefa
    btn2_img = Image.open("images\\btn2.png")
    btn2_img_resized = btn2_img.resize((380, 57), Image.ANTIALIAS)
    btn2_imagem = ImageTk.PhotoImage(btn2_img_resized)
    janelaPrincipal.btn2_imagem = btn2_imagem
    btnTarefaInfo = Button(janelaPrincipal, image = btn2_imagem, width = 380, height = 57, compound = CENTER,bg=bg,command=lambda: funcJanelaTarefa(listaTarefas),highlightthickness = 0, bd = 0)
    btnTarefaInfo.place(x=20, y=420)

    # Combo Selecionar Filtro
    janelaPrincipal.option_add('*TCombobox*Listbox.selectBackground', colorRed)
    janelaPrincipal.option_add('*TCombobox*Listbox.selectForeground', 'white')
    comboFiltro = Combobox(janelaPrincipal, values=filtros, state="readonly", font=("Gilroy-Medium",10), width=20)
    comboFiltro.place(x=415, y=422)
    comboFiltro.set("Todas as Tarefas")
    
    # Botão Atualizar Filtro
    btn5_img = Image.open("images\\btn5.png")
    btn5_img_resized = btn5_img.resize((142, 21), Image.ANTIALIAS)
    btn5_imagem = ImageTk.PhotoImage(btn5_img_resized)
    janelaPrincipal.btn5_imagem = btn5_imagem
    btnFiltro = Button(janelaPrincipal, image = btn5_imagem, width = 142, height = 21, compound = CENTER,bg=bg,command=funcbtnFiltro,highlightthickness = 0, bd = 0)
    btnFiltro.place(x=435, y=451)

    # Label e Entry de Nome da Tarefa
    lblTarefa = Label(group1, text="Tarefa: ",bg=bg, fg="white", font=("Gilroy-Bold",21))
    lblTarefa.place(x=20, y=30)
    entryTarefa = Entry(group1, width=20, font=("Gilroy-Medium",20),selectbackground=colorRed)
    entryTarefa.place(x=25, y=67)

    # Label e Date Entry de Data da Tarefa
    lblData = Label(group1, text="Data",bg=bg, fg="white", font=("Gilroy-Bold",32))
    lblData.place(x=780, y=46)
    data = datetime.date.today()
    ano = data.year
    mes = data.month
    dia = data.day
    cal = DateEntry(
        group1,
        selectmode="day",
        date_pattern="dd/mm/y",
        year=ano,
        month=mes,
        day=dia,
        background=colorRed,
        foreground="black",
        font=("Gilroy-Regular",14),
        selectbackground=colorRed
    )
    cal.place(x=755, y=140)

    # Label e Combo de Categoria da Tarefa
    janelaPrincipal.option_add('*TCombobox*Listbox.font', ("Gilroy-Medium",12))
    lblCategoria = Label(group1, text="Categoria: ",bg=bg, fg="white", font=("Gilroy-Bold",21))
    lblCategoria.place(x=20, y=125)
    ficheiro = open("categorias.txt", "r", encoding="utf-8")
    linha = ficheiro.readline()
    categorias = list(linha.split(";"))
    comboCategoria = Combobox(group1, values=categorias, state="readonly", width=19, font=("Gilroy-Medium",20))
    comboCategoria.place(x=24, y=160)

    # Label e Combo de Utilizador a Atribuir a Tarefa
    lblUtilizadorTarefa = Label(group1, text="Utilizador: ",bg=bg, fg="white", font=("Gilroy-Bold",21))
    lblUtilizadorTarefa.place(x=20, y=220)
    ficheiro = open("utilizadores.txt", "r", encoding="utf-8")
    utilizadores = []
    linhas = ficheiro.readlines()
    for linha in linhas:
        utilizadorDados = list(linha.split(";"))
        utilizadores.append(utilizadorDados[0])
    comboUtilizadores = ttk.Combobox(group1, values=utilizadores, state="readonly", width=19, font=("Gilroy-Medium",20))
    comboUtilizadores.place(x=24, y=255)

    # Label, Radio Buttons e Date Entry de Lembrete da Tarefa
    lblLembrete = Label(group1, text="Lembrete",bg=bg, fg="white", font=("Gilroy-Bold",32))
    lblLembrete.place(x=460, y=46)
    style2 = ttk.Style()
    style2.configure("style.TRadiobutton", background=bg, foreground="white",font=("Gilroy-Regular",13))
    selected = StringVar()
    selected.set("Não")
    radioLembrete1 = ttk.Radiobutton(
        group1, text="Sim", variable=selected, value="Sim", command=check,style="style.TRadiobutton"
    )
    radioLembrete1.place(x=580, y=106)
    radioLembrete2 = ttk.Radiobutton(
        group1, text="Não", variable=selected, value="Não", command=check,style="style.TRadiobutton"
    )
    radioLembrete2.place(x=483, y=106)
    cal2 = DateEntry(
        group1,
        selectmode="day",
        date_pattern="dd/mm/y",
        year=ano,
        month=mes,
        day=dia,
        background=colorRed,
        foreground="black",
        font=("Gilroy-Regular",14),
        selectbackground=colorRed
    )
    cal2.place(x=475, y=140)
    cal2.configure(state = DISABLED)

    # Botão Abrir Dashboard
    btn3_img = Image.open("images\\btn3.png") 
    btn3_img_resized = btn3_img.resize((247, 45), Image.ANTIALIAS)
    btn3_imagem = ImageTk.PhotoImage(btn3_img_resized)
    janelaPrincipal.btn3_imagem = btn3_imagem
    btnDashboardAdmin = Button(janelaPrincipal, image = btn3_imagem, width = 247, height = 45, compound = CENTER,bg=bg,command=funcJanelaDashboardAdmin,highlightthickness = 0, bd = 0)
    btnDashboardAdmin.place(x=745, y=13)

    lblSTarefas = Label(janelaPrincipal, text="SEM TAREFAS",bg="white", fg=colorRed, font=("Gilroy-Black",52))
    lblSTarefas.place(x=280, y=186)

    if listaTarefas.get_children() != ():
        lblSTarefas.place(x=1080, y=1086)

# Função relacionada com a janela de informação sobre a tarefa selecionada
def funcJanelaTarefa(listaTarefas):
    def funcBtnGuardar(dataCheck):
        estadoNovo = comboEstados.get()
        comentario = entryComment.get()
        # Guarda o ID da linha da tabela
        idLinha = listaTarefas.selection()
        # Guarda o index desse ID
        indexLinha = listaTarefas.index(idLinha)
        ficheiro = open("tarefas.txt", "r", encoding="utf-8")
        linhas = ficheiro.readlines()
        ficheiro.close()
        listaTarefas.delete(*listaTarefas.get_children())
        ficheiro = open("tarefas.txt", "w", encoding="utf-8")
        count = 0
        for linha in linhas:
            linhaDividida = list(linha.split(";"))
            if linhaDividida[0] == nomeUtilizadorLoggedIn:
                if count == indexLinha:
                    linhaDividida[3] = estadoNovo
                    linha = ";".join(linhaDividida)
                ficheiro.write(linha)
                listaTarefas.insert(
                    "",
                    "end",
                    values=(
                        linhaDividida[1],
                        linhaDividida[2],
                        linhaDividida[3],
                        linhaDividida[4],
                        linhaDividida[5],
                    ),
                )
                count += 1
            else:
                ficheiro.write(linha)
        ## Abre o ficheiro de tarefas e verifica se a tarefa corresponde ao utilizador logado , para este poder dar um comentário
        ficheiro = open("tarefas.txt", "r", encoding="utf-8")
        linhas = ficheiro.readlines()
        ficheiro.close()
        count1 = 0 
        for linha in linhas:
            linhaDividida = list(linha.split(";"))
            if (linhaDividida[0] == nomeUtilizadorLoggedIn) or (linhaDividida[6] == nomeUtilizadorLoggedIn):
                if count1 == indexLinha:
                    ficheiro_comments = open("comentarios.txt","w",encoding="utf-8")
                    ficheiro_comments.write( linhaDividida[0] + ";" + linhaDividida[1] + ";" + comentario + "\n")
                    ficheiro_comments.close()
                
                count1 += 1
            else:
                entryComment.config(state='disabled')  
        # Adicionar nome na imagem de tarefa
        if filename2 != "":
            imageDirectory2 = str(pathlib.Path(__file__).parent.absolute())
            imageDirectory2 += "/images/tarefas/"
            imageDirectory2 += listValoresTarefa[0] + "-" + listValoresTarefa[1] + "-" + dataCheck.strftime('%d_%m_%Y') + "-" + listValoresTarefa[4] +".png"
            copy2(filename2, imageDirectory2)

        janelaTarefa.destroy()
    # Erro caso nao haja uma tarefa selecionada para editar
    if listaTarefas.item(listaTarefas.focus())["values"] == "":
        messagebox.showerror(title="Erro", message="Nenhuma Tarefa Selecionada")
        return

    # Inicia uma janela com informações sobre a tarefa selecionada e título "2Du - Tarefa"
    janelaTarefa = Toplevel()
    janelaTarefa.title("2Du - Tarefa")
    bg = "#282929"
    colorRed="#ff5454"
    janelaTarefa.configure(bg=bg)

    # Faz com que a janela comece no centro
    w = 600
    h = 800
    ws = janelaTarefa.winfo_screenwidth()
    hs = janelaTarefa.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    janelaTarefa.geometry("%dx%d+%d+%d" % (w, h, x, y))

    # Inicia uma variável que vai guardar os valores da linha selecionada
    valoresTarefa = nomeUtilizadorLoggedIn + ";"
    # Guarda todos os valores da linha selecionada
    for valor in listaTarefas.item(listaTarefas.focus())["values"]:
        valoresTarefa += str(valor) + ";"
    # Converte os valores da linha selecionada numa lista
    listValoresTarefa = valoresTarefa.split(";")

    lblTitulo = Label(janelaTarefa, text="EDITAR TAREFA", font=("Gilroy-Black",53), foreground=colorRed, background=bg)
    lblTitulo.place(x=40,y=30)

    lblNomeTarefa = Label(
        janelaTarefa, text=listValoresTarefa[1], bg=bg,fg="white", font=("Gilroy-Bold",45), anchor="e", justify=CENTER
    )
    lblNomeTarefa.place(x=42, y=155)

    lblTarefa = Label(janelaTarefa, text="Tarefa: ",bg=bg,fg="white", font=("Gilroy-Bold",20))
    lblTarefa.place(x=43, y=125)

    lblData = Label(janelaTarefa, text="Data: ", bg=bg,fg="white", font=("Gilroy-Bold",20))
    lblData.place(x=50, y=250)

    lblValorData = Label(
        janelaTarefa, text=listValoresTarefa[2], bg=bg,fg="white", font=("Gilroy-Medium",15)
    )
    lblValorData.place(x=65, y=290)

    lblLembrete = Label(janelaTarefa, text="Lembrete: ", bg=bg,fg="white", font=("Gilroy-Bold",20))
    lblLembrete.place(x=50, y=360)

    lblValorLembrete = Label(
        janelaTarefa, text=listValoresTarefa[5], bg=bg,fg="white", font=("Gilroy-Medium",15)
    )
    lblValorLembrete.place(x=65, y=410)

    lblCategoria = Label(janelaTarefa, text="Categoria: ", bg=bg,fg="white", font=("Gilroy-Bold",20))
    lblCategoria.place(x=50, y=480)

    lblNomeCategoria = Label(
        janelaTarefa, text=listValoresTarefa[4], bg=bg,fg="white", font=("Gilroy-Medium",15)
    )
    lblNomeCategoria.place(x=65, y=520)

    lblEstado = Label(janelaTarefa, text="Estado: ", bg=bg,fg="white", font=("Gilroy-Bold",20))
    lblEstado.place(x=50, y=590)

    # Abre o ficheiro que contém os estados possíveis em modo read
    ficheiro = open("estados.txt", "r", encoding="utf-8")
    # Guarda todos os estados possíveis numa variável
    linha = ficheiro.readline()
    # Converte numa lista
    estados = list(linha.split(";"))
    # Remove "\n"
    estados[-1] = estados[-1].strip("\n")
    # Guarda o estado da tarefa selecionada
    estadoTarefa = listValoresTarefa[3]
    # Se o estado da tarefa já não estiver no ficheiro estados.txt, ele é adicionado temporariamente à lista de estados
    if estadoTarefa not in estados:
        estados.append(estadoTarefa)

    janelaTarefa.option_add('*TCombobox*Listbox.selectBackground', colorRed)
    janelaTarefa.option_add('*TCombobox*Listbox.selectForeground', 'white')
    indexEstado = estados.index(estadoTarefa)
    comboEstados = Combobox(janelaTarefa, values=estados, state="readonly", font=("Gilroy-Medium",14), width=14)
    comboEstados.current(indexEstado)
    comboEstados.place(x=55, y=640)
    
    # botão para guardar a edição da tarefa
    btn_img_save = Image.open("images\\btn11.png")
    btn_img_resized = btn_img_save.resize((196, 42), Image.ANTIALIAS)
    btn_imagem = ImageTk.PhotoImage(btn_img_resized)
    janelaTarefa.btn_imagem = btn_imagem
    btnGuardar = Button(janelaTarefa, image = btn_imagem, width = 196, height = 42, compound = CENTER,command=lambda: funcBtnGuardar(dataCheck),highlightthickness = 0, bd = 0)
    btnGuardar.place(x=200, y=705)
    

    lblComentarios = Label(
        janelaTarefa, text="Comentários: ", bg=bg,fg="white", font=("Gilroy-Medium",20, "bold")
    )
    lblComentarios.place(x=283, y=520)
    
    # Recebe os comentários na janela da tarefa
    entryComment = Entry(janelaTarefa, width=15, font=("Gilroy-Medium",20))
    entryComment.place(x=288, y=560)

    frame1 = Frame(janelaTarefa,bd = 3)
    frame1.place(x=288 , y=610)

    # Uma scrollbar para os comentários
    scrollbar = Scrollbar(frame1)
    scrollbar.pack(side = RIGHT, fill = Y)

    # xscrollcommand parra scroll horizontal,  yscrollcommand para scroll vertical
    mylist = Listbox(frame1,height=3,width=38, yscrollcommand = scrollbar.set, xscrollcommand = scrollbar.set, bd = 2, relief = "sunken" )
    ## carregar dados de um ficheiro para a Listbox
    idLinha = listaTarefas.selection()
    # Guarda o index desse ID
    indexLinha = listaTarefas.index(idLinha)
    # Inserir na listbox os comentários escritos na entry    
    f=open("comentarios.txt", "r", encoding="utf-8")
    lista = f.readlines()
    f.close()
    count2 = 0 
    for linha in lista:
        linhaDividida = list(linha.split(";"))
        if (linhaDividida[0] == nomeUtilizadorLoggedIn): 
            if count2 == indexLinha:
                mylist.insert(END, linhaDividida[2]  + "\n")    
                
            count2 += 1    

    mylist.pack(side = LEFT, fill = BOTH )
    scrollbar.config( command = mylist.yview )
    #Função para adicionar uma imagem á tarefa durante a edição da mesma
    def funcAbrirImagem():
        global new_pic, filename2
        filename2 = filedialog.askopenfilename(title = "Select file",filetypes = (("all files","*.*"),("jpeg files","*.jpg"),("png files", "*.png")))
        my_pic = Image.open(filename2)
        new_pic = ImageTk.PhotoImage(my_pic.resize((160, 160)))
        janelaTarefa.new_pic = new_pic
        canvas3.itemconfig(image_id, image=new_pic)


    dataCheck = datetime.datetime.strptime(listValoresTarefa[2], '%d/%m/%Y')
    imageDirectory = str(pathlib.Path(__file__).parent.absolute())
    imageDirectory += "/images/tarefas/"
    imageDirectory += listValoresTarefa[0] + "-" + listValoresTarefa[1] + "-" + dataCheck.strftime('%d_%m_%Y') + "-" + listValoresTarefa[4] +".png"

    canvas3 = Canvas(janelaTarefa,bg=bg,width=160,height=160,borderwidth=0,highlightthickness=0)
    canvas3.place(x=335, y=260)
    my_pic = Image.open(imageDirectory)
    resized = my_pic.resize((160,160), Image.ANTIALIAS)
    new_pic = ImageTk.PhotoImage(resized)
    janelaTarefa.new_pic = new_pic
    image_id = canvas3.create_image(0, 0, anchor='nw', image=new_pic)

    #Botao para inserir imagem da tarefa (botão em formato imagem)
    btn4_2_img = Image.open("images\\btn4.png") 
    btn4_2_img_resized = btn4_2_img.resize((256, 39), Image.ANTIALIAS)
    btn4_2_imagem = ImageTk.PhotoImage(btn4_2_img_resized)
    janelaTarefa.btn4_2_imagem = btn4_2_imagem
    btnAvatar = Button(janelaTarefa, image = btn4_2_imagem, width = 256, height = 39, compound = CENTER,bg=bg,command=funcAbrirImagem,highlightthickness = 0, bd = 0)
    btnAvatar.place(x=290, y=453)


# Função relacionada com a janela de dashboard e definições de admin(Rank máximo)
def funcJanelaDashboardAdmin():
    def funcBtnGuardar(imageDirectory):
        categoriasNovas = txtCategorias.get("1.0", END)
        ficheiro = open("categorias.txt", "w", encoding="utf-8")
        categoriasNovas = categoriasNovas.strip("\n")
        ficheiro.write(categoriasNovas)
        ficheiro.close()
        estadosNovos = txtEstados.get("1.0", END)
        ficheiro = open("estados.txt", "w", encoding="utf-8")
        estadosNovos = estadosNovos.strip("\n")
        ficheiro.write(estadosNovos)
        copy2(filename, imageDirectory)

    def funcGraph1():
        lblFrame1.lift()

    def funcGraph2():
        lblFrame2.lift()

    def funcGraph3():
        lblFrame3.lift()

    # Inicia uma janela dashboard & admin com título "2Du - Dashboard & Definções de Admin"
    janelaDashboardAdmin = Toplevel()
    janelaDashboardAdmin.title("2Du - Dashboard & Definições de Admin")

    # Faz com que a janela comece no centro
    w = 1430
    h = 800
    ws = janelaDashboardAdmin.winfo_screenwidth()
    hs = janelaDashboardAdmin.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    janelaDashboardAdmin.geometry("%dx%d+%d+%d" % (w, h, x, y))
    bg = "#282929"
    colorRed="#ff5454"
    janelaDashboardAdmin.configure(bg=bg)

    lblTitulo = Label(janelaDashboardAdmin, text="DASHBOARD", font=("Gilroy-Black",90), foreground=colorRed, background=bg)
    lblTitulo.place(x=42,y=30)

    lblFrame1 = LabelFrame(janelaDashboardAdmin,width="300", height="300")
    lblFrame1.place(x=350,y=292)

    lblFrame2 = LabelFrame(janelaDashboardAdmin,width="200", height="200")
    lblFrame2.place(x=350,y=292)

    lblFrame3 = LabelFrame(janelaDashboardAdmin,width="200", height="200")
    lblFrame3.place(x=350,y=292)

    #########################
    #        GRÁFICOS       #
    #########################
    # GRÁFICO Nº TAREFAS/ESTADO
    ficheiro1 = open("estados.txt", "r", encoding="utf-8")
    linhas1 = ficheiro1.readline()
    listEstados = list(linhas1.split(";"))
    ficheiro2 = open("tarefas.txt", "r", encoding="utf-8")
    linhas2 = ficheiro2.readlines()
    listNum = []
    for estado in listEstados:
        count=0
        for linha in linhas2:
            linhaDividida = list(linha.split(";"))
            if estado == linhaDividida[3] and linhaDividida[0] == nomeUtilizadorLoggedIn:
                count +=1
        listNum.append(count)

    x= np.array (listEstados)
    v= np.array (listNum)
    
    fig = Figure(figsize=(4,4))
    a = fig.add_subplot(111)
    a.bar(x,v,color="#ff5454")

    a.set_title ("Nº Tarefas/Estado", fontsize=16)
    a.set_ylabel("Y", fontsize=4)
    a.set_xlabel("X", fontsize=4)

    matplotlib.rc('axes', labelsize=3) 

    canvas = FigureCanvasTkAgg(fig, master=lblFrame1)
    canvas.get_tk_widget().pack()
    canvas.draw()
    ficheiro1.close()
    ficheiro2.close()

    # GRÁFICO Nº TAREFAS/CATEGORIAS
    ficheiro1 = open("categorias.txt", "r", encoding="utf-8")
    linhas1 = ficheiro1.readline()
    listCategorias = list(linhas1.split(";"))
    ficheiro2 = open("tarefas.txt", "r", encoding="utf-8")
    linhas2 = ficheiro2.readlines()
    listNum2 = []
    for categoria in listCategorias:
        count=0
        for linha in linhas2:
            linhaDividida = list(linha.split(";"))
            if categoria == linhaDividida[4] and linhaDividida[0] == nomeUtilizadorLoggedIn:
                count +=1
        listNum2.append(count)

    x= np.array (listCategorias)
    v= np.array (listNum2)
    
    fig = Figure(figsize=(4,4))
    a = fig.add_subplot(111)
    a.bar(x,v,color="#ff5454")

    a.set_title ("Nº Tarefas/Categorias", fontsize=16)
    a.set_ylabel("Y", fontsize=4)
    a.set_xlabel("X", fontsize=4)

    matplotlib.rc('axes', labelsize=3) 

    canvas = FigureCanvasTkAgg(fig, master=lblFrame2)
    canvas.get_tk_widget().pack()
    canvas.draw()

    # GRÁFICO Nº TAREFAS/PRAZO
    ficheiro2 = open("tarefas.txt", "r", encoding="utf-8")
    linhas2 = ficheiro2.readlines()
    listNum = []
    today = datetime.datetime.now()
    dataHojeString = today.strftime("%d/%m/%Y")
    dataHoje = datetime.datetime.strptime(dataHojeString, "%d/%m/%Y")
    count=0
    for linha in linhas2:
        linhaDividida = list(linha.split(";"))
        dataTarefaCheck = datetime.datetime.strptime(linhaDividida[2], "%d/%m/%Y")
        if dataHoje == dataTarefaCheck and linhaDividida[0] == nomeUtilizadorLoggedIn:
            count +=1
    listNum.append(count)
    count=0
    for linha2 in linhas2:
        linhaDividida = list(linha2.split(";"))
        dataTarefaCheck = datetime.datetime.strptime(linhaDividida[2], "%d/%m/%Y")
        if dataHoje <= dataTarefaCheck <= dataHoje + timedelta(days=7) and linhaDividida[0] == nomeUtilizadorLoggedIn:
            count +=1
    listNum.append(count)
    count=0
    for linha3 in linhas2:
        linhaDividida = list(linha3.split(";"))
        dataTarefaCheck = datetime.datetime.strptime(linhaDividida[2], "%d/%m/%Y")
        if dataHoje <= dataTarefaCheck <= dataHoje + timedelta(days=30) and linhaDividida[0] == nomeUtilizadorLoggedIn:
            count +=1
    listNum.append(count)

    x= np.array (["Hoje", "Esta Semana", "Este Mês"])
    v= np.array (listNum)
    
    fig = Figure(figsize=(4,4))
    a = fig.add_subplot(111)
    a.bar(x,v,color="#ff5454")

    a.set_title ("Nº Tarefas/Prazo", fontsize=16)
    a.set_ylabel("Y", fontsize=4)
    a.set_xlabel("X", fontsize=4)

    matplotlib.rc('axes', labelsize=3) 

    canvas = FigureCanvasTkAgg(fig, master=lblFrame3)
    canvas.get_tk_widget().pack()
    canvas.draw()
    ficheiro2.close()
    ##############################
    #        Fim Gráficos        #
    ##############################
    btn9_img = Image.open("images\\btn9.png") 
    btn9_img_resized = btn9_img.resize((286, 132), Image.ANTIALIAS)
    btn9_imagem = ImageTk.PhotoImage(btn9_img_resized)
    janelaDashboardAdmin.btn9_imagem = btn9_imagem
    btnGraph1 = Button(janelaDashboardAdmin, image = btn9_imagem, width = 286, height = 132, compound = CENTER,bg=bg,command=funcGraph1,highlightthickness = 0, bd = 0)
    btnGraph1.place(x=45, y=293)

    btn12_img = Image.open("images\\btn12.png") 
    btn12_img_resized = btn12_img.resize((286, 132), Image.ANTIALIAS)
    btn12_imagem = ImageTk.PhotoImage(btn12_img_resized)
    janelaDashboardAdmin.btn12_imagem = btn12_imagem
    btnGraph3 = Button(janelaDashboardAdmin, image = btn12_imagem, width = 286, height = 132, compound = CENTER,bg=bg,command=funcGraph3,highlightthickness = 0, bd = 0)
    btnGraph3.place(x=45, y=428)

    btn10_img = Image.open("images\\btn10.png") 
    btn10_img_resized = btn10_img.resize((286, 132), Image.ANTIALIAS)
    btn10_imagem = ImageTk.PhotoImage(btn10_img_resized)
    janelaDashboardAdmin.btn10_imagem = btn10_imagem
    btnGraph2 = Button(janelaDashboardAdmin, image = btn10_imagem, width = 286, height = 132, compound = CENTER,bg=bg,command=funcGraph2,highlightthickness = 0, bd = 0)
    btnGraph2.place(x=45, y=563)

    lblGraphs = Label(janelaDashboardAdmin, text="Gráficos: ", bg=bg,fg="white", font=("Gilroy-Bold",30))
    lblGraphs.place(x=42, y=199)

    lblGraphs2 = Label(janelaDashboardAdmin, text="Analise gráficos baseados em 3 diferentes critérios", bg=bg,fg="white", font=("Gilroy-Medium",16))
    lblGraphs2.place(x=45, y=250)

    lblEstados = Label(janelaDashboardAdmin, text="Estados: ", bg=bg,fg="white", font=("Gilroy-Bold",30))
    lblEstados.place(x=855, y=30)

    lblEstados2 = Label(janelaDashboardAdmin,text="Altere os estados disponíveis (apenas para Admins)", bg=bg,fg="white", font=("Gilroy-Medium",12))
    lblEstados2.place(x=857, y=85)

    lblCategorias = Label(janelaDashboardAdmin, text="Categorias: ", bg=bg,fg="white", font=("Gilroy-Bold",30))
    lblCategorias.place(x=855, y=239)

    lblCategorias2 = Label(janelaDashboardAdmin,text="Altere as categorias disponíveis (apenas para Admins)", bg=bg,fg="white", font=("Gilroy-Medium",12))
    lblCategorias2.place(x=857, y=294)

    txtEstados = Text(janelaDashboardAdmin, width=44, height=4,font=("Gilroy-Bold",13))
    txtEstados.place(x=860, y=120)

    ficheiro = open("estados.txt", "r", encoding="utf-8")
    linha = ficheiro.readline()
    txtEstados.insert(1.0, linha)

    txtCategorias = Text(janelaDashboardAdmin, width=44, height=4,font=("Gilroy-Bold",13))
    txtCategorias.place(x=860, y=329)

    ficheiro = open("categorias.txt", "r", encoding="utf-8")
    linha = ficheiro.readline()
    txtCategorias.insert(1.0, linha)

    if "admin" not in rankLoggedIn:
        txtEstados.config(state="disabled")
        txtCategorias.config(state="disabled")
        lblDisabled1 = Label(janelaDashboardAdmin,text="NÃO É ADMIN",bg="white", fg=colorRed, font=("Gilroy-Black",59))
        lblDisabled1.place(x=854,y=120)
        lblDisabled2 = Label(janelaDashboardAdmin,text="NÃO É ADMIN",bg="white", fg=colorRed, font=("Gilroy-Black",59))
        lblDisabled2.place(x=854,y=330)

    lblInfo = Label(janelaDashboardAdmin, text="Utilizador:",bg=bg, fg="white", font=("Gilroy-Bold",30))
    lblInfo.place(x=855, y=459)

    lblUser = Label(janelaDashboardAdmin, text=nomeUtilizadorLoggedIn,bg=bg, fg="white", font=("Gilroy-Bold",19))
    lblUser.place(x=859, y=555)
    lblUserInfo = Label(janelaDashboardAdmin, text="Utilizador com sessão iniciada: ",bg=bg, fg="white", font=("Gilroy-Medium",13))
    lblUserInfo.place(x=859, y=535)

    lblRank = Label(janelaDashboardAdmin, text=rankLoggedIn,bg=bg, fg="white", font=("Gilroy-Bold",19))
    lblRank.place(x=859, y=630)
    lblRankInfo = Label(janelaDashboardAdmin, text="Rank do utilizador: ",bg=bg, fg="white", font=("Gilroy-Medium",13))
    lblRankInfo.place(x=859, y=610)

    # Função para escolher imagem para o utilizador
    def funcAbrirImagem():
        global new_pic, filename
        filename = filedialog.askopenfilename(title = "Select file",filetypes = (("all files","*.*"),("jpeg files","*.jpg"),("png files", "*.png")))
        my_pic = Image.open(filename)
        new_pic = ImageTk.PhotoImage(my_pic.resize((110, 110)))
        janelaDashboardAdmin.new_pic = new_pic
        canvas2.itemconfig(image_id, image=new_pic)
    
    #Muda o diretório da imagem e coloca-a com o mesmo nome do utilizador que a selecionou de modo a estar automaticamente ligada ao mesmo
    imageDirectory = str(pathlib.Path(__file__).parent.absolute())
    imageDirectory += "/images/users/"
    imageDirectory += nomeUtilizadorLoggedIn + ".png"

    canvas2 = Canvas(janelaDashboardAdmin,bg=bg,width=110,height=110,borderwidth=0,highlightthickness=0)
    canvas2.place(x=1197, y=525)
    my_pic = Image.open(imageDirectory)
    resized = my_pic.resize((110,110), Image.ANTIALIAS)
    new_pic = ImageTk.PhotoImage(resized)
    janelaDashboardAdmin.new_pic = new_pic
    image_id = canvas2.create_image(0, 0, anchor='nw', image=new_pic)
    #Botão com a função de escolher uma imagem
    btn4_2_img = Image.open("images\\btn4.png") 
    btn4_2_img_resized = btn4_2_img.resize((176, 26), Image.ANTIALIAS)
    btn4_2_imagem = ImageTk.PhotoImage(btn4_2_img_resized)
    janelaDashboardAdmin.btn4_2_imagem = btn4_2_imagem
    btnAvatar = Button(janelaDashboardAdmin, image = btn4_2_imagem, width = 176, height = 26, compound = CENTER,bg=bg,command=funcAbrirImagem,highlightthickness = 0, bd = 0)
    btnAvatar.place(x=1165, y=658)
    #Botão para guardar as alterações
    btn11_img = Image.open("images\\btn11.png") 
    btn11_img_resized = btn11_img.resize((216, 45), Image.ANTIALIAS)
    btn11_imagem = ImageTk.PhotoImage(btn11_img_resized)
    janelaDashboardAdmin.btn11_imagem = btn11_imagem
    btnGuardar = Button(janelaDashboardAdmin, image = btn11_imagem, width = 216, height = 45, compound = CENTER,bg=bg,command=lambda: funcBtnGuardar(imageDirectory),highlightthickness = 0, bd = 0)
    btnGuardar.place(x=1000, y=720)


# Função relacionada com a janela de notificação de tarefa
def funcJanelaNotificacaoData(count, linhaDividida):
    #Função para fechar a janela quando é acionado um botão
    def funcFechar():
        janelaNotificacaoData.destroy()
        return
    # Inicia uma janela de notificação com e título "2Du - Notificação"
    janelaNotificacaoData = Toplevel()
    janelaNotificacaoData.title("2Du - Notificação")

    # Faz com que a janela comece no centro
    w = 300
    h = 200
    ws = janelaNotificacaoData.winfo_screenwidth()
    hs = janelaNotificacaoData.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    janelaNotificacaoData.geometry("%dx%d+%d+%d" % (w, h, x, y))
    bg = "#282929"
    colorRed="#ff5454"
    janelaNotificacaoData.configure(bg=bg)
    janelaNotificacaoData.lift()
    janelaNotificacaoData.grab_set()

    aviso = Label(
        janelaNotificacaoData, text="Tem a seguinte tarefa\nplaneada para hoje: ", font=("Gilroy-Bold",17),background=bg,foreground="white", anchor="e", justify=LEFT
    )
    aviso.place(x=10, y=30)

    tarefaAviso = Label(janelaNotificacaoData, text=linhaDividida[1], font=("Gilroy-Bold",21),foreground=colorRed, background=bg,)
    tarefaAviso.place(x=10, y=90)

    ficheiro = open("tarefas.txt", "r", encoding="utf-8")
    linhas = ficheiro.readlines()
    ficheiro.close()
    ficheiro = open("tarefas.txt", "w", encoding="utf-8")
    count2 = 0
    for linha in linhas:
        if count == count2:
            linhaDividida = list(linha.split(";"))
            linhaDividida[7] = "jaNotificado"
            linha = ";".join(linhaDividida)
            ficheiro.write(linha)
        else:
            ficheiro.write(linha)
        count2 += 1
    ficheiro.close()

    btn15_img = Image.open("images\\btn15.png") 
    btn15_img_resized = btn15_img.resize((70, 32), Image.ANTIALIAS)
    btn15_imagem = ImageTk.PhotoImage(btn15_img_resized)
    janelaNotificacaoData.btn15_imagem = btn15_imagem
    btnGuardar = Button(janelaNotificacaoData, image = btn15_imagem, width = 70, height = 32, compound = CENTER,bg=bg,command=funcFechar,highlightthickness = 0, bd = 0)
    btnGuardar.place(x=13, y=142)



# Função relacionada com a janela de notificação de tarefa
def funcJanelaNotificacaoLembrete(count, linhaDividida):
    #Função para fechar a janela quando é acionado um botão
    def funcFechar():
        janelaNotificacaoLembrete.destroy()
        return
    # Inicia uma janela de notificação com e título "2Du - Notificação"
    janelaNotificacaoLembrete = Toplevel()
    janelaNotificacaoLembrete.title("2Du - Notificação")

    # Faz com que a janela comece no centro
    w = 300
    h = 200
    ws = janelaNotificacaoLembrete.winfo_screenwidth()
    hs = janelaNotificacaoLembrete.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    janelaNotificacaoLembrete.geometry("%dx%d+%d+%d" % (w, h, x, y))
    bg = "#282929"
    colorRed="#ff5454"
    janelaNotificacaoLembrete.configure(bg=bg)
    janelaNotificacaoLembrete.lift()
    janelaNotificacaoLembrete.grab_set()

    aviso = Label(
        janelaNotificacaoLembrete, text="Tem o seguinte lembrete\npara hoje: ", font=("Gilroy-Bold",17),background=bg,foreground="white", anchor="e", justify=LEFT
    )
    aviso.place(x=10, y=30)

    tarefaAviso = Label(janelaNotificacaoLembrete, text=linhaDividida[1], font=("Gilroy-Bold",21),foreground=colorRed, background=bg,)
    tarefaAviso.place(x=10, y=90)

    ficheiro = open("tarefas.txt", "r", encoding="utf-8")
    linhas = ficheiro.readlines()
    ficheiro.close()
    ficheiro = open("tarefas.txt", "w", encoding="utf-8")
    count2 = 0
    for linha in linhas:
        if count == count2:
            linhaDividida = list(linha.split(";"))
            if len(linhaDividida)==10:              #Funcionalidade que evita que as diferentes linhas do ficheiro se juntem se tiverem menos de 10 caracteres
                linhaDividida[8] = "jaNotificadoLem"
            else:
                linhaDividida[8] = "jaNotificadoLem\n"
            linha = ";".join(linhaDividida)
            ficheiro.write(linha)
        else:
            ficheiro.write(linha)
        count2 += 1
    ficheiro.close()

    btn15_img = Image.open("images\\btn15.png") 
    btn15_img_resized = btn15_img.resize((70, 32), Image.ANTIALIAS)
    btn15_imagem = ImageTk.PhotoImage(btn15_img_resized)
    janelaNotificacaoLembrete.btn15_imagem = btn15_imagem
    btnGuardar = Button(janelaNotificacaoLembrete, image = btn15_imagem, width = 70, height = 32, compound = CENTER,bg=bg,command=funcFechar,highlightthickness = 0, bd = 0)
    btnGuardar.place(x=13, y=142)

janelaInicial.mainloop()
