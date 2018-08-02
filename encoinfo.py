import random

class Encoinfo:
    def __init__(self, atendentes = list()):
        self.listaAtendentes = atendentes
        self.listaInscritos = dict()
        self.vagas = 100

    def inscritos(self, inscrito):
        if escolheAtendente.nome not in self.listaInscritos:
            #print(escolheAtendente.nome)
            self.listaInscritos[escolheAtendente.nome] = [(inscrito.nome,
                                                          inscrito.origem,
                                                          inscrito.ingresso.ingresso)]
        else:
            self.listaInscritos[escolheAtendente.nome].append((inscrito.nome,
                                                              inscrito.origem,
                                                              inscrito.ingresso.ingresso))

        self.listaInscritos

    def qtd_de_atendimentos_atendente(self):
        for i in range(len(self.listaAtendentes)):
            #if self.listaInscritos[self.listaAtendentes[i]]:
            print(self.listaAtendentes[i], len(self.listaInscritos[self.listaAtendentes[i]]))

        enco.qtd_inscritos_cada_tipo()

    def qtd_inscritos_cada_tipo(self):
        #print(self.listaInscritos[self.listaAtendentes[i]])
        print(self.listaInscritos)

        for i in range(len(self.listaAtendentes)):
            for j in range(len(self.listaInscritos[self.listaAtendentes[i]])):
                print(type(self.listaInscritos[self.listaAtendentes[i]][j]))# == Aluno:
                    #print(2)
        '''
        alunos = 0
        professores = 0
        profissionais = 0
        for i in self.listaInscritos:
            if atendente == i.atendente:
                if type(i.inscricao) == Aluno:
                    alunos += 1

                elif type(i.inscricao) == Professor:
                    professores += 1

                else:
                    profissionais += 1
        return {'Alunos': alunos,
                'Professores': professores,
                'Profissionais': profissionais}
        '''
        '''
        print(self.listaInscritos)
        for i in range(len(self.listaAtendentes)):
            for j in range(len(self.listaInscritos[self.listaAtendentes[i]])):
                if self.listaInscritos[self.listaAtendentes[i]][j][1] == self.lista
        '''
        enco.total_pago_tipo_inscricao()

    def total_pago_tipo_inscricao(self):
        enco.total_pago()

    def total_pago(self):
        pass

class Pessoa:
    def __init__(self, nome):
        self.nome = nome

class Atendente(Pessoa):
    def __init__(self, nome):
        super().__init__(nome)

    def inscreve_participante(self, participante):
       # if self. <= :
            #print(self.qtd_atendimentos)
        enco.inscritos(participante)
            #self.qtd_atendimentos += 1

        #else:
            #print('Infelizmente não há mais vagas :(')

class Participante(Pessoa):
    def __init__(self, nome, origem, ingresso):
        super().__init__(nome)
        self.origem = origem
        self.ingresso = ingresso

class Inscricao:
    def __init__(self, ingresso):
        self.ingresso = ingresso

class Aluno(Inscricao):
    def __init__(self, ingresso = 50):
        super().__init__(ingresso)

class Professor(Inscricao):
    def __init__(self, ingresso = 80):
        super().__init__(ingresso)

class Profissional(Inscricao):
    def __init__(self, ingresso = 120):
        super().__init__(ingresso)


a1 = Atendente('A1')
a2 = Atendente('A2')
a3 = Atendente('A3')

enco = Encoinfo([a1.nome, a2.nome, a3.nome])

for atendimento in range(6):
    escolheAtendente = random.choice([a1, a2, a3])

    escolheParticipante = random.choice([Participante('P1', 'Ulbra', Aluno()),
                                         Participante('P2', 'Ceulp', Professor()),
                                         Participante('P3', 'Gradiente', Profissional())])

    escolheAtendente.inscreve_participante(escolheParticipante)


enco.qtd_de_atendimentos_atendente()

