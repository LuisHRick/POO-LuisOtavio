# Abstração
# log
class Log:
    def _log(self,msg):
        raise NotImplementedError(
            'Implemente o método log'
        )

    def log_error(self,msg):
        self._log(f'Error: {msg}')

    def log_success(self,msg):
        self._log(f'Success: {msg}')


class LogFileMixin(Log):

    def _log(self, msg):
        print(msg)

if __name__ == '__main__':
    l = Log()
    l.log('Alguma coisa')