# TeleSaúde Fácil - Sistema de Apoio a Teleconsultas

pacientes = []
agendamentos = []

def mostrar_menu():
    print("\n====== TeleSaúde Fácil ======")
    print("1. Cadastrar Paciente")
    print("2. Listar Pacientes")
    print("3. Agendar Teleconsulta")
    print("4. Ver Agendamentos")
    print("5. Ajuda")
    print("0. Sair")

def cadastrar_paciente():
    nome = input("Nome: ").strip()
    idade = input("Idade: ").strip()
    telefone = input("Telefone: ").strip()
    if nome and idade.isdigit() and telefone:
        pacientes.append({"nome": nome, "idade": int(idade), "telefone": telefone})
        print("Paciente cadastrado com sucesso!")
    else:
        print("Dados inválidos. Tente novamente.")

def listar_pacientes():
    if not pacientes:
        print("Nenhum paciente cadastrado.")
    else:
        for i, p in enumerate(pacientes, 1):
            print(f"{i}. {p['nome']} - {p['idade']} anos - {p['telefone']}")

def agendar_teleconsulta():
    if not pacientes:
        print("Cadastre ao menos um paciente antes.")
        return
    listar_pacientes()
    escolha = input("Escolha o número do paciente: ").strip()
    if escolha.isdigit() and 1 <= int(escolha) <= len(pacientes):
        paciente = pacientes[int(escolha) - 1]
        data = input("Data (dd/mm/aaaa): ").strip()
        hora = input("Hora (hh:mm): ").strip()
        agendamentos.append({"paciente": paciente["nome"], "data": data, "hora": hora})
        print("Teleconsulta agendada com sucesso!")
    else:
        print("Escolha inválida.")

def ver_agendamentos():
    if not agendamentos:
        print("Nenhum agendamento encontrado.")
    else:
        for ag in agendamentos:
            print(f"{ag['paciente']} - {ag['data']} às {ag['hora']}")

def ajuda():
    print("\nAjuda - Como usar o sistema:")
    print("1. Cadastre pacientes com nome, idade e telefone.")
    print("2. Agende teleconsultas após cadastrar.")
    print("3. Use a opção de ajuda para lembrar os passos.")
    print("4. Volte sempre ao menu após cada ação.")

def main():
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ").strip()
        if opcao == "1":
            cadastrar_paciente()
        elif opcao == "2":
            listar_pacientes()
        elif opcao == "3":
            agendar_teleconsulta()
        elif opcao == "4":
            ver_agendamentos()
        elif opcao == "5":
            ajuda()
        elif opcao == "0":
            print("Encerrando...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
