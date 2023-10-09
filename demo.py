from pyclrout.pyclr import *
import inspect, sys

for x in inspect.getmembers(sys.modules[__name__], inspect.isclass):
    if x[0]!="custom":
        exec(f"{x[0]}.print(\"{x[0]}\")")
custom(12,34,56).print("\n\ndone")