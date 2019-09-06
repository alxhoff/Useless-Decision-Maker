
class Option:

    def __init__(self, q_id, o_id, string):
        self.q_id = q_id
        self.id = o_id
        self.string = string


class Question:
    """A decision that has been or needs to be made
    """

    def __init__(self, q_id, string, *options):
        self.id = q_id
        self.string = string
        self.options = []
        for option in options:
            self.options.append(option)

    def addoption(self, option):
        self.options.append(option)

    def clear(self):
        self.id = None
        self.string = None
        self.options = []

    def print(self):
        print(self.string)
        for option in self.options:
            print(option)
