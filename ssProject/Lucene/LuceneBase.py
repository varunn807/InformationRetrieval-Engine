import sys, lucene, unittest
import os, shutil
import operator
from itertools import islice
import ssProject.Document as d
from nltk.stem import PorterStemmer
from ssProject.Class import Paths as myPaths

from java.io import StringReader
from java.nio.file import Path, Paths
from org.apache.lucene.analysis.core import WhitespaceAnalyzer
from org.apache.lucene.analysis.miscellaneous import LimitTokenCountAnalyzer
from org.apache.lucene.analysis.standard import StandardAnalyzer
from org.apache.lucene.document import \
    Document, Field, StoredField, StringField, TextField
from org.apache.lucene.index import \
    IndexOptions, IndexWriter, IndexWriterConfig, DirectoryReader, \
    MultiFields, Term
from org.apache.lucene.queryparser.classic import \
    MultiFieldQueryParser, QueryParser
from org.apache.lucene.search import BooleanClause, IndexSearcher, TermQuery,BooleanQuery,BoostQuery
from org.apache.lucene.store import MMapDirectory, SimpleFSDirectory
from whoosh.lang.wordnet import Thesaurus




class LuceneBase:

    def __init__(self):
        print("===============")
        print(lucene.getVMEnv())
        if lucene.getVMEnv() == None:
            lucene.initVM(vmargs=['-Djava.awt.headless=true'])
            #lucene.initVM(lucene.CLASSPATH)
        else:
            lucene.getVMEnv().attachCurrentThread()

        # lucene.initVM(vmargs=['-Djava.awt.headless=true'])
        #self.wr = self.getWriter(self.openStore(), self.getAnalyzer(), True)

        self.ccounter = 0
        self.mcounter = 0
        self.stpFile = open(myPaths.StopwordDir, "r", encoding="utf8");
        self.stopList = self.stpFile.read().splitlines();
        return

    def initVM(self):
        lucene.initVM(vmargs=['-Djava.awt.headless=true'])
        self.wr = self.getWriter(self.openStore(), self.getAnalyzer(), True)

    def addField(self, d):

        doc = self.getDocument()
        doc.add(Field("entities", ' '.join(d['entities']), TextField.TYPE_STORED))

        doc.add(Field("abstract", (d['paperAbstract']), TextField.TYPE_STORED))
        #doc.add(Field("pageRankScore", (str(d['pageRankScore'])), TextField.TYPE_STORED))

        authors = d['authors']
        authorNames = []
        for author in authors:
            authorNames.append(author['name'])
        authorNames = ' '.join(authorNames)

        doc.add(Field("authorName", authorNames, TextField.TYPE_STORED))

        doc.add(Field("title", d['title'], TextField.TYPE_STORED))
        # if 'year' in d.keys():
        #     year=d['year']

        #
        #doc.add(Field("s2Url", d['s2Url'],
                      #StringField.TYPE_STORED))
        doc.add(Field("id", d['id'],
                      StringField.TYPE_STORED))
        doc.add(Field("inCitations", ' '.join(d['inCitations']),
                      TextField.TYPE_STORED))
        doc.add(Field("outCitations", ' '.join(d['outCitations']),
                      TextField.TYPE_STORED))
        doc.add(Field("venue", d['venue'], StringField.TYPE_STORED))
        doc.add(Field("url", d["s2Url"], StringField.TYPE_STORED))
        doc.add(Field("journalName", d["journalName"], StringField.TYPE_STORED))




        self.wr.addDocument(doc)
        doc = None
        self.ccounter += 1
        # if (self.ccounter % 100000 == 0):
        #     self.ccounter = 0
        #     self.mcounter += 1
        #     print(self.mcounter)
        # if (self.ccounter == 1000):
        #     self.ccounter = 0
        #     return 1
        return 1

    def closeWriter(self):
        self.wr.commit()
        self.wr.close()

    def searchQ(self,query):
        ps=PorterStemmer()
        # qboosto=BoostQuery.BoostQuery()
        f = open("C:/Users/Tigmanshu/Documents/IRWeb/ssProject/Lucene/wn_s.pl")
        t = Thesaurus.from_file(f)
        # print(t.synonyms("regression"))
        result = []
        qList=query.mainq.lower().split()
        checkList=[]
        notQ=""
        mustQ=""
        shouldQ=""
        for qt in qList:
            if qt[0]=='!':
                notQ=notQ+" "+qt[1:len(qt)]
                # checkList.append(qt[1:len(qt)])
            elif qt[0]=='$':
                mustQ = mustQ + " " + qt[1:len(qt)]
                checkList.append(ps.stem(qt[1:len(qt)]))
            else:
                shouldQ=shouldQ + " " + qt
                thes=t.synonyms(qt)
                i=0
                for term in thes:
                    if i==5:
                        break
                    shouldQ = shouldQ + " " + term
                    i+=1
                checkList.append(ps.stem(qt))
        del qList
        self.stopList="a an the of is zero".split()
        searcher = IndexSearcher(DirectoryReader.open(self.openStore()))
        analyzer = StandardAnalyzer()
        # q1 = QueryParser("abstract", analyzer).parse(shouldQ)
        # q2 = QueryParser("entities", analyzer).parse(shouldQ)
        # q3 = QueryParser("abstract", analyzer).parse(mustQ)
        # q4 = QueryParser("entities", analyzer).parse(mustQ)
        # q5 = QueryParser("abstract", analyzer).parse(notQ)
        # q6 = QueryParser("entities", analyzer).parse(notQ)




        b1 = BooleanQuery.Builder()
        if len(shouldQ)>0:
            q1 = QueryParser("abstract", analyzer).parse(shouldQ)
            q2 = QueryParser("entities", analyzer).parse(shouldQ)
            # q1.setBoost(2)
            b1.add(q1, BooleanClause.Occur.SHOULD)
            b1.add(q2, BooleanClause.Occur.SHOULD)
        if len(mustQ)>0:
            q3 = QueryParser("abstract", analyzer).parse(mustQ)
            q4 = QueryParser("entities", analyzer).parse(mustQ)
            b1.add(q3, BooleanClause.Occur.MUST)
            b1.add(q4, BooleanClause.Occur.MUST)
        if len(notQ)>0:
            q5 = QueryParser("abstract", analyzer).parse(notQ)
            q6 = QueryParser("entities", analyzer).parse(notQ)
            b1.add(q5, BooleanClause.Occur.MUST_NOT)
            b1.add(q6, BooleanClause.Occur.MUST_NOT)

        if len(query.journal)>0:
            print("$$$$$")
            print(query.journal)
            q7 = QueryParser("journalName", analyzer).parse(query.journal)
            b1.add(q7, BooleanClause.Occur.SHOULD)
        if len(query.author)>0:
            q8 = QueryParser("authorName", analyzer).parse(query.author)
            b1.add(q8, BooleanClause.Occur.SHOULD)
        bq1 = b1.build()

        #print(bq1)
        topDocs = searcher.search(bq1, 100)
        scoreDocs = topDocs.scoreDocs
        #print(len(scoreDocs))
        entitiesHitList = {}
        for i in scoreDocs:
            myDoc= d.Document()
            doc = searcher.doc(i.doc)
            # print(doc.get("id"), i)
            # print(doc.get("abstract"))
            # print(doc.get("authorName"))

            for entity in doc.get("entities").split():
                entity=entity.lower()
                if ps.stem(entity) in checkList:
                    continue
                if entity in self.stopList:
                    continue
                if entity in entitiesHitList:
                    entitiesHitList[entity] += 1
                else:
                    entitiesHitList[entity] = 1
            myDoc.setDocTitle(doc.get("title"))
            myDoc.setAbstract(doc.get("abstract"))
            myDoc.setJournal(doc.get("journalName"))
            myDoc.setAuthor(doc.get("authorName"))
            myDoc.setURL(doc.get("url"))
            result.append(myDoc)
        sorted_d = sorted(entitiesHitList.items(), key=operator.itemgetter(1), reverse=True)
        del entitiesHitList
        n_items = dict(islice(sorted_d , 10))
        del sorted_d
        return {"res":result,"sug":n_items,"query":query}

    # def search(self,query):
    #     searcher = IndexSearcher(DirectoryReader.open(self.openStore()))
    #     analyzer = StandardAnalyzer()
    #     query = QueryParser("paperAbstract", analyzer).parse(query)
    #     topDocs = searcher.search(query, 100)
    #     return topDocs

    def getDocument(self):
        doc = Document()
        return doc
        # return

    def getField(self):
        return Field()

    def getStringField(self):
        return StringField()

    def getTextField(self):
        return TextField()

    def getAnalyzer(self):
        return StandardAnalyzer()

    def openStore(self):
        INDEX_DIR = "projectIndexFiles.index"
        path1 = "D:/IR Dataset/"
        base_dir = os.path.dirname(os.path.abspath(path1))
        storeDir = os.path.join(base_dir, INDEX_DIR)
        store = SimpleFSDirectory(Paths.get(storeDir))
        return store

    def closeStore(self, store, *args):
        pass

    def getWriter(self, store, analyzer=None, create=False):
        if analyzer is None:
            analyzer = StandardAnalyzer()
        config = IndexWriterConfig(analyzer)
        config.setOpenMode(IndexWriterConfig.OpenMode.CREATE)
        writer = IndexWriter(store, config)
        return writer

    def getReader(self, store, analyzer):
        pass

    def getSearcher(self, store):
        return IndexSearcher(DirectoryReader.open(store))