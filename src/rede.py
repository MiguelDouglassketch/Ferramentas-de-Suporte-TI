import socket


def testar_conexao_internet():
    print("\n===== TESTE DE CONEXÃO =====")

    try:
        conexao = socket.create_connection(
            ("www.google.com", 443),
            timeout=5
        )

        conexao.close()

        print("Conexão com a internet: CONECTADO!")

    except OSError:
        print("Conexão com a internet: SEM CONEXÃO!")

    print("============================")
