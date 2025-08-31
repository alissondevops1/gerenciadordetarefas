import os
from idlelib.iomenu import encoding
from turtledemo.penrose import start

ARQUIVO_TAREFAS = "tarefas.txt"

def carregar_tarefas():
    """Carrega tarefas salvas no arquivo."""
    tarefas = []
    if os.path.exists(ARQUIVO_TAREFAS):
        with open(ARQUIVO_TAREFAS, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                tarefa, status = linha.strip().split(" | ")
                tarefas.append({"tarefa": tarefa, "concluída": status == "1"})
    return tarefas

def salvar_tarefas(tarefas):
    """salva as tarefas do arquivo"""
    with open(ARQUIVO_TAREFAS, "w", encoding="utf-8") as arquivo:
        for t in tarefas:
            status = "1" if t["concluída"] else "0"
            arquivo.write(f"{t['tarefa']} | {status}\n")

def adicionar_tarefa(tarefas):
    tarefa = input("Digite uma nova tarefa: ").strip()
    if tarefa:
        tarefas.append({"tarefa": tarefa, "concluída": False})
        salvar_tarefas(tarefas)
        print ("✅ Tarefa Adicionada!")
    else:
        print("⚠️ Tarefa vazia não foi adicionada.")

def listar_tarefas(tarefas):
    if tarefas:
        print("\n📑 Lista de tarefas:")
        for i, t in enumerate(tarefas, start=1):
            status = "✔️" if t["concluída"] else "❌"
            print(f"{i}. {t['tarefa']} [{status}]")
    else:
        print("\n🫙 Nenhuma tarefa.")

def marcar_concluida(tarefas):
    listar_tarefas(tarefas)
    if tarefas:
        try:
            indice = int(input("número da tarefa para marcar como concluída: "))
            if 1 <= indice <= len(tarefas):
                tarefas[indice - 1]["concluída"] = True
                salvar_tarefas(tarefas)
                print("✅ tarefa marcada como concluída! ")
            else:
                print("⚠️ Número inválido.")
        except ValueError:
            print("⚠️ Digite um número válido")

def remover_tarefa(tarefas):
    listar_tarefas(tarefas)
    if tarefas:
        try:
            indice = int(input("Número da tarefa para remover: "))
            if 1 <= indice <= len(tarefas):
                removida = tarefas.pop(indice - 1)
                salvar_tarefas(tarefas)
                print(f"🗑️ Tarefa '{removida['tarefa']}' removida!")
            else:
                print("⚠️ Número inválido.")
        except ValueError:
            print("⚠️ Digite um número válido.")

def menu():
    print("\n===== GERENCIADOR DE TAREFAS =====")
    print("1 - Adicionar tarefa")
    print("2 - Listar Tarefas")
    print("3 - Marcar Tarefa como concluída")
    print("4 - Remover Tarefa")
    print("5 - Sair")
    return input("Escolha uma opção: ")

def main():
    tarefas = carregar_tarefas()

    while True:
        opcao = menu()

        if opcao == "1":
            adicionar_tarefa(tarefas)
        elif opcao == "2":
            listar_tarefas(tarefas)
        elif opcao == "3":
            marcar_concluida(tarefas)
        elif opcao == "4":
            remover_tarefa(tarefas)
        elif opcao == "5":
            print("👋 Saindo do Programa...")
            break
        else:
            print("Opção Inválida")

if __name__ == "__main__":
    main()







