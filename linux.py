import json

class flush:
    _buf=""
    @classmethod
    def flush(self,msg):
        self._buf+=msg
    
    @classmethod
    def print(self):
        with open("out.py","w") as out:
            out.write(self._buf)
with open("colors.json","r") as colors:
    colordict=json.load(colors)
    # todo: iterate over every possible rgb and match with css with below article
    for key, value in colordict.items():
        r, g, b=value[0], value[1], value[2]
        flush.flush(f"""
class {key}:
    @staticmethod
    def print(msg):
        print('\\x1b[38;2;{r};{g};{b}m', end='')
        print(msg,end='')
        print('\\x1b[0m')""")
flush.print()