from django.shortcuts import render
from AlgoHITS_PR import run

from ssProject import QueryRetrieval,Query
# Create your views here.
from django.http import HttpResponse
from django.template import loader
import lucene

myQuery=Query.Query()
def homepage(request):

    # vm=lucene.getVMEnv()
    # vm.attachCurrentThread()
    template = loader.get_template('IRapp/index4.html')
    context = { }

    return HttpResponse(template.render(context,request))

def test(request):

    #print("in test func")
    # print(request.POST['query'])
    #myQuery.mainq=myQuery.mainq+"HEllo"
    #print(myQuery.mainq)

    for x in request.POST :
        if x != "csrfmiddlewaretoken":
            myQuery.mainq = myQuery.mainq +" " +request.POST[x]
            #print(request.POST[x])
    query_ret_obj = QueryRetrieval.QueryRetrieval()
    result_obj = query_ret_obj.searchQ(myQuery)
    list_of_res = result_obj['res']
    dict_of_sugg = result_obj['sug']
    # myQuery.setmain(request.POST['query'])
    # myQuery.setjournal(request.POST['journal'])
    # myQuery.setauth(request.POST['author'])
    # print(type(dict_of_sugg))
    list_names = list(dict_of_sugg.keys())
    template = loader.get_template('IRapp/category.html')
    context = {'list_of_res': list_of_res, 'list_names': list_names,'query_str':myQuery.getmain() }
    return HttpResponse(template.render(context, request))


def index(request):
    if request.method == 'POST':
        #print(request.POST['query'])
        #obj_run=run.run()
        obj_query=Query.Query()
        query_str=request.POST['query']
        obj_query.setmain(request.POST['query'])
        obj_query.setauth(request.POST['author'])
        obj_query.setjournal(request.POST['journal'])
        query_ret_obj=QueryRetrieval.QueryRetrieval()
        result_obj=query_ret_obj.searchQ(obj_query)
        list_of_res=result_obj['res']
        dict_of_sugg = result_obj['sug']
        myQuery.setmain(request.POST['query'])
        myQuery.setjournal(request.POST['journal'])
        myQuery.setauth(request.POST['author'])
        #print(type(dict_of_sugg))
        list_names=list(dict_of_sugg.keys())
        #print(type(list_names))
        #print("*********************************************************")
        # all_scores=obj_run.getScores(request.POST['query'], request.POST['author'], request.POST['journal'])
        # pr_scores=obj_run.getPRscores()
        # all_scores=all_scores[:10]
        # pr_scores = pr_scores[:10]
        #print(type(all_scores))
        #print(list_names[1])
        #print("**********************************************************")
        #print(obj_run.getScores())
        template = loader.get_template('IRapp/category.html')
        context = {'list_of_res': list_of_res , 'list_names': list_names,'query_str':query_str, }

        return HttpResponse(template.render(context,request))
