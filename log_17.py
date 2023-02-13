# Abstração
# log
from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt '

class Log:
    def _log(self,msg):
        raise NotImplementedError(
            'Implemente o método log'
        )

    def log_error(self,msg):
        self._log(f'Error: {msg}')

    def log_success(self,msg):
        self._log(f'Success: {msg}')

class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')

class LogFileMixin(Log):

    def _log(self, msg):
        msg_formatada = f'{msg}({self.__class__.__name__})'
        print('Salvando no log', msg_formatada)
        with open(LOG_FILE, 'a') as arquivo:
            arquivo.write(msg_formatada)
            arquivo.write('\n')

if __name__ == '__main__':
    lp = LogPrintMixin()
    lp.log_error('Erro')
    lp.log_success('Sucesso')

    lf = LogFileMixin()
    lf.log_error('Erro')
    lf.log_success('Sucesso')