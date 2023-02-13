# Abstração
# log
class Log:
    def log(self,msg):
        raise NotImplementedError(
            'Implemente o método log'
        )

class LogFileMixin(Log):

    def log(self, msg):
        print(msg)

if __name__ == '__main__':
    l = Log()
    l.log('Alguma coisa')