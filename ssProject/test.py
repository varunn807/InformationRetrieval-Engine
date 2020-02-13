import Query as Query
import QueryRetrieval as qr
import lucene as lucene
import json
from java.nio.file import Paths
import os
from org.apache.lucene.search import BooleanClause, IndexSearcher
from org.apache.lucene.index import DirectoryReader
from org.apache.lucene.document import Document, Field, StringField, TextField
from org.apache.lucene.analysis.standard import StandardAnalyzer
from org.apache.lucene.index import IndexWriter
from org.apache.lucene.queryparser.classic import \
    MultiFieldQueryParser, QueryParser
from org.apache.lucene.index import IndexWriterConfig
from org.apache.lucene.analysis.core import WhitespaceAnalyzer
from Class import Paths as P



# ab="medical medicine clinic general study cross coronary heart disease machine learning computer skin simple complicated new research search neural brain nuclear factor energy contain"
# auth="v"
query=Query.Query()
query.author="Florin Gorunescu"
query.mainq="$network medical medicine clinic general study cross coronary heart disease machine artificial learning computer skin simple complicated new research search neural brain nuclear factor energy contain"
# q={"mainq":"medical medicine clinic general study cross coronary heart disease machine learning computer skin simple complicated new research search neural brain nuclear factor energy contain",
#    "author":"m"}
# q["mainq"]="medical medicine clinic general study cross coronary heart disease machine learning computer skin simple complicated new research search neural brain nuclear factor energy contain"
# q["author"]="m"

q=qr.QueryRetrieval()

q.searchQ(query)



# for filename in os.listdir(P.test):
#     print(filename)
#     corpus = open(P.test+"/"+filename, "r", encoding="utf8")
#     for line in corpus:
#         d = json.loads(line)
#
#         entities = ' '.join(d['entities'])
#         abstract = (d['paperAbstract'])
#         authors = d['authors']
#         authorNames = []
#         for author in authors:
#             authorNames.append(author['name'])
#         authorNames = ' '.join(authorNames)
#
#         year = d['year']
#         url = d['s2Url']
#         id = d['id']
#         inCit = ' '.join(d['inCitations'])
#         outCit = ' '.join(d['outCitations'])
#         title = d['title']
#         venue = d['venue']
#         print(venue)

# corpus = open(P.records, "r", encoding="utf8")
# for line in corpus:
#     d = json.loads(line)
# 
#     entities = ' '.join(d['entities'])
#     abstract = (d['abstract'])
#     authors = d['authors']
#     authorNames = []
#     for author in authors:
#         authorNames.append(author['name'])
#     authorNames = ' '.join(authorNames)
# 
# 
#     year = d['year']
#     url = d['s2Url']
#     id = d['id']
#     inCit = ' '.join(d['inCitations'])
#     outCit = ' '.join(d['outCitations'])
#     title = d['title']
#     venue = d['venue']
#     print(year)
