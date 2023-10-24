import sqlite3

# conexao de bd ou criacao de bd
con = sqlite3.connect('biblioteca.db')

#creating table books
con.execute('CREATE TABLE livros(\
            id INTEGER PRIMARY KEY,\
            titulo TEXT,\
            autor TEXT,\
            editora TEXT,\
            ano_publi INTEGER )')

#creating table user
con.execute('CREATE TABLE usuarios(\
            id INTEGER PRIMARY KEY,\
            nome TEXTE,\
            sobrenome TEXT,\
            grupo INT)')

# creating table borrowing
con.execute('CREATE TABLE emprestimos(\
            id INTEGER PRIMARY KEY,\
            id_livro INTEGER,\
            id_usuario INTEGER,\
            data_emprestimo TEXT,\
            data_devolucao TEXT,\
            FOREIGN KEY(id_livro) REFERENCES livros(id),\
            FOREIGN KEY(id_usuario) REFERENCES usuarios(id))')
