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
        print(msg)

if __name__ == '__main__':
    l = LogPrintMixin()
    l._log('A')
    print(LOG_FILE)