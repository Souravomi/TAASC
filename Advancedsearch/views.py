from django.shortcuts import render, redirect 
from django.http import HttpResponse,JsonResponse
from datetime import datetime
from User.models import BasicDetails, FamilyMembers, DomesticAnimals, VegFru, Fish, Rubber,Survey
from django.apps import apps
import json
from django.core import serializers
from django.db.models import Q,FilteredRelation
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def getAll(request):
    if request.method=="POST":
        alldata = BasicDetails.objects.all()
        return render(request,'Advanced_Search.html',{
            'data':alldata
        }) 

@login_required
def Search(request):
    return render(request, 'Advanced_Search.html')

def getModelsFields(request):
    if request.method == "GET":
        table = request.GET['tbName']
    return JsonResponse(fetchColumnNames(table),safe=False)

def customSearch(request):
    if request.method=="POST":
        print("called this")
        tableName = request.POST["selectTable"]
        column1=request.POST["column1"]
        Search1=request.POST["search1"]
        Search2=request.POST["search2"]
        cond1=request.POST["cond1"]
        column2 = request.POST["column2"]

        if column1 =="None":
            column1 = None
        if cond1 =="None":
            cond1 = None
        if column2 =="None":
            column2 = None
        if Search2 =="":
            Search2=None
            
        print(cond1)
        print(column1)
        print(Search1)
        print("Data from "+ tableName)
        alldata=buildQuery(tableName,column1,cond1,Search1,column2=column2,search2=Search2)
        # data = serializers.serialize('json',alldata)
        # # return HttpResponse(data, content_type="text/json-comment-filtered")
        return render(request,'Advanced_Search.html',{
            'data':alldata
        }) 
    else:
        return HttpResponse("Not a valid route")

def buildQuery(tableNameStr,column1,condClause1,search1,isJoinCondAvailable=None,column2=None,condClause2=None,search2=None):
    if tableNameStr == "None":
        return None
    tableName = tableNameStr.lower()
    print(tableName +""+ tableNameStr)
    tableName = apps.get_model('User',tableNameStr)

    print(type(tableNameStr))
    queryData = None
    # queryData=BasicDetails.objects.filter(**{tableName+"__"+column1:search1,column2+"__"+"icontains":"Kottayam"})
    

    if column1 ==None or condClause1 ==None:
        if column2 is not None and search2 is not None:
            queryData=BasicDetails.objects.filter(**{tableNameStr:"Yes",column2+"__"+"icontains":search2})
        else:
            queryData = BasicDetails.objects.filter(**{tableNameStr:"Yes"})
       
    else:
        if condClause1 == "0":
            print("cond1 called")
            try:
                queryData = BasicDetails.objects.filter(**{tableNameStr.lower()+"__"+column1:search1})
                # queryData=BasicDetails.objects.filter(**{tableName+"__"+column1:search1})

            except:
                print("Not a valid query")

                
        elif condClause1 =="1":
            try:
                 queryData = BasicDetails.objects.filter(**{tableNameStr.lower()+"__"+column1+"__lte":search1})
                # queryData=BasicDetails.objects.filter(**{tableName+"__"+column1+"__lte":search1})
            except:
                print("Not a valid query")
                
        elif condClause1 =="2":
            try:
                 queryData = BasicDetails.objects.filter(**{tableNameStr.lower()+"__"+column1+"__gte":search1})
                # queryData=BasicDetails.objects.filter(**{tableName+"__"+column1+"__gte":search1})
            except:
                print("Not a valid query")

    if column2 is not None and search2 is not None:
        if condClause1 == "0":
            print("called condclause1")
            try:
                queryData=BasicDetails.objects.filter(**{tableNameStr.lower()+"__"+column1:search1,column2+"__"+"icontains":search2})
            except:
                print("Not a valid query")
        elif condClause1 =="1":
            try:
                queryData=BasicDetails.objects.filter(**{tableNameStr.lower()+"__"+column1+"__lte":search1,column2+"__"+"icontains":search2})
            except:
                print("Not a valid query")
        elif condClause1 =="2":
            try:
                queryData=BasicDetails.objects.filter(**{tableNameStr.lower()+"__"+column1+"__gte":search1,column2+"__"+"icontains":search2})
            except:
                print("Not a valid query")
        # queryData = BasicDetails.objects.filter(**{tableNameStr.lower()+"__"+column1:search1,column2:search2})

   

    return queryData

def fetchColumnNames(tableName):
    names =[]
    tableName = apps.get_model('User',tableName)
    for f in tableName._meta.get_fields():
        if hasattr(f, 'verbose_name'):
            formatted =f.verbose_name.replace(" ", "_")
            names.append(formatted)
            

    print(names)
    return names





#  queryData=BasicDetails.objects.filter(rubber__Count=1000,District="Kottayam")
 # if isJoinCondAvailable:
    #     if isJoinCondAvailable =="AND":
    #         pass
    #     else:
    #         pass
#     if condClause2 == "0":
    #         pass
    #     elif condClause2 =="1":
    #         pass
    #     elif condClause2 =="2":
    #         pass