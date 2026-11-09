class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.concluida = False

    def concluir(self):
        self.concluida = True

    def resumo(self):
        if self.concluida:
            situacao = "Concluída"
        else:
            situacao = "Pendente"

        return f"{self.descricao} - {situacao}"
    
    def pendente(self):
        self.concluida=False


tarefa = Tarefa("Estudar Python")
print(tarefa.resumo())

tarefa.concluir()
print(tarefa.resumo())


pagar_luz=Tarefa("Pagar a conta")

pagar_luz.resumo()

pagar_luz.concluir()

pagar_luz.resumo()

pagar_luz.pendente()