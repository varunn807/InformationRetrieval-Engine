class Document:

    def __init__(self):
        return

    docid = ""
    title = ""
    score = 0.0
    abstract=""
    journal=""
    url=""
    author =""


    def getDocId(self):
        return self.docid

    def getURL(self):
        return self.url

    def getDocTitle(self):
        return self.docno

    def getScore(self):
        return self.score
    def getAbstract(self):
        return self.abstract
    def getJournal(self):
        return self.journal
    def detAuthor(self):
        return self.author

    def setDocId(self, docid):
        self.docid = docid

    def setDocTitle(self, title):
        self.title = title

    def setURL(self,url):
        self.url=url

    def setScore(self, the_score):
        self.score = the_score
    def setAbstract(self, abstract):
        self.abstract = abstract
    def setJournal(self, journal):
        self.journal = journal
    def setAuthor(self, author):
        self.author=author