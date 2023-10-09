
import webcolors

    

def iterate(_buf):
    for r in range(256):
        for g in range(256):
            for b in range(256):
                # print(r,g,b)
                try:
                    name=webcolors.rgb_to_name((r,g,b))
                    _buf=_buf+(f"""
class {name}:
    @staticmethod
    def print(msg):
        print('\\x1b[38;2;{r};{g};{b}m', end='')
        print(msg,end='')
        print('\\x1b[0m')
    @staticmethod
    def input(prompt):
        print('\\x1b[38;2;{r};{g};{b}m', end='')
        print(prompt,end='')
        print('\\x1b[0m',end='')
        return input()""")
                    print((r,g,b),name)
                except ValueError:
                    pass
    return _buf
    # todo: iterate over every possible rgb and match with css with below article



#     for key, value in colordict.items():
#         r, g, b=value[0], value[1], value[2]

x=iterate("")
x+="""
class custom:
    def __init__(self,r,g,b):
        self.r=r
        self.g=g
        self.b=b
    def print(self,msg):
        print(f'\\x1b[38;2;{self.r};{self.g};{self.b}m', end='')
        print(msg,end='')
        print('\\x1b[0m')
    def input(self, prompt):
        print(f'\\x1b[38;2;{self.r};{self.g};{self.b}m', end='')
        print(prompt,end='')
        print('\\x1b[0m',end='')
        return input()"""

with open("out.py","w") as out:
    out.write(x)