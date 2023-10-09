## Pyclr
### Does one thing badly
## Installation
```bash
python linux.py
cd pyclrout
pip install . # may need --break-system-packages
cd ../
python demo.py
```
## Usage
```py
from pyclr import *

palegreen.print("hello") # can be any valid css color

# or

custom(12,34,56).print("I'm special!") # custom rgb values

blueinput=blue.input("I'm in blue!")
print(blueinput) # not blue
```
## Build
```bash
python linux.py # caution: slow
# took 1m02 on my machine (i5-11400F, 32GB RAM)
```