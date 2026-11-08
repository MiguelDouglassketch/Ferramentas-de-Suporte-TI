
import platform


def mostrar_informacoes_sistema():
    print("\n===== DIAGNÓSTICO DO SISTEMA =====")

    print(f"Sistema operacional: {platform.system()}")
    print(f"Versão: {platform.release()}")
    print(f"Nome do computador: {platform.node()}")
    print(f"Arquitetura: {platform.architecture()[0]}")
    print(f"Processador: {platform.processor()}")
    print("=================================")
import platform


def mostrar_informacoes_sistema():
    print("\n===== DIAGNÓSTICO DO SISTEMA =====")

    print(f"Sistema operacional: {platform.system()}")
    print(f"Versão: {platform.release()}")
    print(f"Computador: {platform.node()}")
    print(f"Arquitetura: {platform.architecture()[0]}")
    print(f"Processador: {platform.processor()}")

    print("=================================")
