from Question import Question


class QuestionAdder:

    def __init__(self):

        self.question = Question()

    def addoption(self, string):

        self.question.options.append(string)

    def removeoption(self, string=None, index=None):

        if string:
            for i, option in enumerate(self.question.options):
                if string == option:
                    del self.question.options[i]
                    return

        if index:
            try:
                del self.question.options[index]
            except indexError:
                print("Deleting question option at index {} failed".format(index))

    def returnfinishedquestion(self):
        return self.question
