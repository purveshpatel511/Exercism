import random
import string

# set of all generated names
NAMES = set()


class Robot:

    name = None

    def reset(self):
        self.name = None
        self.check_name()

    def generate_name(self):
        _alpha = "".join(random.choice(string.ascii_uppercase) for _ in range(2))
        _num = "".join(random.choice(string.digits) for _ in range(3))
        return _alpha + _num

    def check_name(self):
        while self.name == None or self.name in NAMES:
            self.name = self.generate_name()
        NAMES.add(self.name)

    def __init__(self):
        self.check_name()
        pass
