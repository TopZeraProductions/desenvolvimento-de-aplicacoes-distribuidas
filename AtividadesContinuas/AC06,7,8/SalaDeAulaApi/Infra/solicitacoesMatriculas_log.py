from datetime import datetime
class SolicitacaoMatriculaLog():
    def __init__(self, solicitacaoMatricula):
        self.original_data = solicitacaoMatricula.__dict__()
        self.ultima_atualizacao = solicitacaoMatricula.__dict__()
        self.start_time = datetime.now()

    def atualiza(self, solicitacaoMatricula):
        self.ultima_atualizacao = solicitacaoMatricula.__dict__()

    def finaliza_e_imprime(self):
        print(f'Mudanças iniciaram em {self.start_time}')
        print(f'Valor original:')
        print(self.original_data)
        print(f'Valor final:')
        print(self.ultima_atualizacao)
        print(f'Mudanças finalizaram em {datetime.now()}')
