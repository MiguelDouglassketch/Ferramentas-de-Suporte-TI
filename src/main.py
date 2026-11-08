from sistema import mostrar_informacoes_sistema
from rede import testar_conexao_internet


def main():
    print("================================")
    print("       FERRAMENTAS DE TI")
    print("================================")

    print("Bem-vindo ao sistema de suporte!")

    mostrar_informacoes_sistema()
    testar_conexao_internet()

    print("\nDiagnóstico finalizado!")


if __name__ == "__main__":
    main()
