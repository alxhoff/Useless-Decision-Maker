
class Question:
    """A decision that has been or needs to be made
    """

    def __init__(self, q_id, string, *options):
        self.id = q_id
        self.string = string
        self.options = []
        for option in options:
            self.options.append(option)

    def print(self):
        print(self.string)
        for option in self.options:
            print(option)
