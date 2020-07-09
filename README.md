### BadAtComputer
A python something that lets everybody be bad at computer.

## Usage
Import badatcomputer and watch everything go wrong.
```python
import badatcomputer
import time


class PerfectCodeException(Exception):
    """
    Exception raised when we're simply too good.
    """


try:
    raise PerfectCodeException("We're just too good!")
except PerfectCodeException as exc:
    print(f"Perfectly handled exception {exc}!")

print("Since we're so good, let's do some counting now.")
i = 0

while True:
    print(i)
    i += 1
    time.sleep(.5)

```
As you would expect, the code runs fine and nothing happens.