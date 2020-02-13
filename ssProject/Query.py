class Query:

    def __init__(self):
        return

    mainq = ""
    journal = ""

    author=""




    def getmain(self):
        return self.mainq

    def getjournal(self):
        return self.journal

    def getauth(self):
        return self.author

    def setmain(self, mainq):
        self.mainq = mainq

    def setauth(self, auth):
        self.author = auth

    def setjournal(self, journal):
        self.journal = journal
