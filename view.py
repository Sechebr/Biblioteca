import sqlite3

#conect with db
def connect():
    con = sqlite3.connect('biblioteca.db')
    return con

#function for insert new book
def addlivro(titulo, autor, editora, ano_publi):
    con = connect()
    con.execute("INSERT INTO livros(titulo, autor, editora, ano_publi)\
                 VALUES(?, ?, ?, ?)",(titulo, autor, editora, ano_publi))
    con.commit()
    con.close()

#function for insert new user
def addUser(nome, sobrenome, grupo):
    con = connect()
    con.execute("INSERT INTO usuarios(nome, sobrenome, grupo)\
                VALUES (?, ?, ?)", (nome, sobrenome, grupo))
    con.commit()
    con.close()

#function show the books
def exibirBooks():
    con = connect()
    livros = con.execute("SELECT * FROM livros").fetchall()
    con.close()

    if not livros:
        print(r'Nenhum Livro Encontrado na Biblioteca.')
        return
    else:
        print(r"Livros na Biblioteca:")
        for livro in livros:
            print(f'ID: {livro[0]}')
            print(f'titulo: {livro[1]}')
            print(f'autor: {livro[2]}')
            print(f'Editora: {livro[3]}')
            print(f'Ano de publicacao: {livro[4]}')
            print('\n')

#function for borrowing
def insertBorrowing(id_livro, id_usuario, data_emprestimo, data_devolucao):
    con = connect() 
    con.execute('INSERT INTO emprestimos(id_livro, id_usuario, data_emprestimo, data_devolucao)\
                VALUES(?, ?, ?, ?)', (id_livro, id_usuario, data_emprestimo, data_devolucao))
    con.commit()
    con.close()

#function for show book borrowing in the moment
def getBookBorrowing():
    con = connect()
    result = con.execute('SELECT livros.titulo, usuarios.nome, usuarios.sobrenome, emprestimos.id, emprestimos.data_emprestimo, emprestimos.data_devolucao\
                         FROM livros\
                         INNER JOIN emprestimos ON livros.id = emprestimos.id_livro\
                         INNER JOIN usuarios ON usuarios.id = emprestimos.id_usuario').fetchall()
    #WHERE emprestimos.data_devolucao NOT NULL
    con.close()
    if not result:
        print(r'Nenhum Livro emprestado foi Encontrado na Biblioteca.')
        return
    else:
        print("Livros na emprestados: \n")
        for livro in result:
            print(f'Titulo: {livro[0]}')
            print(f'Nome: {livro[1]}')
            print(f'Sobrenome: {livro[2]}')
            print(f'Data do emprestimo: {livro[4]}')
            print(f'Data de devolucao: {livro[5]}')
            print('\n')
    return result

#function for update status of book
def updateBorrowing(id_emprestimo, data_devolucao):
    con = connect()
    con.execute('UPDATE emprestimos SET data_devolucao = ? WHERE id = ?',(id_emprestimo, data_devolucao))
    con.commit()
    con.close()

#functio for menu
def menu():
    print('************************************ \n               MENU \n************************************')
    print('1. Adicionar livro')
    print('2. Adicionar usuario')
    print('3. Listar livros')
    print('4. Emprestar livro')
    print('5. Lista de emprestimos')
    print('6. Sair')

#Function for selection of user
def getSelection():
    return input('Selecione uma opcao: ')

#function for execute action user
def executeSelection(selection):
    if selection == '1':
        titulo = input('Titulo do livro: ')
        autor = input('Nome do autor: ')
        editora = input('Nome da editora: ')
        ano_publi = input('Ano da publicacao: ')
        addlivro(titulo, autor, editora, ano_publi)
        return True
    elif selection == '2':
        nome = input(r'Nome do Atendido: ')
        sobrenome = input(r'Sobrenome do atendido: ')
        grupo = input(r'Grupo do atendido: ')
        addUser(nome, sobrenome, grupo)
        return True
    elif selection == '3':
        exibirBooks()
        return True
    elif selection == '4':
        id_livro = int(input(r'ID do Livro para emprestimo: '))
        id_usuario = int(input(r'ID do usuario para emprestimo: '))
        data_emprestimo = input(r'Data do emprestimo, EX: AAAA-MM-DD: ')
        data_devolucao = input(r'Data para devolucao do livro EX: AAAA-MM-DD: ')
        insertBorrowing(id_livro, id_usuario, data_emprestimo, data_devolucao)
        return True
    elif selection == '5':
        getBookBorrowing()
        return True
    elif selection == '6':
        print('saindo.......')
        return False
    else:
        print('Opcao invalida, tente novamente')
        return True