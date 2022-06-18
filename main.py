import datetime

class Ponto():

    def __init__(self):
        pass

    def relogio(self):
        relogio = []
        hojee = datetime.datetime.now()
        hoje = hojee.strftime("%d/""%m/""%Y ""%H:""%M")
        self.rr = relogio
        self.rr.append(hoje)
        return self.confirmarregistro()


    def registrar(self):
        Re = input('Registro de ação:(Sim/Não)')
        if Re == 'Sim':
            self.relogio()
        elif Re == 'Não':
            self.fechar()
        else:
            print('Digite apenas Sim ou Não')
            return self.registrar()

    def confirmarregistro(self):
        print(self.rr,'Data Registrada')
        return self.permanecer()

    def permanecer(self):
        print('Me avise quando desejar registrar mais uma ação, digitando: (Ação)')
        Perm = input()
        if Perm == 'Ação':
            self.registrar()
        else:
            print('Digite Ação e não o nome do seu cão')

        pass

    def fechar(self):
        Fe = input('Deseja sair:(Sim/Não)')
        if Fe == 'Não':
            self.permanecer()
        elif Fe == 'Sim':
            print('Obrigado por mais um dia de trabalho')
        else:
            print('Digite apenas Sim ou Não')
        pass

x = Ponto()

x.registrar()
