import customtkinter as ctk
from tkinter import messagebox
import os
import pyttsx3

# Inicializa o motor de voz
engine = pyttsx3.init()

# Tema
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Hospital das Clínicas - Teleconsulta")
app.geometry("750x720")

# Lista de agendamentos
agendamentos = []

def formatar_agendamento(agendamento):
    return (f"👤 Nome: {agendamento['nome']}\n"
            f"📞 Telefone: {agendamento['telefone']}\n"
            f"🏥 Especialidade: {agendamento['especialidade']}\n"
            f"🗓️ Horário: {agendamento['horario']}\n")

# Assistente de Voz passo a passo com dropdown para especialidade
class AssistenteVoz:
    def __init__(self, master):
        self.master = master
        self.master.title("Assistente de Voz - Teleconsulta")
        self.master.geometry("600x450")

        self.especialidades = [
            "Clínico Geral", "Psicólogo", "Cardiologista", "Endocrinologista",
            "Ortopedista", "Dermatologista", "Ginecologista", "Neurologista"
        ]

        self.passos = [
            ("Digite seu nome completo:", "nome"),
            ("Digite seu telefone com WhatsApp:", "telefone"),
            ("Escolha a especialidade médica:", "especialidade"),
            ("Informe o melhor dia e horário:", "horario")
        ]
        self.valores = {}
        self.index = 0

        self.label_instrucao = ctk.CTkLabel(master, text="", font=("Helvetica", 18))
        self.label_instrucao.pack(pady=20)

        self.input_entry = ctk.CTkEntry(master, width=400, font=("Helvetica", 16))
        self.optionmenu = None

        self.botao_proximo = ctk.CTkButton(master, text="Próximo", command=self.avancar,
                                           fg_color="#87CEFA", hover_color="#00BFFF", font=("Helvetica", 16))
        self.botao_proximo.pack(pady=10)

        self.falar_passos()

    def falar_passos(self):
        self.label_instrucao.configure(text=self.passos[self.index][0])
        engine.say(self.passos[self.index][0])
        engine.runAndWait()

        if self.passos[self.index][1] == "especialidade":
            self.input_entry.pack_forget()
            if not self.optionmenu:
                self.optionmenu_var = ctk.StringVar(value=self.especialidades[0])
                self.optionmenu = ctk.CTkOptionMenu(self.master, values=self.especialidades,
                                                   variable=self.optionmenu_var, width=400, font=("Helvetica", 16))
                self.optionmenu.pack(pady=10)
        else:
            if self.optionmenu:
                self.optionmenu.pack_forget()
            self.input_entry.pack(pady=10)

    def avancar(self):
        campo = self.passos[self.index][1]

        if campo == "especialidade":
            resposta = self.optionmenu_var.get()
        else:
            resposta = self.input_entry.get().strip()

        if not resposta:
            messagebox.showwarning("Aviso", "Por favor, preencha o campo antes de avançar.")
            engine.say("Por favor, preencha o campo antes de avançar.")
            engine.runAndWait()
            return

        self.valores[campo] = resposta
        self.index += 1
        self.input_entry.delete(0, 'end')

        if self.index == len(self.passos):
            resumo = "\n".join(f"{k.capitalize()}: {v}" for k, v in self.valores.items())
            mensagem = "Confirme seus dados:\n\n" + resumo
            self.label_instrucao.configure(text="Confirme seus dados no pop-up?")
            engine.say("Confirme seus dados no pop-up")
            engine.runAndWait()

            if messagebox.askyesno("Confirmação", mensagem):
                engine.say("Agendamento confirmado. Você receberá lembretes no WhatsApp.")
                engine.runAndWait()
                messagebox.showinfo("Sucesso", "Agendamento confirmado!")
                agendamentos.append(self.valores)
                self.master.destroy()
            else:
                self.index = 0
                self.valores = {}
                self.falar_passos()
        else:
            self.falar_passos()

def marcar_teleconsulta():
    janela = ctk.CTkToplevel(app)
    janela.title("Agendar Teleconsulta")
    janela.geometry("600x600")

    ctk.CTkLabel(janela, text="📋 Formulário de Agendamento", font=("Helvetica", 22, "bold")).pack(pady=20)

    campos = [
        ("Nome completo:", "nome_entry"),
        ("Número de telefone (WhatsApp):", "telefone_entry"),
        ("Melhor dia e horário:", "horario_entry")
    ]

    entradas = {}
    for label, key in campos:
        ctk.CTkLabel(janela, text=label, font=("Helvetica", 16), anchor="w").pack(anchor="w", padx=40)
        entradas[key] = ctk.CTkEntry(janela, width=450, height=40, font=("Helvetica", 15))
        entradas[key].pack(pady=5)

    ctk.CTkLabel(janela, text="Especialidade médica:", font=("Helvetica", 16), anchor="w").pack(anchor="w", padx=40)
    especialidades = [
        "Clínico Geral", "Psicólogo", "Cardiologista", "Endocrinologista",
        "Ortopedista", "Dermatologista", "Ginecologista", "Neurologista"
    ]
    especialidade_var = ctk.StringVar(value=especialidades[0])
    especialidade_menu = ctk.CTkOptionMenu(janela, values=especialidades, variable=especialidade_var,
                                           width=450, height=40, font=("Helvetica", 15))
    especialidade_menu.pack(pady=5)

    def confirmar_agendamento():
        nome = entradas["nome_entry"].get().strip()
        telefone = entradas["telefone_entry"].get().strip()
        horario = entradas["horario_entry"].get().strip()
        especialidade = especialidade_var.get()

        if not nome or not telefone or not horario:
            messagebox.showwarning("Aviso", "Por favor, preencha todos os campos.")
            return

        if messagebox.askyesno("Confirmar", f"Confirma os dados?\n\n{nome}, {telefone}, {especialidade}, {horario}"):
            novo = {"nome": nome, "telefone": telefone, "especialidade": especialidade, "horario": horario}
            agendamentos.append(novo)
            messagebox.showinfo("Sucesso", formatar_agendamento(novo))
            janela.destroy()

    ctk.CTkButton(janela, text="✅ Confirmar Agendamento", command=confirmar_agendamento,
                  fg_color="#87CEFA", hover_color="#00BFFF",
                  font=("Helvetica", 18), height=50, width=300, corner_radius=12).pack(pady=30)

