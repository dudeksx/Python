

class Usuario:
    def __init__(self, nome) -> None:

        self.nome = nome
        self.falhas = 0
        self.bloqueado = False

        pass

    def registra_falha(self):

        self.falhas += 1
        self.bloqueado = self.falhas >= 3
        pass


class validaAcesso:

    def __init__(self) -> None:

        self.base_usuarios = {}
        pass

    def monitora_tentativa(self, nome, status):

        if nome not in self.base_usuarios:
            self.base_usuarios[nome] = Usuario(nome)

        if status == "falha":
            self.base_usuarios[nome].registra_falha()

    def acessa_log(self):
        with open("log.txt", "r") as arquivo:
            for linha in arquivo:
                chave, valor = linha.strip().split(",", 1)
                self.monitora_tentativa(chave, valor)
                self.exporta_bloqueados()

    def exporta_bloqueados(self):
        with open("bloqueados.txt", "w", encoding="utf-8") as arquivo_bloqueados:
            for i in self.base_usuarios.values():
                if i.bloqueado:
                    arquivo_bloqueados.write(
                        f"Usuário: {i.nome} | Falhas: {i.falhas} | Status: BLOQUEADO\n")


acesso_usuario = validaAcesso()

acesso_usuario.acessa_log()

print("--- RELATÓRIO DE SEGURANÇA ---")
for nome, obj_usuario in acesso_usuario.base_usuarios.items():
    status = "BLOQUEADO" if obj_usuario.bloqueado else "Ativo"
    print(
        f"Usuário: {nome:10} | Falhas: {obj_usuario.falhas} | Status: {status}")
