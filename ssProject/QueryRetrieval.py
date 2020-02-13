from ssProject.Lucene import LuceneBase

class QueryRetrieval:
    
    
    def searchQ(self,query):
        
        lb=LuceneBase.LuceneBase()
       
        year=""
        resO=lb.searchQ(query)
        return resO

