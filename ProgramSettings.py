
from PyQt5.QtCore import QSettings


class ApplicationSettings(QSettings):

    def __init__(self):

        super().__init__("decision maker", "HoffSoft")

        self.setValue("testsetting", 68)
