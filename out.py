
class red:
    @staticmethod
    def print(msg):
        print('\x1b[38;2;255;0;0m', end='')
        print(msg,end='')
        print('\x1b[0m')
class green:
    @staticmethod
    def print(msg):
        print('\x1b[38;2;0;255;0m', end='')
        print(msg,end='')
        print('\x1b[0m')
class blue:
    @staticmethod
    def print(msg):
        print('\x1b[38;2;0;0;255m', end='')
        print(msg,end='')
        print('\x1b[0m')
# https://medium.com/codex/rgb-to-color-names-in-python-the-robust-way-ec4a9d97a01f