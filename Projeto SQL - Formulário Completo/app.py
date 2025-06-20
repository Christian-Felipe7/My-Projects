import sqlite3
import os

DATABASE_NAME = 'formulario.db'

def inicializar_db():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS formulario (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            mensagem TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
    print("Banco de dados inicializado com sucesso.")

def adicionar_registro(nome, email, mensagem):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO formulario (nome, email, mensagem) VALUES (?, ?, ?)",(nome, email, mensagem))
        conn.commit()
        print("\nRegistro adicionado com sucesso!")
    except sqlite3.Error as e:
        print(f"\nErro ao adicionar registro: {e}")
    finally:
        conn.close()

def listar_registros():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, email, mensagem FROM formulario")
    mensagens = cursor.fetchall()
    conn.close()

    if not mensagens:
        print("\nSem registros encontrados.")
        return

    print("\n--- Usuários registrados ---")
    print(f"{'ID':<4} | {'Nome':<20} | {'Email':<30} | {'Mensagem':<40}")
    print("-" * 100)

    for msg in mensagens:
        print(f"{msg[0]:<4} | {msg[1]:<20} | {msg[2]:<30} | {msg[3]:<40}")
    print("---------------------------\n")

def deletar_mensagem(id_mensagem):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM formulario WHERE id = ?", (id_mensagem,))
        if cursor.rowcount > 0:
            conn.commit()
            print(f"\nMensagem com id {id_mensagem} deletada com sucesso!")
        else:
            print(f"\nNenhuma mensagem encontrada com ID {id_mensagem}.")
    except sqlite3.Error as e:
        print(f"\nErro ao deletar mensagem {e}")
    finally:
        conn.close()

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_principal():
    inicializar_db()

    while True:
        print("\n--- Menu Principal ---")
        print("1. Adicionar novo registro")
        print("2. Listar todos os registros")
        print("3. Deletar registro por ID")
        print("4. Sair")
        escolha = input("Escolha uma opção: ")

        limpar_tela()

        if escolha == '1':
            print("\n--- Adicionar novo registro ---")
            nome = input("Nome: ")
            email = input("Email: ")
            mensagem = input("Mensagem: ")
            adicionar_registro(nome, email, mensagem)
        elif escolha == '2':
            listar_registros()
        elif escolha == '3':
            mensagem_id_str = input("Insira o ID do registro para deletá-la: ")
            try:
                id_mensagem = int(mensagem_id_str)
                deletar_mensagem(id_mensagem)
            except ValueError:
                print("\nID inválido. Por favor insira um número.")
        elif escolha == '4':
            print("Fechando aplicação...")
            break
        else:
            print("Escolha inválida. Tente novamente.")

if __name__ == "__main__":
    menu_principal()