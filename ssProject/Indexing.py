import json
import os

from Lucene import LuceneBase
from Class import Paths as P, Paths
import lucene

def index():
    lb=LuceneBase.LuceneBase()
    #print(P.test)
    # lucene.initVM(vmargs=['-Djava.awt.headless=true'])
    #store=lb.openStore()
    #analyzer=lb.getAnalyzer()
    # writer = lb.getWriter(store, analyzer, True)
    # corpus = open(P.records, "r", encoding="utf8")

    count = 1

    for filename in os.listdir(P.test1):
        flag = 0
        print(filename)
        corpus = open(P.test1 + "/" + filename, "r", encoding="utf8")

        for line in corpus:
            d = json.loads(line)
            lb.addField(d)
            
            
        corpus.close()
    lb.closeWriter()

    #lb.searchQ()

index()