def video_tutorial():
    try:
        os.startfile(os.path.abspath("video_tutorial.mp4"))
    except:
        messagebox.showerror("Erro", "Vídeo não encontrado.")

def audio_tutorial():
    try:
        os.startfile(os.path.abspath("audio_tutorial.mp3"))
    except:
        messagebox.showerror("Erro", "Áudio não encontrado.")

def mostrar_integrantes():
    integrantes = (
        "👥 Equipe:\n\n"
        "• Murillo – RM: 564969\n"
        "• Leonardo Zerbinatti – RM: 562992\n"
        "• Gustavo Mendes da Rosa Moreira"
    )
    messagebox.showinfo("Integrantes", integrantes)

def mostrar_agendamentos():
    if not agendamentos:
        messagebox.showinfo("Agendamentos", "Nenhum agendamento feito.")
        return
    texto = "📋 Agendamentos:\n\n"
    for i, ag in enumerate(agendamentos, 1):
        texto += f"{i}º:\n{formatar_agendamento(ag)}\n"
    messagebox.showinfo("Lista", texto)

def filtrar_por_especialidade():
    if not agendamentos:
        messagebox.showinfo("Filtro", "Nenhum agendamento ainda.")
        return
    especialidades = sorted(set(ag["especialidade"] for ag in agendamentos))
    if not especialidades:
        messagebox.showinfo("Filtro", "Nenhuma especialidade encontrada nos agendamentos.")
        return

    janela = ctk.CTkToplevel(app)
    janela.title("Filtrar por Especialidade")
    janela.geometry("400x300")

    ctk.CTkLabel(janela, text="Escolha uma especialidade:", font=("Helvetica", 16)).pack(pady=15)
    esp_var = ctk.StringVar(value=especialidades[0])
    ctk.CTkOptionMenu(janela, values=especialidades, variable=esp_var).pack(pady=10)

    def mostrar_filtrados():
        sel = esp_var.get()
        filtrados = [a for a in agendamentos if a["especialidade"] == sel]
        if filtrados:
            msg = f"📂 {sel}:\n\n"
            for i, a in enumerate(filtrados, 1):
                msg += f"{i}. {a['nome']} - {a['horario']}\n"
        else:
            msg = f"Nenhum agendamento encontrado para {sel}."
        messagebox.showinfo("Resultado", msg)
        janela.destroy()

    ctk.CTkButton(janela, text="🔍 Mostrar", command=mostrar_filtrados,
                  fg_color="#87CEFA", hover_color="#00BFFF").pack(pady=20)

usar_assistente_voz = ctk.BooleanVar(value=False)

def abrir_teleconsulta():
    if usar_assistente_voz.get():
        AssistenteVoz(ctk.CTkToplevel(app))
    else:
        marcar_teleconsulta()

# Menu Principal
ctk.CTkLabel(app, text="🏥 Hospital das Clínicas - Teleconsulta", font=("Helvetica", 28, "bold"),
             text_color="#1a5276").pack(pady=30)
ctk.CTkLabel(app, text="Escolha uma opção:", font=("Helvetica", 17), text_color="#2c3e50").pack(pady=10)

ctk.CTkCheckBox(app, text="Usar Assistente de Voz", variable=usar_assistente_voz,
                font=("Helvetica", 15)).pack(pady=(0,10))

botoes = [
    ("📅 Marcar Teleconsulta", abrir_teleconsulta),
    ("📋 Ver Agendamentos", mostrar_agendamentos),
    ("🔍 Filtrar por Especialidade", filtrar_por_especialidade),
    ("🎥 Ver Vídeo Tutorial", video_tutorial),
    ("🔊 Ouvir Áudio Tutorial", audio_tutorial),
    ("👥 Ver Integrantes", mostrar_integrantes)
]

for texto, comando in botoes:
    ctk.CTkButton(app, text=texto, command=comando,
                  fg_color="#87CEFA", hover_color="#00BFFF",
                  width=400, height=55, font=("Helvetica", 18), corner_radius=12).pack(pady=8)

ctk.CTkLabel(app, text="Desenvolvido para o CHALLENGE - 1TDSPH - 1ª Sprint - 2025",
             font=("Helvetica", 13), text_color="#7f8c8d").pack(pady=20)

app.mainloop()
