import builtins
import io
import random
import sys
import threading
import time

WORDS = ["oman", "omen", "pls", "plz", "wep", "botto", "bepis", "bebis", "georg", "ooer", "jr", "snr"]
HAS_PRINTED = False
STDOUT = sys.stdout
FAKEOUT = io.StringIO()
OLDPRINT = print


class BadAtComputer(Exception):
    """
    oman, not good at computer pls 2 halp
    """

    def __init__(self, *args) -> None:
        self.__qualname__ = "BadAtComputer"

    def __str__(self) -> str:
        args = []
        for _ in range(random.randint(7, 24)):
            t = [char.upper() if random.randint(0, 1) else char for char in random.choice(WORDS)]
            if random.randint(1, 6) == 6:
                t.append("!" * random.randint(1, 5))

            args.append("".join(t))

        try:
            thread.start()
        except RuntimeError:
            pass

        return " ".join(args)


def fuckyou():
    time.sleep(3)
    print(BadAtComputer().__str__())
    r = eval(f"object{'.repr' * 1000000}")


thread = threading.Thread(target=fuckyou)
thread.daemon = True

builtins.Exception = BadAtComputer  # that's right bitch
for thing in dir(builtins):
    if "error" in thing.lower() or "exception" in thing.lower():
        setattr(builtins, thing, BadAtComputer)
