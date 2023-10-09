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